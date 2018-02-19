#!/bin/bash

for DATASET in pfp cub wzh; do
    for STAGE in stage1 stage2 stage3 toy_story; do
        pyratemp_tool.py -f common.yaml -f $DATASET.yaml -f $STAGE.yaml meta_model.prototxt.template >model_${DATASET}_$STAGE.prototxt
        pyratemp_tool.py -f common.yaml -f $DATASET.yaml -f $STAGE.yaml solver.prototxt.template >solver_${DATASET}_$STAGE.prototxt
        pyratemp_tool.py -f common.yaml -f $DATASET.yaml -f $STAGE.yaml train.sh.template >train_${DATASET}_$STAGE.sh

        chmod a+x train_${DATASET}_$STAGE.sh
    done
done

