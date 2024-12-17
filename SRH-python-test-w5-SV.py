# Big Data Programming: Pyhton Module Test
# Instructions ...
# Please consider good style & naming while developing the code when necessary,
#  such as Docstring, linting, etc. it is considered in the grading process!
# Use this file for the solution only. Jupyter notebook(.ipynb) not acceptable!
# Push the solution to a remote repo of name "SRH-Python-Test", and send me the link of the repo as DM
#  on Ms Teams for assessment.
# The duration of this test is 1 hour.

# Q1: What is the main difference between the list and Tuple?
# The key difference between tuples and lists is that while tuples are immutable objects, lists are mutable. This means tuples cannot be changed while lists can be modified.


# Q2: why should list indexing be used Python?
# An index allows us to quickly locate, and access data based on the indexed columns, without having to scan through the entire file. This can significantly speed up query 
# performance, especially for large files, by reducing the amount of data that needs to be searched and processed.


# Q3: You have two lists (string_list, values_list) below. Write a function of
#  a name count_car. The function returns a dictionary.
#  The expected return of the function should print out this dictionary:
#  {'Audi_Q5': 2, 'Honda_civic': 4, 'Mercedes_200E': 5, 'BMW_720': 7, 'VW_passat': 2}
string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]

#code - 
  def count_car(string_list, value_list):
    car_count = {}
    for car, value in zip(string_list, value_list):
        if car in car_count:
            car_count[car] += value
        else:
            car_count[car] = value
    return car_count

# Input lists
string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]

# Call the function
result = count_car(string_list, value_list)

# Print the result
print(result)


# Q4: Write a function of a name double_even_numbers. The function squares the
#  even numbers only. Also, the function leaves the first element of the input
#  as is without getting squared regardless being even or odd number.
#  The function has one argument which is a numpy array of 100 elements of
#  integer type between 0-10.
#  The function returns an array. Use list comprehension in your answer.

# code- 
import numpy as np

def double_even_numbers(arr):
    # Ensure input is valid
    if not isinstance(arr, np.ndarray) or len(arr) != 100 or arr.dtype != int:
        raise ValueError("Input must be a numpy array of 100 integer elements.")
    
    # List comprehension to square even numbers excluding the first element
    result = [arr[0]] + [x**2 if x % 2 == 0 else x for x in arr[1:]]
    
    # Convert back to numpy array and return
    return np.array(result)




# Q5: Read "movies.csv" file, a file is provided. Create a function
#  returns only table of elements before 2000 with score 7 and above, then save
#  the elements in a new csv file with a name "dest_csv". 

# Code -
import pandas as pd

def filter_and_save_elements(input_file):
    # Read the input file into a DataFrame
    
    df = pd.read_csv('movies.csv')

    # Filter rows: Year before 2000 and Score >= 7
    filtered_df = df[(df['Year'] < 2000) & (df['Score'] >= 7)]

    # Save the filtered DataFrame to a new CSV file
    output_file = "dest_csv.csv"
    filtered_df.to_csv(output_file, index=False)
    print(f"Filtered data has been saved to {output_file}.")





# Q6: Write a function of a name div_func. It returns the divsion of elements
#  in a list in reversed order. The function should pass the two lists below
#  without errors.

import random
random.seed(42)
short_list = [1, 0, 2, 2, 20]
long_list = [random.randrange(0, 10, 1) for i in range(15)]

# code -
import random

def div_func(list1, list2):
    result = []
    try:
        # Reverse both lists
        reversed_list1 = list1[::-1]
        reversed_list2 = list2[::-1]

        # Iterate through pairs of reversed elements
        for a, b in zip(reversed_list1, reversed_list2):
            try:
                # Perform division and append result
                result.append(a / b)
            except ZeroDivisionError:
                # Skip division by zero
                result.append(None) 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return result


