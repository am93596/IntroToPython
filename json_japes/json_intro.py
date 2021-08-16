import json

first_pet = {
    "name": "Haggis",
    "animal": "Beagle"
}

# print(first_pet, type(first_pet))
#
# first_pet_string = json.dumps(first_pet)
#
# print(first_pet_string, type(first_pet_string))
#
# with open('first_pet_file.json', 'w') as jsonfile:
#     json.dump(first_pet, jsonfile)

with open("new_animal.json", "r") as jsonfile:
    lazy_thing = json.load(jsonfile)

print(lazy_thing, type(lazy_thing))
print(lazy_thing["sound_made"])
print(lazy_thing.get("sound_made"))

json_string = '{"name": "David", "age": 578}'
json_dict = json.loads(json_string)
print(json_dict, type(json_dict))
