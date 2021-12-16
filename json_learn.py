import json
from io import StringIO
import decimal


# ENCODING JSON

# json.dump()


# json module in Python module provides a method called dump() which converts the Python objects
#  into appropriate json objects. It is a slight variant of dumps() method.


# python object(dictionary) to be dumped
dict1 = {
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
                "age": "34",
                "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
                "age": "24",
                "salary": "40000"
    },
}

# the json file where the output must be stored
out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent=6)

out_file.close()

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])


# print(json.__file__)
print(json.dumps("\"foo\bar"))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))


io = StringIO()
# print(io)
json.dump(['streaming API'], io)
print(io.getvalue())


# Pretty printing:


print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))


# python object(dictionary) to be dumped
dict1 = {
    ('addresss', 'street'): 'Brigade road',
}

# the json file where the output must be stored
out_file1 = open("myfile1.json", "w")

json.dump(dict1,  out_file1, indent=6, skipkeys=True)

out_file.close()


# dictionary to be dumped
d = {'lang': '??? ????'}

with open('myfile2.json', 'w', encoding='utf8') as json_file:
    json.dump(d, json_file, ensure_ascii=False)


# Allow nan


# dictionary to be dumped
d = {
    'a': 1,
    'x': float('nan')
}

with open('myfile3.json', 'w', encoding='utf8') as json_file:
    json.dump(d, json_file, allow_nan=True)


# json.dumps() function converts a Python object into a json string.


# Creating a dictionary
Dictionary = {1: 'Welcome', 2: 'to',
              3: 'Geeks', 4: 'for',
              5: 'Geeks'}

# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary)
print('Equivalent json string of input dictionary:',
      json_string)
print("	 ")

# Checking type of object
# returned by json.dumps
print(type(json_string))


Dictionary = {(1, 2, 3): 'Welcome', 2: 'to',
              3: 'Geeks', 4: 'for',
              5: 'Geeks'}


# Our dictionary contains tuple
# as key, so it is automatically
# skipped If we have not set
# skipkeys = True then the code
# throws the error
json_string = json.dumps(Dictionary,
                         skipkeys=True)

print('Equivalent json string of dictionary:',
      json_string)


Dictionary = {(1, 2, 3): 'Welcome', 2: 'to',
              3: 'Geeks', 4: 'for',
              5: 'Geeks', 6: float('nan')}

# If specified, separators should be
# an (item_separator, key_separator)tuple
# Items are separated by '.' and key,
# values are separated by '='
json_string = json.dumps(Dictionary,
                         skipkeys=True,
                         allow_nan=True,
                         indent=6,
                         separators=(". ", " = "))

print('Equivalent json string of dictionary:',
      json_string)


# DECODING JSON


json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
# ['foo', {'bar': ['baz', None, 1.0, 2]}]
json.loads('"\\"foo\\bar"')
# '"foo\x08ar'

io = StringIO('["streaming API"]')
json.load(io)
# ['streaming API']

# Specializing JSON object decoding:


def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


print(json.loads('{"__complex__": true, "real": 1, "imag": 2}',
                 object_hook=as_complex))


print(json.loads('1.1', parse_float=decimal.Decimal))

# Extending JsonEncoder


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


print(json.dumps(2 + 1j, cls=ComplexEncoder))

print(ComplexEncoder().encode(2 + 1j))

print(list(ComplexEncoder().iterencode(2 + 1j)))

# Python program to read
# json file


# Opening JSON file
f = open('data.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
# print(data["emp1"]["name"])

# Extracting all names from a dictionary
for k , v in data.items():
    print(v["name"])
    # for k1 in dic["name"]:
    #     print(k1)


# # Closing file
f.close()

# json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary


# JSON string:
# Multi-line string
x = """{
	"Name": "Jennifer Smith",
	"Contact Number": 7867567898,
	"Email": "jen123@gmail.com",
	"Hobbies":["Reading", "Sketching", "Horse Riding"]
	}"""

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)

	
# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
	
# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
	
print(employee_dict['name'])

