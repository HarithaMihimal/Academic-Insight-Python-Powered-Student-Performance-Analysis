# -*- coding: utf-8 -*-
"""Performance Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/175bSnlNOCp6lO5jG11fwGdw4CGx2kIW2
"""



from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/drive/MyDrive/Academic Insight Python-Powered Student Performance Analysis/Expanded_data_with_more_features.csv')

df

df.describe()

df.info()

df.isnull().sum()

"""Drop the unnamed columns"""

df.drop('Unnamed: 0',axis=1)
print(df.head())

"""change weekly study hours column"""

df['WklyStudyHours'] = df['WklyStudyHours'].str.replace('05-oct','5-10')
df.head()

"""Gender Distribution"""

plt.figure(figsize=(8,6))
ax=sns.countplot(data=df,x='Gender')
ax.bar_label(ax.containers[0])
plt.title('Gender Distribution')
plt.show()

"""from the above chart we have analysed that, the number of females in the data is more than the number of males"""

df.columns

gp=df.groupby('ParentEduc').agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gp)

sns.heatmap(gp,annot=True)
plt.title('Parent Education vs Student Score')
plt.show()

gb1=df.groupby('ParentMaritalStatus').agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb1)

sns.heatmap(gb1,annot=True)
plt.title('Parent Marital Status vs Student Score')
plt.show()

sns.boxplot(data=df,x='MathScore')
plt.title('Test Math Score')
plt.show( )

sns.boxplot(data=df,x='ReadingScore')
plt.title('Test Reading Score')
plt.show( )

sns.boxplot(data=df,x='WritingScore')
plt.title('Test Writing Score')
plt.show( )

print(df['EthnicGroup'].unique())

"""Distribution of Ethnic Group"""

groupA=df.loc[(df['EthnicGroup']=='group A')].count()
groupB=df.loc[(df['EthnicGroup']=='group B')].count()
groupC=df.loc[(df['EthnicGroup']=='group C')].count()
groupD=df.loc[(df['EthnicGroup']=='group D')].count()
groupE=df.loc[(df['EthnicGroup']=='group E')].count()
# print(groupA)
plt.figure(figsize=(10,6))
plt.title('Ethnic Group Distribution')

mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
print(mlist)
plt.pie(mlist,labels=['group A','group B','group C','group D','group E'],autopct='%1.1f%%')
plt.show()

ax=sns.countplot(data=df,x="EthnicGroup")
ax.bar_label(ax.containers[0])
plt.title('Ethnic Group Distribution')
plt.show()

