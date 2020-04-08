#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Renaming Columns and Skipping Rows#


# In[271]:


import pandas as pd
import numpy as np


# In[272]:


olympics_df = pd.read_csv('olympics.csv', header=1 )


# In[273]:


olympics_df.head()


# In[275]:


new_names =  {'Unnamed: 0': 'Country',
              '? Summer': 'Summer Olympics',
              '01 !': 'Gold',
              '02 !': 'Silver',
              '03 !': 'Bronze',
              '? Winter': 'Winter Olympics',
              '01 !.1': 'Gold.1',
              '02 !.1': 'Silver.1',
              '03 !.1': 'Bronze.1',
              '? Games': '# Games',
              '01 !.2': 'Gold.2',
              '02 !.2': 'Silver.2',
              '03 !.2': 'Bronze.2'}


# In[276]:


olympics_df.rename(columns=new_names, inplace=True)


# In[278]:


olympics_df.head()


# In[ ]:




