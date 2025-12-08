# How to use the `sorted()` function in Python

The `sorted()` function returns a new sorted list from the items in an iterable.

## Basic Syntax

```python
sorted(iterable, key=None, reverse=False)
```

-   `iterable`: A sequence (like a list, tuple, string) or collection (like a set, dictionary) to be sorted.
-   `key` (optional): A function to execute to decide the order. Default is `None` (compare the elements directly).
-   `reverse` (optional): A boolean. `False` will sort ascending, `True` will sort descending. Default is `False`.

## Simple Example

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# The original list is unchanged
print(numbers) # Output: [3, 1, 4, 1, 5, 9, 2, 6]
```

## Sorting a List of Dictionaries

When you have a list of dictionaries, you need to tell `sorted()` *what* to sort by. You do this using the `key` parameter. The `key` should be a function that takes a dictionary and returns the value to sort by. A `lambda` function is often used for this.

### Example from your code

In your `du_lieu_hoc_sinh.py` file, you calculate `diem_xet_tuyen` for each student. To sort the list of students based on this score, you can do the following:

```python
# ... (your existing code to calculate diem_xet_tuyen) ...

# Sort the list of students by 'diem_xet_tuyen' in descending order
sorted_data = sorted(data, key=lambda thi_sinh: thi_sinh['diem_xet_tuyen'], reverse=True)

# print the sorted data
print(sorted_data)
```

### Explanation:

1.  `key=lambda thi_sinh: thi_sinh['diem_xet_tuyen']`: This tells `sorted()` to look at each element (`thi_sinh`) in the `data` list and use the value of the `'diem_xet_tuyen'` key for comparison.
2.  `reverse=True`: This sorts the list from the highest score to the lowest.
3.  `sorted_data = ...`: `sorted()` **returns a new sorted list**. It does not modify the original `data` list. You need to assign the result to a new variable (or back to `data` itself if you want to replace it).

Your line `sorted(data)` in `du_lieu_hoc_sinh.py` doesn't do anything because it doesn't specify a key for sorting the dictionaries, and its result is not stored.

