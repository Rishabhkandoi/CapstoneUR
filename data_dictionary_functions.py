#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import os
import pickle

from datetime import datetime
import time

def get_data_dict_df():
    project_dir = 'Box\\Capstone\\Data Science Capstone'
    data_dict_excel_filename = 'Data Dictionary (2022).xlsx'
    
    data_dict_df = pd.read_excel(project_dir + '\\' + data_dict_excel_filename)
    
    data_dict_df['notes_1'] = data_dict_df['Unnamed: 5']
    data_dict_df['notes_2'] = data_dict_df['Unnamed: 6']
    data_dict_df['notes_3'] = data_dict_df['Unnamed: 7']
    
    data_dict_df = data_dict_df.drop(['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7'], axis=1)
    
    data_dict_df['notes_1'] = data_dict_df['notes_1'].fillna('')
    data_dict_df['notes_2'] = data_dict_df['notes_2'].fillna('')
    data_dict_df['notes_3'] = data_dict_df['notes_3'].fillna('')
    
    data_dict_df = data_dict_df.drop(0)
    
    data_dict_df['Number'] = data_dict_df['Number\n(Position)'].copy()
    data_dict_df = data_dict_df.drop('Number\n(Position)', axis=1)
    
    data_dict_df['Variable'] = data_dict_df['Variable Name\n(Column header)'].copy()
    data_dict_df = data_dict_df.drop('Variable Name\n(Column header)', axis=1)
    
    data_dict_df['Key'] = data_dict_df['Key'].fillna('(no key)')
    
    def get_key_dict(key_str):
        if key_str == '(no key)':
            return key_str
        else:
            key_dict = dict()
            key_list = key_str.split('\n')
            for key_pair_str in key_list:
                key_pair = key_pair_str.split(' = ')
                key_dict[key_pair[0]] = key_pair[1]
            return key_dict
    
    data_dict_df['KeyDict'] = [get_key_dict(key) for key in data_dict_df['Key']]
    
    data_dict_df = data_dict_df.drop('Key', axis=1)
    
    return data_dict_df

def get_var_definition(var_name, data_dict_df=get_data_dict_df()):
    definition = data_dict_df[data_dict_df['Variable']==var_name].iloc[0]['Definition']
    return definition