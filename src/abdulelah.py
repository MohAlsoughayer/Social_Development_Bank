
#%% 
# importing packeges


import pandas as pd
import numpy as np
import arabic_reshaper
import matplotlib.pyplot as plt
import seaborn as sns
from bidi.algorithm import get_display
import plotly.express as px
import plotly.graph_objects as go
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
g.set_yticklabels(x_labs)
plt.xlabel(get_display(arabic_reshaper.reshape('تصنيف التمويل')))
plt.ylabel(get_display(arabic_reshaper.reshape('مبلغ التمويل')))
# %%
del g
# %%

df_mf= df[df.gender != 'غير معرف']

# %%
df.loan_type.value_counts()
# %%

df_mf= df[df.gender != 'غير معرف']
df_mf = df[df.loan_type == 'تمويل الافراد']
sns.violinplot(data=df_mf,  x="loan_class", y="loan_amount", hue="gender",
               split=True)
sns.despine(left=True)
plt.ylim(0, 70000)

# %%


import sys
sys.getdefaultencoding()
# %%
df_mf.loan_class.value_counts()
# %%
df_mf= df[df.gender != 'غير معرف']
df_mf = df[df.loan_type == 'التمويل الحر']

# %%

sns.violinplot(data=df_mf,  x="loan_class", y="loan_amount", hue="gender",
               split=True)
sns.despine(left=True)
plt.ylim(0, 200000)


# %%

df_mf= df[df.gender != 'غير معرف']
df_mf = df_mf[df.loan_type == 'تمويل الاعمال']
sns.violinplot(data=df_mf,  x="loan_class", y="loan_amount", hue="gender",
               split=False)
sns.despine(left=True)
plt.ylim(0, 200000)
# %%
df_mf.gender.value_counts()
# %%
df[df.loan_class =='زواج'].gender.unique()
# %%
df.describe()
# %%
df_mf= df[df.gender != 'غير معرف']
df_mf = df_mf[df.loan_type == 'تمويل نقل']
sns.barplot(data=df_mf,  x="loan_class", y="loan_amount", hue="gender",
               )

plt.ylim(0, 200000)
# %%

fig = go.Figure()

fig.add_trace(go.Violin(x=df_mf['loan_class'][ df_mf['gender'] == 'ذكر' ],
                        y=df_mf['loan_amount'][ df_mf['gender'] == 'ذكر' ],
                        legendgroup='ذكر',  name='ذكر',
                        side='negative',
                        line_color='blue')
             )
fig.add_trace(go.Violin(x=df_mf['loan_class'][ df_mf['gender'] == 'أنثى' ],
                        y=df_mf['loan_amount'][ df_mf['gender'] == 'أنثى' ],
                        legendgroup='أنثى',  name='أنثى',
                        side='positive',
                        line_color='orange')
             )
#fig.update_traces(meanline_visible=True)
#fig.update_layout(violingap=0, violinmode='overlay')
fig.show() 
# %%
df_no = df[df.loan_amount <200_000]
# %%
fig = px.treemap(df_no, path=[px.Constant("Loans"), 'loan_type', 'loan_class'],
                  color='loan_amount',
                  color_continuous_scale='RdBu', color_continuous_midpoint=100_000
                )
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()








#start from here
#%%
sns.set(rc={'figure.figsize':(10,8)})
# %%
# Graph the gender vs sum
bar_labels=[ 'ﺀﺎﺴﻨﻟﺍ','ﻝﺎﺟﺮﻟﺍ', 'ﻑﺮﻌﻣ ﺮﻴﻏ']
g1= sns.barplot(y=bar_labels,x=df.groupby('gender').loan_amount.sum())
plt.ylabel(get_display(arabic_reshaper.reshape('الصنف')))
plt.xlabel(get_display(arabic_reshaper.reshape('مجموع مبلغ التمويل')))
g1.set_xticklabels(['0','10','20','30','40'])

# %%
# graphing without the wedding laon
df_mrgless= df[df.loan_class != 'زواج']
bar_labels=[ 'ﺀﺎﺴﻨﻟﺍ','ﻝﺎﺟﺮﻟﺍ', 'ﻑﺮﻌﻣ ﺮﻴﻏ']
g11= sns.barplot(y=bar_labels,x=df_mrgless.groupby('gender').loan_amount.sum())
plt.ylabel(get_display(arabic_reshaper.reshape('الصنف')))
plt.xlabel(get_display(arabic_reshaper.reshape(('مجموع مبلغ التمويل (مليار ريال)'))
g11.set_xticklabels(['5','10','15','20','25'])

# %%

# %%
#Lets check the propotion of wedding loans to the total
mrg_percent= df[df.loan_class == 'زواج'].loan_amount.sum()/df.loan_amount.sum()
mrg_percent=round(mrg_percent*100,2)
print(mrg_percent,'%')
# %%
# graph the type vs. sum
y_labels2=['ﺮﺤﻟﺍ ﻞﻳﻮﻤﺘﻟﺍ', 'ﻝﺎﻤﻋﻻﺍ ﻞﻳﻮﻤﺗ', 'ﺩﺍﺮﻓﻻﺍ ﻞﻳﻮﻤﺗ', 'ﻞﻘﻧ ﻞﻳﻮﻤﺗ']
x2=df.groupby('loan_type').loan_amount.sum()
g2= sns.barplot(x=x2, y=y_labels2)
plt.ylabel(get_display(arabic_reshaper.reshape('الصنف')))
plt.xlabel(get_display(arabic_reshaper.reshape('مجموع مبلغ التمويل (مليار ريال)')))
g2.set_xticklabels(['0','10','20','30','40'])


# %%
# graph the type vs. counts
y_labels22=[ 'ﺩﺍﺮﻓﻻﺍ ﻞﻳﻮﻤﺗ','ﺮﺤﻟﺍ ﻞﻳﻮﻤﺘﻟﺍ', 'ﻝﺎﻤﻋﻻﺍ ﻞﻳﻮﻤﺗ','ﻞﻘﻧ ﻞﻳﻮﻤﺗ']
x2=df.loan_type.value_counts()
g22= sns.barplot(x=x2, y=y_labels22)
plt.ylabel(get_display(arabic_reshaper.reshape('الصنف')))
plt.xlabel(get_display(arabic_reshaper.reshape('عدد القروض')))

# %%
# graph thr age vs. sum
x3=df.groupby('age').loan_amount.sum()
ticks_label=['<30','30-40','40-60','>60','ﻑﺮﻌﻣ ﺮﻴﻏ']
g3= sns.barplot(x=x3, y=x3.index);
plt.ylabel(get_display(arabic_reshaper.reshape('العمر')));
plt.xlabel(get_display(arabic_reshaper.reshape('مجموع مبلغ التمويل (مليار ريال)')));
g3.set_yticklabels(ticks_label);
g3.set_xticklabels(['0','5','10','15','20']);
# %%
#graph the age vs counts
x33=df.age.value_counts()
ticks_label=['<30','30-40','40-60','>60','ﻑﺮﻌﻣ ﺮﻴﻏ']
g33= sns.barplot(x=x33, y=x33.index);
plt.ylabel(get_display(arabic_reshaper.reshape('العمر')));
plt.xlabel(get_display(arabic_reshaper.reshape('عدد القروض')));
g33.set_yticklabels(ticks_label);
# %%


# %%
