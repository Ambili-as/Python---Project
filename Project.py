#!/usr/bin/env python
# coding: utf-8

# ### Working with a dataset from ABC company, consisting of 458 rowsand 9 columns. The company requires a comprehensive report detailing information about their employees across various teams
# 

# In[23]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv(r"C:\Users\user\Downloads\myexcel - myexcel.csv.csv")
data


# In[8]:


data.isnull().sum()


# ##### Replacing null values

# In[14]:


x = data['Salary'].median()
data['Salary'].fillna(x,inplace = True)
data


# In[15]:


data.drop_duplicates(inplace = True)
data


# In[16]:


data.dropna ( inplace = True)
data


# In[17]:


data.isnull().sum()


# #### Preprocessing:
# ###### Correct the data in the "height" column by replacing it with random numbers between 150 and 180.Ensure data consistency and integrity before proceeding with analysis. 

# In[18]:


data['Height'] = np.random.uniform(150,180,size = len(data))
data


# #### Analysis Tasks:
# ###### Determine the distribution of employees across each team and calculate the percentage split relative to the total number of employees. 

# #### distribution of employees across each team
# 

# In[54]:


d=data['Team'].value_counts()
d


# #### percentage split relative to the total number of employees  

# In[53]:


p = data['Team'].value_counts()/len(data)*100
p


# #### Visualization

# In[62]:


sns.distplot(x=p)
plt.title("Percentage splits w.r.t the total no.of employees")
plt.show()


# #### Segregate employees based on their positions within the company.

# In[27]:


employees = data.groupby('Position')['Name'].apply(list)
for Position, Names in employees.items():
    print("Employees in position:",Position)
    for name in Names:
     print(name)
    print("\n")


# #### Visualization

# In[51]:


position_counts = data['Position'].value_counts()
position_counts.plot(kind='bar',color='lightcoral')
plt.title("Employee Distribution by Position")
plt.xlabel("Position")
plt.ylabel("Count of employees")
plt.show()


# ####  Identify the predominant age group among employees.

# In[25]:


data['Age Group'] = data['Age'].apply(lambda age:'20-25' if 20 <= age <= 25 else ('26-30' if 26 <= age <= 30 else ('31-35' if 31 <= age <= 35 else '36 and above')))

data


# In[28]:


data['Age Group'].value_counts()


# #### Visualization

# In[44]:


data['Age Group'].value_counts().plot(kind ='pie')
plt.title("Age group distribution")
plt.xlabel("Age group")
plt.ylabel("Count")
plt.show()


# ####  Discover which team and position have the highest salary expenditure.

# In[29]:


salary_exp = data.groupby(['Team','Position'])['Salary'].sum()
salary_exp.idxmax()


# #### Visualization

# In[37]:


sns.boxplot(x='Position',y='Salary',data=data)
plt.title("Salary Distribution by Position")
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


# ####  Investigate if there's any correlation between age and salary, and represent it visually

# In[30]:


correlation = data['Salary'].corr(data['Age'])
print("THE CORRELATION B/w Salary AND Age IS:",correlation)


# #### plotting the correlation

# In[31]:


sns.scatterplot(x="Age" ,y= "Salary",data= data)
plt.ylabel("Salary")
plt.xlabel("Age")
plt.title("correlation b/w Salary and Age")
plt.show()

