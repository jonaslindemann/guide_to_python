import pandas as pd
import numpy as np

# Create a Series from a list - temperature readings
temperatures = pd.Series([22.5, 23.1, 24.8, 23.9, 22.2])
print("Basic temperature Series:")
print(temperatures)
print(f"Data type: {type(temperatures)}")
print()

# Series has two main components: values and index
print("Series components:")
print(f"Values: {temperatures.values}")
print(f"Values type: {type(temperatures.values)}")  # numpy array!
print(f"Index: {temperatures.index}")
print(f"Index type: {type(temperatures.index)}")
print()
