redo-ifchange $2.filelist.txt



if [ -d $2.lmdb ] ; then
    rm -rf $2.lmdb
fi

if [ $(basename $2) == "images" ]; then
    SOURCE_DIR=$(dirname $2)/../images
    ~/local/caffe/build/tools/convert_imageset $SOURCE_DIR/ $2.filelist.txt $3 --backend=lmdb
elif [ $(basename $2) == "masks" ]; then
    SOURCE_DIR=$(dirname $2)/../masks
    ~/local/caffe/build/tools/convert_imageset $SOURCE_DIR/ $2.filelist.txt $3 --backend=lmdb
else
    SOURCE_DIR=$(dirname $2)/../pd_datums
    cat $2.filelist.txt | awk "{ print \"$SOURCE_DIR/\" \$1 }" | xargs redo-ifchange
    ~/local/caffe/build/tools/convert_datum_set $SOURCE_DIR/ $2.filelist.txt $3 --backend=lmdb
fi
