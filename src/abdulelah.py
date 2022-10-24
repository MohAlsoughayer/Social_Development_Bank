
#%% 
# importing packeges


import pandas as pd
import numpy as np

# %%

df= pd.read_csv('../data/sdb_loans.zip')
# %%
df.head()
# %%

print(df.city.unique())
# %%
def con_cities(city_name):
    '''
    Clean the city names by removing duplicates and fixing spleeing mistakes
    '''
    if "بنك التنمية الإجتماعية فرع " in city_name:
        city_name = city_name.replace('بنك التنمية الإجتماعية فرع ','')
    if "بنك التنمية الإجتماعية ب" in city_name:
        city_name = city_name.replace("بنك التنمية الإجتماعية ب" ,'') # removing the repeated phrase
    if 'ه' in city_name:
        city_name = city_name.replace('ه','ة') # fixing spelling mistake
    if "إ" in city_name:
        city_name = city_name.replace('إ','أ')
    if "ى" in city_name:
        city_name = city_name.replace('ى','ي')
    if "  " in city_name:
        city_name =  city_name.replace('  ',' ')

    if city_name == 'المدينة':
        city_name = 'المدينة المنورة' # consistant name for Medina 
    
    if city_name == 'مكة':
        city_name = 'مكة المكرمة' # consistant name for Makkah 
    return city_name
# %%
df.city = df.city.map(con_cities)
print(df.city.unique())

# %%
# Checking for the unique values.
df.city.value_counts()


# %%
# Cleaning the loan_type
df.loan_type.value_counts()



# %%
def con_types(loan_type):
    '''
    Cleaning the loan_type column
    '''
    if loan_type==  "حر":
        loan_type=  "التمويل الحر"
    if loan_type== "نقل":
        loan_type = 'تمويل نقل'
    
    if loan_type == "مشروع":
        loan_type = 'تمويل الاعمال' # From the loan_class, it seems that those two are the same
    if loan_type== "إجتماعي":
        loan_type = 'تمويل الافراد'# From the loan_class, it seems that those two are the same
    return loan_type
# %%
df.loan_type  = df.loan_type.map(con_types)
df.loan_type.value_counts()
# %%
print(df.groupby('loan_type').loan_class.value_counts())


# %%
len(df.loan_class.unique())
# 44 differnet classes
# %%
def con_classes(loan_class):
    '''
    
    '''
    if  'قرض ' in loan_class:
        loan_class=loan_class.replace('قرض ','')
    return loan_class
# %%
df.loan_class = df.loan_class.map(con_classes)
# %%
df.loan_class.value_counts()
# %%
