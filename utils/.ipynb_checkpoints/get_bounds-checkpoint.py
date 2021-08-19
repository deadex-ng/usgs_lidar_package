class Bounds():
    def __init__(self):
        pass
    
    def set_bounds(self,min_x,max_x,min_y,max_y):
        min_x = str(min_x)
        max_x = str(max_x)
        min_y = str(min_y)
        max_y = str(max_y)
        
        bounds =  '(' + '[' + min_x + ',' + max_x + ']' + ',' + '['+ min_y +','+ max_y + ']'+ ')'
        
        return bounds
    
    def check_bounds_range():
        pass 

#obj = Bounds()
#print(obj.set_bounds(1,2,3,4))