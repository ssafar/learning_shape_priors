

for d in PFP/train PFP/test CUB/train CUB/test; do
    echo $d/ucm.lmdb $d/orient.lmdb $d/rawpd.lmdb $d/images.lmdb $d/masks.lmdb $d/hog.lmdb
done |
xargs redo-ifchange
