class FileHandler():
    
    def __init__(self):
        pass 
    
    def set_output_file_name(self,file_name:str):
        output_name_laz = 'laz/' + str(file_name) +'.'+ 'laz'
        output_name_tif = 'tif/' + str(file_name) +'.' +'tif'
        
        return output_name_laz, output_name_tif
     