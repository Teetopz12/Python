#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd


# In[2]:


cd downloads


# In[5]:


data = pd.read_csv('C:/Users/WALKER/Desktop/Python_ws/diabetes.csv')


# In[7]:


data.head()


# In[8]:


data.columns


# In[9]:


data.info()


# In[10]:


data.describe()


# In[11]:


data.describe().T


# In[13]:


data.isnull()


# In[14]:


data.isnull().sum()


# In[26]:


data_copy = data.copy
data_copy=data_copy(deep= True)


# In[25]:


print(data_copy.isnull().sum())


# In[30]:


data.hist(figsize=(17, 14))
plt.show()


# In[31]:


p= data_copy.hist(figsize=(20,20))


# In[47]:


import seaborn as sns

# Assuming you have a DataFrame named 'df_diabetes' and want to create a bar plot for it
p = sns.barplot(data=data_copy)


# In[52]:


color_wheel = {1: "#0392cf", 2: "#7bc043"}
colors = data["Outcome"].map(lambda x: color_wheel.get(x + 1))
print(data.Outcome.value_counts())
p = data.Outcome.value_counts().plot(kind="bar")


# In[55]:


from pandas.plotting import scatter_matrix

# Assuming you have a DataFrame named 'data'
scatter_matrix(data, figsize=(20, 20))


# In[ ]:


sns.pairplot(data, hue='Outcome')
plt.show()


# In[62]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 10))
p = sns.heatmap(data.corr(), annot=True, cmap="RdYlGn")


# In[68]:


fig, ax = plt.subplots(1, 2, figsize=(20, 7))
sns.countplot(data=data_copy, x="Outcome", ax=ax[0])
data["Outcome"].value_counts().plot.pie(explode=[0, 0.1], autopct="%1.1f%%", labels=["No", "Yes"], shadow=True, ax=ax[1])
plt.show()


# In[ ]:




