import pandas as pd
import numpy as np

file=pd.read_excel('Cleaned COVID Cumulative Cases.xlsx')
dates=pd.read_excel('Dates.xlsx')
final=pd.read_excel('Final COVID Doc.xlsx')



#Repeating District Names
districts=file['District']
#districts.drop(736,inplace=True)
final['District']=districts.repeat(221)


#Repeating Dates
test_dates=np.array(dates['Dates'])
final['Dates'] = pd.np.tile(test_dates,len(districts))

#file.drop(736,inplace=True)
file=file.transpose()
file.columns=file.iloc[0]
file.drop('District',axis=0,inplace=True)

file.to_excel('Cumulative_COVID_Data_without_Districts.xlsx')

file_clean=pd.read_excel('Cumulative_COVID_Data_without_Districts.xlsx')
file_clean.reset_index()

file_clean.drop('Unnamed: 0',axis=1,inplace=True)
file=file_clean


for_districts=list(np.array(file.columns))

#print(np.array(final['District']))

k=0
m=0
for i in file.columns:
    l=for_districts.index(i)
    for j in np.array(final['District']):
        if j==i:
            final.iloc[m,3]=file.iloc[k,l]
            #print(final.iloc[m,3])
            m=m+1
            k=k+1
            if k > 220:
                k = 0
            else:
                continue
            if m > 221*735:
                break



final.to_excel('Rearranged_Cumulative_COVID_Cases.xlsx')

