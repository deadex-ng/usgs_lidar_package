import os 
import sys
import argparse

import json
import functools
import operator 

sys.path.append('../utils')


from get_region import Region
from get_bounds import Bounds

region = Region()
bounds = Bounds()

boundaries = bounds.set_bounds(-93.756155, 41.918015, -93.747334, 41.921429)


#read json file 
json_file = open('../pipeline.json')
data = json.load(json_file)
data['pipeline'][0]['bounds']=boundaries

with open('../pipeline.json', 'w') as f:
    f.write(json.dumps(data))
