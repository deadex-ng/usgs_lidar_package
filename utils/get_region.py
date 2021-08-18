
class Region():
    def __init__(self):
        #self.region = region
        pass   
    
    def check_region_exists(self,region):
        flag = 0 
        try:
            with open('../regions.txt') as f:
                if region in f.read():
                    #region found 
                    flag = 1
                    
                else:
                    #region not found
                    flag =0 
                    
        except Exception:
            print('Failed to read text file')
        return flag
    
    def get_regions_list(self):
        try:
            with open('../regions.txt') as f:
                region = f.read()
                print(region)
        except Exception:
            print('Failed to read text file')
            
#region = Region()
#region.check_region_exists('PRE AK_BrooksCamp_2012/')
#region.check_region_exists('Malawi')
            