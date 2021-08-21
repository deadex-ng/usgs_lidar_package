import os 
import sys
import argparse

import json
import functools
import operator 

sys.path.append('../utils')


from get_region import Region
from get_bounds import Bounds
from file_handler import FileHandler
from pipeline import PDALPipeline

region = Region()
bounds = Bounds()
file_handler_obj = FileHandler()
PDALPipeline = PDALPipeline()


boundaries = bounds.set_bounds(-93.756155, 41.918015, -93.747334, 41.921429)

#check if region exists
#flag = region.check_region_exists('IA_FullState')

region_url = region.set_region('IA_FullState')
output_file = file_handler_obj.set_output_file_name('iowa')

#print("LAZ:", output_file[0])
#print("TIF:",output_file[1])

#read json file 
json_file = open('../pipeline.json')
data = json.load(json_file)

#edit json file 
data['pipeline'][0]['bounds']=boundaries
data['pipeline'][0]['filename']=region_url
data['pipeline'][6]['filename']=output_file[0]
data['pipeline'][7]['filename']=output_file[1]
with open('../pipeline.json', 'w') as f:
    f.write(json.dumps(data))


pipeline_path = '../pipeline.json'
PDALPipeline.run_pipeline(pipeline_path)