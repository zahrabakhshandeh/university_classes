import json
with open('file1.json', 'r') as file:
    data = json.load(file)

print(data)

python_dict = {
  "name": "Emily",
  "age": 35,
  "city": None
}

# Writing JSON data to a file
with open('data.json', 'w') as file:
    json.dump(python_dict, file, indent=4, sort_keys=True)
print("done")