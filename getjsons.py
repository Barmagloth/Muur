#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import glob
import os
import re

def GetJsons():
    jsons_data = []
    for filename in glob.glob('TrigExport/*.json'):
        try:
            with open(os.path.join(os.getcwd(), filename), 'r') as read_file:
                jsons_data.append(json.load(read_file))
                #print (f'{read_file}')
                ret = jsons_data
        except:
            ret = 'there was an error while opening json!'
            pass
    return (ret)
# In[ ]: