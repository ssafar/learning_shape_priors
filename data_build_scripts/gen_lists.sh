#!/bin/bash

for d in CUB/train CUB/test PFP/train PFP/test WZH/train WZH/test; do
    cat $d/list.txt | awk 'BEGIN { a=0; } {print $1 ".ucm.datumproto", a; a=a+1; }' >$d/ucm.filelist.txt
    cat $d/list.txt | awk 'BEGIN { a=0; } {print $1 ".rawpd.datumproto", a; a=a+1; }' >$d/rawpd.filelist.txt
    cat $d/list.txt | awk 'BEGIN { a=0; } {print $1 ".orient.datumproto", a; a=a+1; }' >$d/orient.filelist.txt
    cat $d/list.txt | awk 'BEGIN { a=0; } {print $1 ".png", a; a=a+1; }' >$d/images.filelist.txt
    cat $d/list.txt | awk 'BEGIN { a=0; } {print $1 ".png", a; a=a+1; }' >$d/masks.filelist.txt
    cat $d/list.txt | awk 'BEGIN { a=0; } {print $1 ".hog.datumproto", a; a=a+1; }' >$d/hog.filelist.txt
done
