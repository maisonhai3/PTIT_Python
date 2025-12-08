# How to read a JSON file in Python

Reading a JSON file in Python is straightforward using the built-in `json` module.

## 1. Import the `json` module

```python
import json
```

## 2. Open the JSON file

Use the `open()` function to open the file. It's best practice to use a `with` statement to ensure the file is automatically closed.

```python
with open('your_file.json', 'r') as file:
    # 'r' means open for reading
```

## 3. Load the JSON data

Use the `json.load()` function to parse the JSON file into a Python dictionary or list.

```python
data = json.load(file)
```

## Complete Example

Here is a complete example. Assume you have a file named `data.json` with the content `{"name": "John Doe", "age": 30}`.

```python
import json

# Create a dummy data.json file for demonstration
with open('data.json', 'w') as f:
    json.dump({"name": "John Doe", "age": 30}, f)

# Read the data from data.json
with open('data.json', 'r') as f:
  data = json.load(f)

# You can now access the data as a dictionary
print(data['name'])  # Output: John Doe
print(data['age'])   # Output: 30
```

That's it! You have successfully read data from a JSON file.

