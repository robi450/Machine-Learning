import numpy as np
from lab_utils_multi import load_house_data, run_gradient_descent 
from lab_utils_multi import norm_plot, plt_equal_scale, plot_cost_i_w
from lab_utils_common import dlc

import matplotlib.pyplot as plt

np.set_printoptions(precision=2)
plt.style.use('./deeplearning.mplstyle')

"""Notation:
General
Notation	Description	Python (if applicable)
𝑎
 	scalar, non bold	
𝐚
 	vector, bold	
𝐀
 	matrix, bold capital	
Regression		
𝐗
 	training example maxtrix	X_train
𝐲
 	training example targets	y_train
𝐱(𝑖)
 ,  𝑦(𝑖)
 	 𝑖𝑡ℎ
 Training Example	X[i], y[i]
m	number of training examples	m
n	number of features in each example	n
𝐰
 	parameter: weight,	w
𝑏
 	parameter: bias	b
𝑓𝐰,𝑏(𝐱(𝑖))
 	The result of the model evaluation at  𝐱(𝑖)
  parameterized by  𝐰,𝑏
 :  𝑓𝐰,𝑏(𝐱(𝑖))=𝐰⋅𝐱(𝑖)+𝑏
 	f_wb
∂𝐽(𝐰,𝑏)∂𝑤𝑗
 	the gradient or partial derivative of cost with respect to a parameter  𝑤𝑗
 	dj_dw[j]
∂𝐽(𝐰,𝑏)∂𝑏
 	the gradient or partial derivative of cost with respect to a parameter  𝑏
 	dj_db"""

"""Problem Statement
As in the previous labs, you will use the motivating example of housing price prediction. The training data set contains many examples with 4 features (size, bedrooms, floors and age) shown in the table below. Note, in this lab, the Size feature is in sqft while earlier labs utilized 1000 sqft. This data set is larger than the previous lab.

We would like to build a linear regression model using these values so we can then predict the price for other houses - say, a house with 1200 sqft, 3 bedrooms, 1 floor, 40 years old.

Dataset:
Size (sqft)	Number of Bedrooms	Number of floors	Age of Home	Price (1000s dollars)
952	2	1	65	271.5
1244	3	2	64	232
1947	3	2	17	509.8
...	...	...	...	...
"""
# Load the data set
X_train, y_train = load_house_data()
X_features = ['Size(sqft)', 'Bedrooms', 'Floors', 'Age']

# Let's view the data set and its features by plotting each feature versus price.

fig,ax=plt.subplots(1, 4, figsize=(12,3), sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:,i], y_train)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel('Price (1000s $)')
plt.show()
