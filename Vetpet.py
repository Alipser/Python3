import pandas as pd
import numpy as np

nombres= ["Martín", "Milú", 'Anastasia', 'Lupita', 'Tomasa', 'Pelusa', 'Genoveva', 'Motita']
tipos= ['canino', 'canino', 'felino', 'felino', 'felino', 'canino', 'bovino', 'roedor' ]
edades= [12, 9, 10, 8, 9, 2, 14, 1 ]
pesos= [33, 26, 4, 5, 5, 6, 106.4, 0.34 ]


########################################################################################################################

#Primer Diccionario del reto key:Index str zip((nombres,tipos,edades,pesos))
D1_key=list(map(str,(list(range(1,len(nombres)+1)))))
Dict_patient_init=dict(zip((D1_key),list(map(list,(zip(nombres,tipos,edades,pesos))))))
print(Dict_patient_init)

########################################################################################################################

#Segundo Dicionario Key:str Index remover raedores y bovinos:

#manupulating data as dataframe.

first_df_onlife=pd.DataFrame(list(zip(nombres,tipos,edades,pesos)), columns=[ "Nombre","tipo","edades","pesos"])


#removing type bovino and roedor
Erase_index = set(list(first_df_onlife[ first_df_onlife['tipo'] == 'bovino'].index)\
              + list(first_df_onlife[ first_df_onlife['tipo'] == 'equino'].index)\
              + list(first_df_onlife[ first_df_onlife['tipo'] == 'roedor'].index)\
              + list(first_df_onlife[ first_df_onlife['edades'] < 9].index))
first_df_onlife.drop(Erase_index , inplace=True)
if first_df_onlife.empty:
    mean1=None
else:
    mean1=first_df_onlife['edades'].mean()
mean1=first_df_onlife['edades'].mean()
first_df_onlife=first_df_onlife.reset_index(drop=True)
key2=list(range(1,(first_df_onlife.shape[0]+1)))
#creating the second dict
first_df_onlife=first_df_onlife.assign(KeyDict=key2)
first_df_onlife=first_df_onlife.reindex(columns=["KeyDict", "Nombre", "tipo", "pesos"])
first_df_onlife['KeyDict']=first_df_onlife['KeyDict'].astype(str)
first_df_onlife=first_df_onlife.set_index('KeyDict').T.to_dict('list')
print(first_df_onlife)
#########################################################################################################################

#Third Dicctionary: str Index remover raedores y caninos felinos:

first_df_onlife=pd.DataFrame(list(zip(nombres,tipos,edades,pesos)), columns=[ "Nombre","tipo","edades","pesos"])

#removing type bovino and roedor
Erase_index = set(list(first_df_onlife[ first_df_onlife['tipo'] == 'canino'].index)\
              + list(first_df_onlife[ first_df_onlife['tipo'] == 'felino'].index)\
              + list(first_df_onlife[ first_df_onlife['tipo'] == 'roedor'].index)\
              + list(first_df_onlife[ first_df_onlife['edades'] < 16].index))
first_df_onlife.drop(Erase_index , inplace=True)
if first_df_onlife.empty:
    mean2=None
else:
    mean2=first_df_onlife['edades'].mean()
first_df_onlife=first_df_onlife.reset_index(drop=True)
key2=list(range(1,(first_df_onlife.shape[0]+1)))
#creating the third dict
first_df_onlife=first_df_onlife.assign(KeyDict=key2)
first_df_onlife=first_df_onlife.reindex(columns=["KeyDict", "Nombre", "tipo", "edades" ,"pesos"])
first_df_onlife['KeyDict']=first_df_onlife['KeyDict'].astype(str)
first_df_onlife=first_df_onlife.set_index('KeyDict').T.to_dict('list')
print(first_df_onlife)
############################################################################################################################
print(mean1)

print(mean2)












