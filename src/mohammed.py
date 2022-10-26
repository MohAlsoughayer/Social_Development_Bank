# %%
import numpy as np
import pandas as pd
import matplotlib as mlp
import plotly.express as px
import seaborn as sns
import arabic_reshaper 
#%%
df = pd.read_csv('../data/sdb_loans_cleaned.zip', index_col=0)
df.head()
# %%
df.groupby('job').describe()['loan_amount']
#%%
# fig = px.histogram(data_frame=df, x='job', animation_frame='year', color='job',
#  title='# Of Loans Given For Each Job Category Over The Years',
#  labels={'job':'قطاع العميل'})
# fig.update_layout(yaxis_title='العدد التمويلات')
# fig.show()

# %%
df.groupby(['gender', 'loan_type']).describe()['loan_amount']
##
# %%
df.groupby(['gender', 'loan_class']).describe()['loan_amount']
# %%
fig = px.histogram(df, x='month',
             color='gender', barmode='group',
             animation_frame='year',
             title='عدد التمويلات لكل جنس عبر السنين',
             labels={'year': 'السنه',
                     'month': 'الشهر',
                     'gender': 'جنس العميل'
                     })
fig.update_layout(yaxis_title='عدد التمويلات')
fig.show()

# %%
df['loan_class'].value_counts()
# %%
df['loan_type'].value_counts()
# %%
freelance_female_sum = df[(df.loan_type == 'التمويل الحر') & (df.gender == 'أنثى')]['loan_amount'].sum()
freelance_male_sum = df[(df.loan_type == 'التمويل الحر') & (df.gender == 'ذكر')]['loan_amount'].sum()
personal_finance_female_sum = df[(df.loan_type == 'تمويل الافراد') & (df.gender == 'أنثى')]['loan_amount'].sum()
personal_finance_male_sum = df[(df.loan_type == 'تمويل الافراد') & (df.gender == 'ذكر')]['loan_amount'].sum()
# %%
fig = px.histogram(df[(df.loan_type == 'التمويل الحر')], x='year',
             color='gender', barmode='group',
             title='عدد التمويل الحر لكل جنس عبر السنين',
             labels={'year': 'السنه',
                     'gender': 'جنس العميل'
                     })
fig.update_layout(yaxis_title='عدد التمويلات')
fig.show()
# %%
fig = px.histogram(df[(df.loan_type == 'تمويل الافراد')], x='year',
             color='gender', barmode='group',
             title='عدد تمويلات الافراد لكل جنس عبر السنين',
             labels={'year': 'السنه',
                     'gender': 'جنس العميل'
                     })
fig.update_layout(yaxis_title='عدد التمويلات')
fig.show()
# %%