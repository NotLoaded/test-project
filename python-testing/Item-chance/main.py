import json

data = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        }
    ]
}


json_string1 = json.dumps(data)
json_string2 = json.dumps(data)
print(json_string1)
print(json_string2)

# Directly from dictionary
with open('json_data_1.json', 'w') as outfile:
    json.dump(json_string1, outfile)


# Using a JSON string
with open('json_data_2.json', 'w') as outfile:
    outfile.write(json_string2)