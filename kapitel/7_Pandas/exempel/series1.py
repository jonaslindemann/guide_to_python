import pandas as pd

data = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(data) 

print(data.dtype)  # Check the data type of the Series
print(data.index)  # Check the index of the Series
print(data.values)  # Check the values of the Series

# Accessing elements
print(data['a'])  # Access by index label
print(data[0])    # Access by position
print(data[['a', 'c']])  # Access multiple elements by index labels
# Conditional selection
print(data[data > 20])  # Select elements greater than 20
# Check if an index label exists
print(30 in data.values)  # Skriver ut True om 30 finns i serien
print(50 in data.values)  # Skriver ut False om 50 inte finns i serien
print('a' in data.index)  # Skriver ut True om 'a' finns i indexet
print('e' in data.index)  # Skriver ut False om 'e' inte finns i indexet
#print('b' in data)
# Convert Series to a NumPy array
array_data = data.to_numpy()
print(array_data)  # Display the NumPy array
# Convert Series to a list
list_data = data.tolist()
print(list_data)  # Display the list
# Convert Series to a dictionary
dict_data = data.to_dict()
print(dict_data)  # Display the dictionary
