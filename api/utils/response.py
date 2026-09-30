def ResponseSuccess(success = 200 , message = "" , data = {} , other = {}):
   return { 
    success , 
    message , 
    data , 
    other
   }
def ResponseFailure(success = 500 , message = "", other = {}):
   return { 
    success , 
    message , 
    other
   }    