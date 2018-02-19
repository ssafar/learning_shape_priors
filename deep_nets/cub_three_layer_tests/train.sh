#!/bin/bash

~/local/caffe/build/tools/caffe -weights=/home/ssafar/local/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel --solver=solver_segm_cub_patches.prototxt train
