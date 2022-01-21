""" Created on Fri Nov 12 11:39:10 2021 @author: Roisin McPhillips D00219161"""
# Assignment 4 PCA - Dataset fround from Kraggle at this link 
# https://www.kaggle.com/tourist55/clothessizeprediction by Sarvesh Dubey

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

# PCA Steps
# Step 1 - Get some data, clean it and display it out
# Import the Excel csv file from File Location & Read in
import os
cwd = os.getcwd()
print(cwd)
os.chdir('C:/Users/roisi/OneDrive/Desktop/Computing Years/Computing Year 4/Data Analysis & Visualisation (Sems 1)/Continuous Assessments - Exercises\Assignment 4 Roisin McPhillips')
data= pd.read_csv("Original_Data_Set.csv")

# Describes the data information from the imported csv file
print("Data Types") 
data.info()
 # 0   Weight  119734 non-null  int64  
 # 1   Age     119477 non-null  float64
 # 2   Height  119404 non-null  float64
 # 3   Size    119734 non-null  object 

data.head()  
#    Weight   Age  Height Size
# 0      62  28.0  172.72   XL
# 1      59  36.0  167.64    L
# 2      61  34.0  165.10    M
# 3      65  27.0  175.26    L
# 4      62  45.0  172.72    M

data.describe()
#               Weight            Age         Height
# count  119734.000000  119477.000000  119404.000000
# mean       61.756811      34.027311     165.805794
# std         9.944863       8.149447       6.737651
# min        22.000000       0.000000     137.160000
# 25%        55.000000      29.000000     160.020000
# 50%        61.000000      32.000000     165.100000
# 75%        67.000000      37.000000     170.180000
# max       136.000000     117.000000     193.040000

# I will drop the Size column as it is not numerical 
data.drop('Size', axis=1, inplace=True)
data.info()
 # 0   Weight  119734 non-null  int64  
 # 1   Age     119477 non-null  float64
 # 2   Height  119404 non-null  float64

# Missing Values - Check for any missing values here. 
# Just to make sure I have no missing values within my dataset
data.isnull().sum()
# Weight      0 - No missing values
# Age       257 - 257 missing values
# Height    330 - 330 missing values

# I found the mode of the age value
age_mode = data.Age.mode()[0]
print(age_mode)
# 30.0 - this is the mode

# I found the mode of the height value
height_mode = data.Height.mode()[0]
print(height_mode)
# 162.56 - this is the mode

# As my dataset contains over 10000 lines of data, I will drop the customers 
# with the missing values to ensure the data stays honest. 
# Remove the age null values from the dataset
data = data.drop(data[data.Age.isnull()].index)
data.isnull().sum()
# Remove the height null values from the dataset
data = data.drop(data[data.Height.isnull()].index)
data.isnull().sum()
# Check my dataset again for any missing values to make sure all have been dropped
data.isnull().sum()
# Weight    0 - No missing values
# Age       0 - No missing values
# Height    0 - No missing values

# Checking to see if each column of data has the same number of values.
data.info()
 # 0   Weight  119153 non-null  int64  
 # 1   Age     119153 non-null  float64
 # 2   Height  119153 non-null  float64
 
 # Describes the data after null values dropped
data.describe()
#               Weight            Age         Height
# count  119153.000000  119153.000000  119153.000000
# mean       61.756095      34.032714     165.807068
# std         9.942877       8.148302       6.737797
# min        22.000000       0.000000     137.160000
# 25%        55.000000      29.000000     160.020000
# 50%        61.000000      32.000000     165.100000
# 75%        67.000000      37.000000     170.180000
# max       136.000000     117.000000     193.040000 

# Step 2 - Subtract the mean
# Find the mean of the weight column
meanWeight = data.mean().Weight
print("Weight mean = ", meanWeight)
# Weight mean =  61.756095104613394

# Substract the weight mean from each weight
print("Weight Values", data.Weight)
print("Weight Mean Value", meanWeight)
print ("The value after subraction of mean")
updatedWeight = data.Weight - data.mean().Weight
print(updatedWeight)

# Assign Data to table 
dataWeight = {'Weight Values':data.Weight,'Mean Weight Values':data.Weight - data.mean().Weight}
# Creates pandas DataFrame.  
dfWeight = pd.DataFrame(dataWeight)  
# Print the data  
print(dfWeight)  

# Find the mean of the age column
meanAge = data.mean().Age
print("Age mean = ", meanAge)
# Age mean =  34.03271424135355

# Substract the age mean from each age
print("Age Values", data.Age)
print("Age Mean Value", meanAge)
print ("The value after subraction of mean")
updatedAge = data.Age - data.mean().Age
print(updatedAge)

# Assign Data to table
dataAge = {'Age Values':data.Age, 'Mean Age Values':data.Age - data.mean().Age}
# Creates pandas DataFrame.  
dfAge = pd.DataFrame(dataAge)  
# Print the data  
print(dfAge)  

# Find the mean of the height column
meanHeight = data.mean().Height
print("Height mean = ", meanHeight)
# Height mean =  165.8070678875258

# Substract the height mean from each height
print("Height Values", data.Height)
print("Height Mean Value", meanHeight)
print ("The value after subraction of mean")
updatedHeight = data.Height - data.mean().Height
print(updatedHeight)

# Assign Data to table 
dataHeight = {'Height Values':data.Height,'Mean Height Values':data.Height - data.mean().Height}
# Creates pandas DataFrame.  
dfHeight = pd.DataFrame(dataHeight)  
# Print the data  
print(dfHeight)  

# Create a new DataFrame for the new values now once the mean has been substracted
# New DataFrame is called updatedData 
updatedData = pd.DataFrame({"Updated Weight":updatedWeight, "Updated Age":updatedAge, "Updated Height":updatedHeight})
print(updatedData)

# Scatter Plot of Original Data Values
figure(num=None, figsize=(20, 18), dpi=80, facecolor='w', edgecolor='k')
sns.scatterplot(data.Weight, data.Age, data.Height)
plt.show()
# Produce scatter and correlation plots of Original Data Values
figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
sns.pairplot(data)
plt.show()

# Scatter Plot of Updated Data Values
figure(num=None, figsize=(20, 18), dpi=80, facecolor='w', edgecolor='k')
sns.scatterplot(updatedWeight, updatedAge, updatedHeight)
plt.show()
# Produce scatter and correlation plots of Updated Data Values
figure(num=None, figsize=(20, 18), dpi=80, facecolor='w', edgecolor='k')
sns.pairplot(updatedData)
plt.show()

# Step 3 - Calculate the covariance matrix 
# of the now updated Data Values - New DataFrame = updatedData as created in step 2
covarianceMatrix = updatedData.cov()
print(covarianceMatrix)
#                 Updated Weight  Updated Age  Updated Height
# Updated Weight       98.860797     5.521919       26.030227
# Updated Age           5.521919    66.394827       -0.167130
# Updated Height       26.030227    -0.167130       45.397907

# Step 4 - Calculate the eigenvectors and eigenvalues of the covariance matrix
eigenValues, eigenVectors = np.linalg.eig(covarianceMatrix)
print("EigenValues :", eigenValues, "EigenVectors :", eigenVectors)
# EigenValues : [110.02676389  34.65894753  65.96781927] 
# EigenVectors : [[ 0.92151693  0.38002476  0.07992323]
#                 [ 0.11520371 -0.07097964 -0.9908027 ]
#                 [ 0.37085664 -0.92224892  0.1091892 ]]

# Step 5 - Choosing components and forming a feature vector
# Order the eigenVectores by eigenValue, highest to lowest
idx = eigenValues.argsort()[::-1]   
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
print("EigenValues :", eigenValues, "EigenVectors :", eigenVectors)
# EigenValues : [110.02676389  65.96781927  34.65894753] 
# EigenVectors : [[ 0.92151693  0.07992323  0.38002476]
#                 [ 0.11520371 -0.9908027  -0.07097964]
#                 [ 0.37085664  0.1091892  -0.92224892]]

# Create a new featureVector - eigenVectores wish to keep from list of eigenvectors,
# and form a matrix
featureVector = eigenVectors
print(featureVector)
# [[ 0.92151693  0.07992323  0.38002476]
#  [ 0.11520371 -0.9908027  -0.07097964]
#  [ 0.37085664  0.1091892  -0.92224892]]

# Step 6 - Deriving the new data set
# New DataFrame Created in Step 2 when Mean Values Substracted From Original Values
updatedData = pd.DataFrame({"Updated Weight":updatedWeight, "Updated Age":updatedAge, "Updated Height":updatedHeight})
print(updatedData)
#         Updated Weight  Updated Age  Updated Height
# ID                                                 
# 1             0.243905    -6.032714        6.912932
# 2            -2.756095     1.967286        1.832932
# 3            -0.756095    -0.032714       -0.707068
# 4             3.243905    -7.032714        9.452932
# 5             0.243905    10.967286        6.912932
#                ...          ...             ...
# 119730        1.243905     7.967286        9.452932
# 119731      -16.756095    -5.032714      -10.867068
# 119732       -0.756095    -3.032714        6.912932
# 119733       12.243905    -3.032714        1.832932
# 119734        8.243905    -4.032714        1.832932
# [119153 rows x 3 columns]

# Use the covarianceMatrix of the updatedData to then be transposed for the rowDataAdjust
print(covarianceMatrix)
#                 Updated Weight  Updated Age  Updated Height
# Updated Weight       98.860797     5.521919       26.030227
# Updated Age           5.521919    66.394827       -0.167130
# Updated Height       26.030227    -0.167130       45.397907

# The featureVector Transposed and stored in rowFeatureVector
rowFeatureVector = np.transpose(featureVector) 
print(rowFeatureVector)
# [[ 0.92151693  0.11520371  0.37085664]
#  [ 0.07992323 -0.9908027   0.1091892 ]
#  [ 0.38002476 -0.07097964 -0.92224892]]

# The covarianceMatrix of the updatedData Transposed and stored in rowDataAdjust
rowDataAdjust = np.transpose(covarianceMatrix)
print(rowDataAdjust)
#                 Updated Weight  Updated Age  Updated Height
# Updated Weight       98.860797     5.521919       26.030227
# Updated Age           5.521919    66.394827       -0.167130
# Updated Height       26.030227    -0.167130       45.397907

# The updatedData Transposed and stored in rowDataUpdatedTransposed
rowDataUpdatedTransposed = np.transpose(updatedData)
print(rowDataUpdatedTransposed)
# ID                1         2         3       ...    119732     119733    119734
# Updated Weight  0.243905 -2.756095 -0.756095  ... -0.756095  12.243905  8.243905
# Updated Age    -6.032714  1.967286 -0.032714  ... -3.032714  -3.032714 -4.032714
# Updated Height  6.912932  1.832932 -0.707068  ...  6.912932   1.832932  1.832932
# [3 rows x 119153 columns]

# The finalData is equal to the rowFeatureVector (featureVector of eigenVectors) 
# multiplied by the rowDataAdjust (covarianceMatrix of my updatedData 
# (Means substracted from original data)) 
finalData = rowFeatureVector * rowDataAdjust
print(finalData)
#                 Updated Weight  Updated Age  Updated Height
# Updated Weight       91.101898     0.636146        9.653482
# Updated Age           0.441330   -65.784174       -0.018249
# Updated Height        9.892131     0.011863      -41.868170

# Final Data Updated using Mean DataSet
finalData = np.dot(rowFeatureVector, rowDataUpdatedTransposed)
print(finalData)
# [[ 2.09347818 -1.63339465 -0.96274406 ...  1.51757238 11.6133408
#    7.81206935]
#  [ 6.7515408  -1.96933166 -0.10522038 ...  3.69920946  4.18353027
#    4.85464006]
#  [-5.85455439 -2.87744128  0.36707978 ... -6.44751807  3.17782833
#    1.72870893]]

# Step 7 - Getting the old data back
finalData = rowFeatureVector * rowDataAdjust
print(finalData)
#              Updated Weight  Updated Age  Updated Height
# Updated Weight       91.101898     0.636146        9.653482
# Updated Age           0.441330   -65.784174       -0.018249
# Updated Height        9.892131     0.011863      -41.868170

rowDataAdjust = rowFeatureVector-1 * finalData
print(rowDataAdjust)
#                 Updated Weight  Updated Age  Updated Height
# Updated Weight      -90.180381    -0.520942       -9.282626
# Updated Age          -0.361406    64.793372        0.127438
# Updated Height       -9.512106    -0.082842       40.945922

rowDataAdjust = np.transpose(rowFeatureVector) * finalData
print(rowDataAdjust)
#                 Updated Weight  Updated Age  Updated Height
# Updated Weight       83.951942     0.050843        3.668562
# Updated Age           0.050843    65.179138        0.001295
# Updated Height        3.668562     0.001295       38.612875

rowOriginalData = (np.transpose(rowFeatureVector) * finalData) + updatedData
print(rowOriginalData) 
 
 
 
 
 
 
 
 
 
 
 
 
 