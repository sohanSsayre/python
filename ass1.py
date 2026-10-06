
# 1
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")

# 2

def word_frequency(sentence, word):
    words = sentence.split()
    count = 0
    for w in words:
        if w.lower() == word.lower():
            count += 1
    return count

sentence = input("Enter a sentence: ")
word = input("Enter a word to find its frequency: ")
print(f"The word '{word}' appears {word_frequency(sentence, word)} times in the sentence.")


# 3
def perform_arithmetic_operations(set1, set2):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set_1 = set1.difference(set2)
    difference_set_2 = set2.difference(set1)

    return union_set, intersection_set, difference_set_1, difference_set_2

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_result, intersection_result, diff1_result, diff2_result = perform_arithmetic_operations(set1, set2)
print(f"Union: {union_result}")
print(f"Intersection: {intersection_result}")
print(f"Difference (Set 1 - Set 2): {diff1_result}")
print(f"Difference (Set 2 - Set 1): {diff2_result}")


# 4
def concatenate_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = concatenate_lists(list1, list2)
print(f"Concatenated List: {concatenated_list}")


# 5
import pandas as pd

data = [
    ['John Doe', 'Savings', 5000],
    ['Jane Smith', 'Checking', 3000],
    ['Alice Johnson', 'Savings', 7000],
    ['Bob Brown', 'Checking', 2000],
    ['Charlie Davis', 'Savings', 6500],
    ['Diana Lee', 'Checking', 4000],
    ['Eve Wilson', 'Savings', 8500],
    ['Frank Clark', 'Checking', 3500],
    ['Grace Adams', 'Savings', 9000],
    ['Henry Kim', 'Checking', 1500]
]

df = pd.DataFrame(data, columns=['Name', 'Account Type', 'Balance'])
min_balance = df['Balance'].min()
max_balance = df['Balance'].max()

print(f"Minimum Balance: {min_balance}")
print(f"Maximum Balance: {max_balance}")


# 6
import pandas as pd

data = {
    'Roll': [1, 2, 3, 4, 5],
    'Name': ['Sohan', 'Jane', 'Alice', 'Bob', 'Charlie'],
    'Class': ['X', 'XI', 'XII', 'XIII', 'XIV'],
    'Fees': [5000, 6000, 7000, 8000, 9000]
}

df = pd.DataFrame(data)
print(df)

