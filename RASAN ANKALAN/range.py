import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("D:\\My Programming\\tox21trainingdata.sdf\\new_dataset_no_outliers.csv")

# Check the range of a specific column using describe()
column_name = 'toxicity_score'
column_range = df[column_name].describe()[['min', 'max']]

# Alternatively, you can access the min and max values directly
# column_range = {'min': df[column_name].min(), 'max': df[column_name].max()}

# Print the range
print('Range of', column_name)
print('Min:', column_range['min'])
print('Max:', column_range['max'])
