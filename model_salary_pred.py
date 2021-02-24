import numpy as np 			
import matplotlib.pyplot as plt		
import pandas as pd			
dataset = pd.read_csv(r'D:\data science\AMXWAM data science\class 16 & 17_oct 17, 2020\3. AMXWAM_ TASK\TASK-14\Salary_Data.csv')
X = dataset.iloc[:, :-1].values	
y = dataset.iloc[:,1].values    
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

import pickle
pickle.dump(regressor,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
