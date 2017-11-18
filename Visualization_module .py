
# coding: utf-8

# In[3]:


from skimage import data as imgdata
import matplotlib.pyplot as plt
import numpy as np

coffee_cup = imgdata.coffee()
plt.imshow(coffee_cup)
plt.show()


# In[4]:


#for plotting line chart
def line_chart(data_obj):v 
    '''
    Expect data_obj dictionary with keys:
    data1 : one dimension numpy array (x axis)
    data2 : one dimension numpy array (y axis)
    x_label : label for x axis
    y_label : label for y axis
    title : chart title
    
    '''
    data1 = data_obj['data1']
    data2 = data_obj['data2']
    x_label = data_obj['x_label']
    y_label = data_obj['y_label']
    title = data_obj['title']
   
    plt.plot(data1,data2)
 
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


# In[5]:


#for plotting Scatter chart
def scatter_chart(data_obj):
    '''
    Expect data_obj dictionary with keys:
    data1 : one dimension numpy array (x axis)
    data2 : one dimension numpy array (y axis)
    x_label : label for x axis
    y_label : label for y axis
    title : chart title
    
    '''
    data1 = data_obj['data1']
    data2 = data_obj['data2']
    x_label = data_obj['x_label']
    y_label = data_obj['y_label']
    title = data_obj['title']
   
    plt.scatter(data1,data2)
 
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


# In[6]:


#for plotting bar chart
def bar_chart(data_obj):
    '''
    Expect data_obj dictionary with keys:
    data1 : one dimension numpy array (y axis)
    x-axis: index label
    x_label : label for x axis
    y_label : label for y axis
    title : chart title
    
    '''
    data2 = data_obj['data1']
    data1 = np.arange(len(data_obj['data1']))
    x_label = data_obj['x_label']
    y_label = data_obj['y_label']
    title = data_obj['title']
   
    plt.bar(data1,data2)
 
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


# In[31]:


#for plotting multiline chart
def multiplot_chart(data_obj):
    '''
    Expect data_obj dictionary with keys:
    data1 : two dimension numpy array (y axis)
    x-axis: index label
    x_label : label for x axis
    y_label : label for y axis
    title : chart title
    
    '''
    data1 = data_obj['data1']
    data2 = np.arange(len(data_obj['data1'][0,:]))
    x_label = data_obj['x_label']
    y_label = data_obj['y_label']
    title = data_obj['title']
    
    for da in data1:
        plt.plot(data2,da)
    plt.legend(data_obj['legends'])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

