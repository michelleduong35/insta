import json

#load follower file
with open('data/followers.json', 'r') as file:
    data = json.load(file)

#append followers into arr
followers = []
for item in data:
    followers.append(item['string_list_data'][0]['value'])

#load following file
with open('data/following.json', 'r') as file:
    data = json.load(file)

#append followers into arr
following = []
for item in data['relationships_following']:
    following.append(item['string_list_data'][0]['value'])
    
#followers that I don't follow back
result = []
for follower in followers:
  if follower not in following:
    result.append(follower)
print("followers that I don't follow back: ")
print(result)

#following that doesn't follow me
result = []
for follow in following:
  if follow not in followers:
    result.append(follow)
print("following that doesn't follow me: ")
print(result)