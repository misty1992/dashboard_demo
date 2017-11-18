
# coding: utf-8

# In[ ]:


def plot_dict_gen_for_sales(a):
    
    plot_input ={}
    
    plot_legends = []
    factory_data = []
    
    for factory_id in np.arange(a.shape[2]):
        factory_data.append(np.sum(a,axis=0)[:,factory_id])
        plot_legends.append('factory_' + str(factory_id))
    
    plot_input['data'] = np.array(factory_data)
    plot_input['legends'] = plot_legends
    plot_input['x_label'] = 'Time (months)'
    plot_input['y_label'] = 'sales'
    plot_input['title'] = 'Sales for each factory across years'
        
    return plot_input

plot_dict_gen_for_sales(coffee_cup)

