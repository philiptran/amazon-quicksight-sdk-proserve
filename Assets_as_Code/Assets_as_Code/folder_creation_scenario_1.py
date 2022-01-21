"""
This script template is for dev/admin to copy folder structure from a source dataset to a target dataset.
Author: Ying Wang
Email: wangzyn@amazon.com or ywangufl@gmail.com
Version: Nov-20-2021
Note:
    configuration are in ./config folder
    library are in ./library folder
    imported functions are in ./src folder
    migration folder is for migrating exisiting QS assets accross differnt accounts/regions.
    exported_results folder stores some sample QS API exported results.
    log folder stores logs
Thank you and enjoy the open source self-service BI!
"""

"""
import libraries
"""
import boto3
import time
import json
import sys
import src
import src.functions as func
import src.supportive_functions as s_func

#load analysis library
f = open('library/1st_class_assets/data_set_library.json')
l_dataset = json.load(f)

#load dev and prod account configuration
f = open('config/dev_configuration.json', )
dev_config = json.load(f)
f = open('config/prod_configuration.json', )
prod_config = json.load(f)

#start quicksight session
qs_session = s_func._assume_role(dev_config["aws_account_number"], dev_config["role_name"],  dev_config["aws_region"])

# provide the name of source dataset we would like to copy the folders from
name = 'template_1'
# provide the id of the target dataset
target_dataset_id = 'copy_t_1'

# please provide the template analysis name you would like to copy
source_dataset_id = l_dataset[name]    # analysisid = l_analysis['sample_analysis_name']

"""automation process
step 1 of scenario 1: copy a template analysis and then edit in dev account/folder
"""
faillist = [] #define log array to record errors
successlist = [] #define log array to record success

try:
    sample_folder_creation = func.folder_creation_source_dataset (qs_session, source_dataset_id, target_dataset_id, [])
except Exception as e:
    faillist.append({
        "Action": "folder_creation",
        "Error Type": "folder_creation_source_dataset Error",
        "AnalysisID": source_dataset_id,
        "Name": name,
        "Error": str(e)
    })




