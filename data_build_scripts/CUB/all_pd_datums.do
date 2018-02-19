for d in `find pd_output/ -name '*.mat'`; do
    TARGET=${d/pd_output/pd_datums}
    echo ${TARGET%.mat}.datumproto
done |
xargs redo-ifchange
