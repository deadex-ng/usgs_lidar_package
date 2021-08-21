from subprocess import call 

pipeline_path = '../pipeline.json'

class PDALPipeline():
    def __init__(self):
        pass

    def run_pipeline(self,pipeline_path):
        call(["pdal","pipeline", pipeline_path])
        


        