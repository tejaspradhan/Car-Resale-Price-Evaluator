
# coding: utf-8

# # Importing Machine Learning Libraries

# In[290]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[292]:


df = pd.read_excel('E:\Projects\Python Project\Car Resale Price Predictor\CRD.xlsx')


# In[293]:


df


# # Splitting the Data into Input and Output Features

# In[294]:


x = df[['Years','Running']]
y= df['Resale Price']


# In[295]:


x


# # Data Visualisation

# In[296]:


plt.scatter(df['Years'],df['Resale Price'])


# In[297]:


plt.scatter(df['Running'],df['Resale Price'])


# In[298]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.4, random_state=101)


# # Training the Model

# In[299]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x_train)
poly.fit(x_poly,y_train)
lm = LinearRegression()
lm.fit(poly.fit_transform(x_train),y_train)


# In[300]:


prediction = lm.predict(poly.fit_transform(x_test))


# In[301]:


plt.scatter(y_test,prediction)


# In[302]:


from sklearn import metrics
metrics.r2_score(y_test,prediction)*100

