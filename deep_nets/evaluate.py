# %pylab inline
# import pdb

import numpy as np
from scipy import misc
from scipy import io
import os
import fnmatch
import gflags

FLAGS = gflags.FLAGS

import sys
sys.path.append('/home/ssafar/local/caffe/python');
import caffe

from scipy import ndimage
from scipy import misc

def striped_mask(image, mask):
    rows, cols, channels = image.shape
    mask_resized = misc.imresize(mask, (rows,cols)) > 0

    mg_cols, mg_rows = np.meshgrid(np.arange(cols), np.arange(rows))
    # the red positive stripes
    stripe_mask_1 = np.mod(mg_cols + mg_rows, 5) == 0
    stripe_mask_2 = np.mod(mg_cols + mg_rows, 5) == 1

    imcpy = image.copy()

    imcpy[:,:,0][np.bitwise_and(stripe_mask_1, mask_resized)] = 255
    imcpy[:,:,1][np.bitwise_and(stripe_mask_1, mask_resized)] = 0

    outline = ndimage.morphology.binary_dilation(mask_resized, iterations=2) - mask_resized
    imcpy[np.repeat(outline[:, :, np.newaxis], 3, 2)] = 255

    return imcpy

def load_classifier(net_name, snapshot_name, model_file=None):
    model_dir = os.path.join("/visionfs/ssafar_no_backup/mmbm/deep_nets", net_name);

    if not model_file:
        model_files = [f for f in os.listdir(model_dir) if fnmatch.fnmatch(f, "model_*.prototxt")]
        assert(len(model_files)== 1)
        model_file = model_files[0]

    classifier = caffe.Net("/visionfs/ssafar_no_backup/mmbm/deep_nets/dummy_model.prototxt")
    classifier.set_mode_gpu()
    classifier.set_phase_test()
    classifier = caffe.Net(os.path.join(model_dir, model_file),
                       os.path.join(model_dir, snapshot_name))

    return classifier


def evaluate(net_name, snapshot_name, dataset, model_file=None):
    classifier = load_classifier(net_name, snapshot_name, model_file)
        
    if "global_r32" in classifier.blobs:
        print "Shape prior:"
        eval_layer(classifier, gt="mask_r32", ours="global_r32", dataset=dataset)

    if "patchsecond_sigm_r64" in classifier.blobs:
        print "Patch-match:"
        eval_layer(classifier, gt="mask_r64", ours="patchsecond_sigm_r64", dataset=dataset)

    if "good_mask_r64" in classifier.blobs:
        print "GT:"
        eval_layer(classifier, gt="mask_r64", ours="good_mask_r64", dataset=dataset)

def dataset_params(dataset):
    return {"pfp": {"height": 128, "num_test": 446},
            "cub": {"height": 64, "num_test": 3000},
            "wzh": {"height": 64, "num_test": 200}}[dataset]

def eval_layer(classifier, gt, ours, dataset):
    params = dataset_params(dataset)
    height = params["height"]
    num_test = params["num_test"]

    good = 0.0
    bad = 0.0
    union =0.0
    intersect = 0.0
    for iter in range(num_test/2):
        classifier.forward()

        if (iter % (num_test / 100)) == 0:
            sys.stdout.write(".")
            sys.stdout.flush()
        gt_mask = classifier.blobs[gt].data > 0
        our_mask = classifier.blobs[ours].data.reshape((-1, 1, gt_mask.shape[2], gt_mask.shape[3])) > 0

        assert(gt_mask.shape[0] == our_mask.shape[0])

        for im_id in range(gt_mask.shape[0]):
            this_gt = gt_mask[im_id, 0].flatten()
            this_ours = our_mask[im_id, 0].flatten()
            good += np.sum(this_gt==this_ours)
            bad += np.sum(this_gt != this_ours)
            intersect += np.sum(np.logical_and(this_gt==1, this_ours==1) )
            union += np.sum(np.logical_or(this_gt==1, this_ours==1))

    ap, iou = good / (good+bad), intersect / union
    print "results: AP: %f IOU: %f" % (ap, iou)

    return ap, iou

if __name__ == "__main__":
    gflags.DEFINE_string("net_name", None, "Name of the dir containing the net.")
    gflags.DEFINE_string("dataset", None, "Which dataset shall we do the eval on?")
    gflags.DEFINE_string("snapshot", None, "Which snapshot?")
    gflags.DEFINE_string("model_file", None, "Which model?")
    sys.argv = FLAGS(sys.argv)

    evaluate(FLAGS.net_name, FLAGS.snapshot, FLAGS.dataset, FLAGS.model_file)

