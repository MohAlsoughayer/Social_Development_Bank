# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv('../data/sdb_loans.zip')
df.head()
# %%
def clean_job(job):
    # ask group about the retired grouping
    if job == 'غير محدد':
        job = 'غير معرف'
    if job == 'موظف قطاع خاص':
        job = 'قطاع خاص'
    if job == 'شركة حكومية' or job == 'موظف شركة حكومية' or job == 'موظف حكومي':
        job = 'قطاع حكومي'
    return job
# %%
def clean_loan_amount(loan_amount):
    # All float 
    if type(loan_amount) == 'str':
        loan_amount = float(loan_amount)
    return loan_amount
# %%
def clean_loan_pmt(loan_pmt):
    # get rid of spaces
    if loan_pmt == '>= 1000':
        loan_pmt = '>=1000'
    elif loan_pmt == '< 1000':
        loan_pmt = '<1000'
    return loan_pmt
# %%
df.job = df.job.map(clean_job)
df.job.unique()
# %%
df.loan_amount = df.loan_amount.map(clean_loan_amount)
df['loan_amount'].plot.density()
# %%
df.loan_pmt = df['loan_pmt'].map(clean_loan_pmt)
df['loan_pmt'].unique()
# %%
df['loan_pmt'].value_counts()
# %%
df.info()
# %%
