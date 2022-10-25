#%%
import pandas as pd
import numpy as np
import plotly.express as px
import missingno as msno


# %%

df=pd.read_csv("../data/sdb_loans.csv")
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
df["age"].unique()


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

#df[(df.job.isnull()) | (df.job == "غير معرف" )].year.value_counts()


# %%
