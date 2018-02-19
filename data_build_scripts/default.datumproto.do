MAT_FILE=${2/pd_datums/pd_output}.mat
redo-ifchange $MAT_FILE

python /visionfs/ssafar_no_backup/mmbm/code/deep/mat_to_datum_proto.py --input=$MAT_FILE
