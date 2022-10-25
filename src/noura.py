import pandas as pd
import numpy as np

df = pd.read_csv("../data/sdb_loans.zip")

df.info()
df.shape[0]
df.isnull().sum()


#%% 
#Standardize the values in the spl_needs column
def special_needs(spl):
    if spl=="ذوي الاحتياجات الخاصة" :
        spl = "نعم"
    if spl== "سليم":
        spl ="لا"
    return spl

# %%
df.spl_needs = df.spl_needs.map(special_needs)

pd.crosstab(index= df["spl_needs"],columns="freq")
print(df.spl_needs.unique()) 

#%%
#Reclassifying the groups in family_members coulmn.
def family_count(famcnt):
    if famcnt == "< 02":
        famcnt= "less than 2"
    if famcnt == ">= 02":
        famcnt = "2 to 4"
    if famcnt == ">= 05":
        famcnt = "5 to 9"
    if famcnt == ">= 10":
        famcnt = "10 and above"
    return famcnt
#%%
df.family_members= df.family_members.map(family_count)

pd.crosstab(index=df["family_members"],columns= "freq")
print(df.family_members.unique())

# %%
#Redefined the groups in saving_loan coulmn
def s_loans(sloans):
    if sloans =="0":
        sloans= "لا"
    if sloans == 0:
        sloans= "لا"
    if sloans == "1":
        sloans ="نعم"
    if sloans == 1:
        sloans = "نعم"
    return sloans
#%%
df.saving_loan = df.saving_loan.map(s_loans)

pd.crosstab(index=df["saving_loan"],columns= "freq")

# %%
#Redefined the groups in income coulmn

def salary(sal):
    if sal == "<5000":
        sal= "< 5000"
    if  sal == ">=5000":
        sal = ">= 5000"
    if sal ==">=7500":
        sal = ">= 7500"
    if sal == ">=10000":
        sal = ">= 10000"
    if sal == 0:
        sal = "0"
    if sal == 6000:
        sal = "6000"
    return sal
#%%
df.income = df.income.map(salary)  

pd.crosstab(index=df["income"],columns= "freq")   
print(df.income.unique())

# %%
print(df.income.unique())
# %%
df.isnull().sum()
