#%%
import pandas as pd
import numpy as np
import plotly.express as px
import missingno as msno
import plotly.graph_objects as go
from matplotlib.pyplot import xlabel
import plotly.express as px



# %%
df = pd.read_csv("../data/sdb_loans_cleaned.csv")

df_old# %%

fig = px.histogram(df[(df.loan_type == 'تمويل نقل')], x="city", animation_frame= "year",
 title="عدد قروض (تمويل النقل)",
labels= {'city':'المدينه',
        'loan_type':'نوع القرض'})
fig.update_layout(yaxis_title= 'عدد القروض')
fig.show()



#%%

df["loan_type"].unique()


# %%
df[(df.loan_type == 'تمويل نقل')]["city"].unique()
# %%

fig = px.histogram(df[(df.loan_type == 'تمويل الاعمال')], x="city", animation_frame= "year",
 title="عدد قروض (تمويل الاعمال)",
labels= {'city':'المدينه',
        'loan_type':'نوع القرض'})
fig.update_layout(yaxis_title= 'عدد القروض')
fig.show()
fig.update_layout(yaxis_range=[0,650])


# %%
fig = px.histogram(df[(df.loan_type == 'تمويل الافراد')], x="city", animation_frame= "year",
 title="عدد قروض (تمويل الافراد)",
labels= {'city':'المدينه',
        'loan_type':'نوع القرض'})
fig.update_layout(yaxis_title= 'عدد القروض')
fig.show()

#%%
fig = px.histogram(df[(df.loan_type == 'التمويل الحر')], x="city", animation_frame= "year",
 title="عدد قروض (التمويل الحر)",
labels= {'city':'المدينه',
        'loan_type':'نوع القرض'})
fig.update_layout(yaxis_title= 'عدد القروض')



fig.show()=pd.read_csv("../data/sdb_loans.csv")
# %%

#to get cols
list(df.columns)


# %%

#removing white space only on ends and beginings
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


# %%

#to get unique values in the col
df["martial_status"].unique()

#%%

df["martial_status"].value_counts(dropna=False)


# %%

df["gender"].unique()
#array(['MALE', 'FEMALE', 'ذكر', 'أنثى', nan, 'انثى'], dtype=object)


# %%

#replacing english names
df.replace("FEMALE", "أنثى", inplace=True)
df.replace("انثى", "أنثى", inplace=True)
df.replace("MALE", "ذكر", inplace=True)


# %%
df["loan_type"].unique()


#%%
df["age"].value_counts(dropna=False)


# %%
#filling Na in age or all
df.fillna("غير معرف", inplace=True)


# %%
df.info()
# %%
df.loc[970000,"date"]

#%%
df_noage = df[df.age.isnull()]

# %%
df_noage.gender.value_counts()
# %%
df.gender.value_counts()

# %%
#converting date col type
df.date = pd.to_datetime(df.date)
# %%
#extracting the year and month
df["year"] = df.date.dt.year
df["month"]= df.date.dt.month

# %%
df.sort_values("date", inplace = True)
# %%
msno.bar(df)
# %%
df["loan_type"].unique
#df[(df.job.isnull()) | (df.job == "غير معرف" )].year.value_counts()

df.columns
# %%



#%%
x_labs = []
for item in df.loan_type.unique():
    x_labs.append(get_display(arabic_reshaper.reshape(item)))


#%%
sns.barplot(x="year", y="loan_type", data=df)








# %%
#df["year"].unique()
#!pip install arabic_reshaper


# %%

