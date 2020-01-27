import pandas as pd
elsevier=pd.read_excel('../Original Data/elsevier_active.xls')
num2issn=lambda x: x[:4]+'-'+x[4:]
elsevier.ISSN=elsevier.ISSN.map(num2issn)
elsevier.to_csv('../Analysis Data/elsevier_journals.csv')
