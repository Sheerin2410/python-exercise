import json

python_data = {'name' : 'django','subject':'python'}
print(type(python_data))
json_data = json.dumps(python_data)

print(json_data)
print(type(json_data))
