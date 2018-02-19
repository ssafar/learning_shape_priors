for d in pd_output/*.mat; do
    TARGET=${d/pd_output/pd_datums}
    echo ${TARGET%.mat}.datumproto
done |
xargs redo-ifchange
