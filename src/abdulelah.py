
#%% 
# importing packeges


import pandas as pd
import numpy as np
import arabic_reshaper
import matplotlib.pyplot as plt
import seaborn as sns
from bidi.algorithm import get_display

#pip install python-bidi
# %%
df= pd.read_csv('/workspaces/Social_Development_Bank/data/sdb_loans_cleaned.zip')
#%%
x_labs = [ ]

for item in df.loan_type.unique():
    x_labs.append(get_display(arabic_reshaper.reshape(item)))
# %%

g_title=get_display(arabic_reshaper.reshape('الجنس'))

g_labels=  [ ]
for item in df.gender.unique():
    g_labels.append(get_display(arabic_reshaper.reshape(item)))

# %%
# Initialize the figure
f, ax = plt.subplots()
sns.despine(bottom=True, left=True)

# Show each observation with a scatterplot
g=sns.stripplot(
    data=df_mf, x="loan_type", y="loan_amount", hue="gender",
    dodge=True, alpha=.01, zorder=1,jitter=True
)
plt.legend(title=g_title, loc='upper left', labels=g_labels)
plt.ylim(0, 500000)
g.set_xticklabels(x_labs)
plt.xlabel(get_display(arabic_reshaper.reshape('تصنيف التمويل')))
plt.ylabel(get_display(arabic_reshaper.reshape('مبلغ التمويل')))
# %%

# %%

df_mf= df[df.gender != 'غير معرف']

# %%

df_mf= df[df.gender != 'غير معرف']
sns.violinplot(data=df_mf,  x="loan_type", y="loan_amount", hue="gender",
               split=True)
sns.despine(left=True)
plt.ylim(0, 500000)
# %%
