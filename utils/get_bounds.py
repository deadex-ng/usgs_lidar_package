from pyproj import CRS, Transformer

class Bounds():
    def __init__(self):
        pass
    
    def set_bounds(self,min_x,min_y,max_x,max_y):
        #min_x = str(min_x)
        #max_x = str(max_x)
        #min_y = str(min_y)
        #max_y = str(max_y)
        
        transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
        
        min_x, min_y = transformer.transform(min_x, min_y)
        max_x, max_y = transformer.transform(max_x, max_y)
        
        bounds =  '(' + '[' + str(min_x) + ',' + str(max_x) + ']' + ',' + '['+ str(min_y) +','+ str(max_y) + ']'+ ')'
        '''
        print("----min-----")
        print("min_x",min_x)
        print("min_y",min_y)
        print("----max-----")
        print("max_x",max_x)
        print("max_y",max_y)
        '''
        return bounds
    
    def check_bounds_range():
        pass 

#obj = Bounds()
#print(obj.set_bounds(-93.756155,41.918015,-93.747334,41.921429))