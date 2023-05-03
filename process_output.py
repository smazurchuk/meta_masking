# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:29:06 2023

This processes the output of the meta-mask file

@author: Stephen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

# Get most recent filename 
fname = sorted(glob('data/*meta-mask2*.csv'))[-1]; print(fname)

# Load file
df = pd.read_csv(fname)

# Pull out relevant information
relation   = {'a':1,'q':2,'d':3,'e':4}
true_img   = np.array([int(k.split('_stim')[0][-1]) for k in df.imgName if isinstance(k, str)])
response   = np.array([relation[k] for k in df['mainTrial_response.keys'] if not pd.isna(k)])
actual_soa = np.array([k for k in (df['mask.started'] - df['stim.stopped']) if not pd.isna(k)])*1000
target_soa = np.array([k for k in df.soa if not pd.isna(k)])*1000
jitter     = np.array([k for k in df.jitter if not pd.isna(k)])

# Create a plot of reaction times
print(f'Accuracy: {(response == true_img).sum()}')
plt.scatter(target_soa,(response==true_img)+((np.random.rand(len(actual_soa))*.1)-.05))
plt.xlabel('SOA (ms)')

# Cool, let's get the accuracy
u_values  = np.unique(np.round(actual_soa))
responses = (response==true_img)
accs = []
for u_value in u_values:
    ids = (u_value == np.round(actual_soa))
    t = responses[ids]
    accs.append(t.sum()/len(t))
plt.plot(u_values, accs,'-o')
    


# Let's verify actual SOA verses target SOA
t = np.array([k for k in (df['mask.started'] - df['stim.stopped']) if not pd.isna(k)])

