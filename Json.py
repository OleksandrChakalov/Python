import json

# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))

print(json.loads('"\\"foo\\bar"'))

# import json
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)