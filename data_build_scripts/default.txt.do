# For the list.txt files in the train / test dirs.
TRAIN_OR_TEST_DIR=$(dirname $2)

redo-ifchange $TRAIN_OR_TEST_DIR/../list.mat
TRAIN_OR_TEST=$(basename $TRAIN_OR_TEST_DIR)

../code/deep/list_mat2txt.py --input=$TRAIN_OR_TEST_DIR/../list.mat --cell=${TRAIN_OR_TEST}list
