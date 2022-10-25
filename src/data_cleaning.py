# importing packeges
import pandas as pd
import numpy as np

#import the data
df= pd.read_csv('/workspaces/Social_Development_Bank/data/sdb_loans.zip')

#remove unnamed columns
df.drop('Unnamed: 0', axis=1, inplace=True)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


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


df.city = df.city.map(con_cities)

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

df.loan_type  = df.loan_type.map(con_types)

def con_classes(loan_class):
    '''
    
    '''
    if  'قرض ' in loan_class:
        loan_class=loan_class.replace('قرض ','')
    return loan_class

df.loan_class = df.loan_class.map(con_classes)

# Mohammed cleaning


def clean_job(job):
    # ask group about the retired grouping
    if job == 'غير محدد':
        job = 'غير معرف'
    elif job == 'موظف قطاع خاص':
        job = 'قطاع خاص'
    elif job == 'شركة حكومية' or job == 'موظف شركة حكومية' or job == 'موظف حكومي':
        job = 'قطاع حكومي'
    # elif job == 'متقاعد تأمينات' or job == 'متقاعد حكومي':
    #     job = 'متقاعد'
    return job

def clean_loan_amount(loan_amount):
    # All float 
    if type(loan_amount) == 'str':
        loan_amount = float(loan_amount)
    return loan_amount

def clean_loan_pmt(loan_pmt):
    # get rid of spaces
    if loan_pmt == '>= 1000':
        loan_pmt = '>=1000'
    elif loan_pmt == '< 1000':
        loan_pmt = '<1000'
    return loan_pmt

df.loan_amount = df.loan_amount.map(clean_loan_amount)
df.loan_pmt = df['loan_pmt'].map(clean_loan_pmt)
df.job = df.job.map(clean_job)


# Dona
#replacing english names
df.replace("FEMALE", "أنثى", inplace=True)
df.replace("انثى", "أنثى", inplace=True)
df.replace("MALE", "ذكر", inplace=True)

#extracting the year and month
df.date = pd.to_datetime(df.date)
df["year"] = df.date.dt.year
df["month"]= df.date.dt.month

#filling Na in age or all
df.fillna("غير معرف", inplace=True)


# Noura

def special_needs(spl):
    if spl=="ذوي الاحتياجات الخاصة" :
        spl = "نعم"
    if spl== "سليم":
        spl ="لا"
    return spl

df.spl_needs = df.spl_needs.map(special_needs)


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

df.family_members= df.family_members.map(family_count)

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
df.saving_loan = df.saving_loan.map(s_loans)
 
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


df.income = df.income.map(salary) 

df.to_csv('data/sdb_loans_cleaned.csv')


