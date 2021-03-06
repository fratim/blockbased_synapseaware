
makeflow_directory  = "/n/pfister_lab2/Lab/tfranzmeyer/exp_code/blockbased_synapseaware/makeflow_example/"
checkfile_folder    = "/n/pfister_lab2/Lab/tfranzmeyer/exp/output_files_kimi/check_files/Zebrafinch/"
stdout_folder       = "/n/pfister_lab2/Lab/tfranzmeyer/exp/output_files_kimi/stdout_files/Zebrafinch/"
stderr_folder       = "/n/pfister_lab2/Lab/tfranzmeyer/exp/output_files_kimi/stderr_files/Zebrafinch/"

blockconsumption = 1024*1024*1024*8/1000/1000

RAM_HF_S1_S4  = 110000
RAM_HF_S2     = 110000
RAM_HF_S3     = 110000
RAM_SK_S1_S2  = 110000
RAM_SK_S3     = 110000
RAM_SK_S4     = 30000
RAM_ST_S1     = 130000
RAM_ST_S2     = 110000

cluster_partition = "test"
job_time = "0-00:59"
max_remote = 5

######## ONLY VALID for Kimimaro (benchmark)
kimi_load_synapses = True
