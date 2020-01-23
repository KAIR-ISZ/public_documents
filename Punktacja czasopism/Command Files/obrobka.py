# %%
import pandas as pd
# %%
mnisw=pd.read_excel('lista_mnisw.xlsx',skiprows=3)
# %%
jcr=pd.read_excel('JCR.xlsx',skiprows=2)
# %%
jcr=jcr.drop(['Total Cites', 'Unnamed: 3', 'Eigenfactor Score', 'Unnamed: 6','Unnamed: 7'],axis=1)
# %%
mnisw_AEE_ITT=(mnisw.loc[:,['Lp.','Tytuł 1','issn','Punkty',   'e-issn',202,203]]
               .dropna(subset=[202,203],how='all')
               .merge(jcr, left_on='Tytuł 1',right_on='Full Journal Title',how='left')
               .rename(columns={'Lp.':'Numer z listy MNISW',
                                202:'AEE',
                                203:'ITT',
                                'Journal Impact Factor':'IF'})
               .set_index('Numer z listy MNISW')
               .drop(['Full Journal Title','Rank'],axis=1)
              )
# %%
mnisw_AEE_ITT.loc[:,['AEE','ITT']]=(mnisw_AEE_ITT.loc[:,['AEE','ITT']]
                                    .fillna(False)
                                    .replace({'x':True}))
# %%
mnisw_AEE_ITT['IF']=pd.to_numeric(mnisw_AEE_ITT['IF'],errors='coerce')
# %%
mnisw_AEE_ITT.head()
# %%
import matplotlib.pyplot as plt
# %%
mnisw_AEE_ITT[mnisw_AEE_ITT.AEE].plot(kind='scatter',y='Punkty',x='IF')
plt.savefig('test.png', bbox_inches='tight')
plt.show()
# %%
mnisw_AEE_ITT.to_csv('Punktacja_MNISW_oraz_IF_dla_AEE_i_ITT.csv')
# %% markdown
# ## Jak używać
# Aby sobie odfiltrować publikacje w danej punktacji dyscyplinie trzeba zmienić warunek poniżej.
# %%
pd.set_option('display.max_rows',100)
mnisw_AEE_ITT[(mnisw_AEE_ITT.AEE)&(mnisw_AEE_ITT.Punkty==100)].iloc[0:100,:]
# %%
