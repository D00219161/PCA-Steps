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
data.head()  
data.describe()

# I will drop the Size column as it is not numerical 
data.drop('Size', axis=1, inplace=True)
data.info()

# Missing Values - Check for any missing values here. 
# Just to make sure I have no missing values within my dataset
data.isnull().sum()

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
# Checking to see if each column of data has the same number of values.
data.info()
# Describes the data after null values dropped
data.describe()

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

# Step 4 - Calculate the eigenvectors and eigenvalues of the covariance matrix
eigenValues, eigenVectors = np.linalg.eig(covarianceMatrix)
print("EigenValues :", eigenValues, "EigenVectors :", eigenVectors)

# Step 5 - Choosing components and forming a feature vector
# Order the eigenVectores by eigenValue, highest to lowest
idx = eigenValues.argsort()[::-1]   
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
print("EigenValues :", eigenValues, "EigenVectors :", eigenVectors)

# Create a new featureVector - eigenVectores wish to keep from list of eigenvectors,
# and form a matrix
featureVector = eigenVectors
print(featureVector)

# Step 6 - Deriving the new data set
# New DataFrame Created in Step 2 when Mean Values Substracted From Original Values
updatedData = pd.DataFrame({"Updated Weight":updatedWeight, "Updated Age":updatedAge, "Updated Height":updatedHeight})
print(updatedData)

# Use the covarianceMatrix of the updatedData to then be transposed for the rowDataAdjust
print(covarianceMatrix)

# The featureVector Transposed and stored in rowFeatureVector
rowFeatureVector = np.transpose(featureVector) 
print(rowFeatureVector)

# The covarianceMatrix of the updatedData Transposed and stored in rowDataAdjust
rowDataAdjust = np.transpose(covarianceMatrix)
print(rowDataAdjust)

# The updatedData Transposed and stored in rowDataUpdatedTransposed
rowDataUpdatedTransposed = np.transpose(updatedData)
print(rowDataUpdatedTransposed)

# The finalData is equal to the rowFeatureVector (featureVector of eigenVectors) 
# multiplied by the rowDataAdjust (covarianceMatrix of my updatedData 
# (Means substracted from original data)) 
finalData = rowFeatureVector * rowDataAdjust
print(finalData)

# Final Data Updated using Mean DataSet
finalData = np.dot(rowFeatureVector, rowDataUpdatedTransposed)
print(finalData)

# Step 7 - Getting the old data back
finalData = rowFeatureVector * rowDataAdjust
print(finalData)

rowDataAdjust = rowFeatureVector-1 * finalData
print(rowDataAdjust)

rowDataAdjust = np.transpose(rowFeatureVector) * finalData
print(rowDataAdjust)

rowOriginalData = (np.transpose(rowFeatureVector) * finalData) + updatedData
print(rowOriginalData) 
 
 
 
 
 
 
 
 
 
 
 
 
 