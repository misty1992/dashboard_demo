
# coding: utf-8

# In[45]:


from skimage import data as imgdata
import matplotlib.pyplot as plt
import numpy as np

#coffee_cup= imgdata.coffee()
#data=np.sum(coffee_cup,(1,2))

def chk_dim(data):
    try:
            print('Num factories:', data.shape[2])
            print('Num of month:', data.shape[1])
            print('Number of products:', data.shape[0])
            return True
         
    except:
            print('right data but wrong dimenson. Enter data with d=3')
            return False 
    

def chk_data_type(data):
    
    if isinstance(data,np.ndarray):
        return True
        
    else:
        print("wrong data type. enter an 3-d array")
        return False

def chk_negative(data):
    data=np.array(data)
    if np.any(data<0)==True:
        print("sales cannot be negative") 
        return False 
    else:
        return True 

def data_ingestion(data):
    
    data_validity = False
    
    if chk_data_type(data)==True:
        chk_negative(data)
        if chk_negative(data)==True:
            chk_dim(data)
            if chk_dim==True:
                data_validity = True
            
    return data_validity




        


# In[36]:




