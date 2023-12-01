print("task1 in line1")
# import requests
# import json

# # 1.1: GET Request
# post_id = 1
# url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
# response = requests.get(url)
# if response.status_code in range(400, 600):
#     print(f"Error: {response.status_code}")
# else:
#     print(response.json())

# # 1.2: Create a class "ToDo"
# class ToDo:
#     def __init__(self, userId, id, title, completed):
#         self.userId = userId
#         self.id = id
#         self.title = title
#         self.completed = completed

# # 1.3: Create a new object of class ToDo
# new_todo = ToDo(1, 1, "Buy milk", False)

# # 1.4: POST Request
# url = "https://jsonplaceholder.typicode.com/todos"
# payload = {
#     "userId": new_todo.userId,
#     "title": new_todo.title,
#     "completed": new_todo.completed
# }
# response = requests.post(url, json=payload)
# if response.status_code in range(400, 600):
#     print(f"Error: {response.status_code}")
# else:
#     print(response.json())

# # 1.5: Edit some data of your attributes of your todo item
# new_todo.title = "Buy cheese"

# # 1.6: PUT Request
# chosen_id = 1
# url = f"https://jsonplaceholder.typicode.com/todos/{chosen_id}"
# payload = {
#     "userId": new_todo.userId,
#     "id": new_todo.id,
#     "title": new_todo.title,
#     "completed": new_todo.completed
# }
# response = requests.put(url, json=payload)
# if response.status_code in range(400, 600):
#     print(f"Error: {response.status_code}")
# else:
#     print(response.json())



print("task 2 in line 58")

# import requests
# import json
# import random
# from typing import List

# # 2.1 Random Character Request
# character_id = random.randint(1, 826)
# url = f"https://rickandmortyapi.com/api/character/{character_id}"
# response = requests.get(url)
# json_response = response.json()

# # 2.2 Response Output
# print(json.dumps(json_response, indent=4))

# # 2.3 Save to File
# with open(f"info_character_{character_id}.json", "w") as f:
#     json.dump(json_response, f, indent=4)

# # 2.4 Episode List
# episode_urls = json_response["episode"]
# episode_ids = [int(url.split("/")[-1]) for url in episode_urls]
# with open(f"all_episodes_with_character_{character_id}", "a") as f:
#     for url in episode_urls:
#         f.write(url + "\n")

# # 2.5 Episode Response Structure
# episode_id = 1
# url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
# response = requests.get(url)
# episode_json = response.json()
# print(json.dumps(episode_json, indent=4))

# # 2.6 Episode Class Creation
# class Episode:
#     def __init__(self, id: int, name: str, air_date: str, episode: str, characters: List[str], url: str, created: str):
#         self.id = id
#         self.name = name
#         self.air_date = air_date
#         self.episode = episode
#         self.characters = characters
#         self.url = url
#         self.created = created

# # 2.7 Episode Data Retrieval
# episodes = []
# for episode_id in episode_ids:
#     url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
#     response = requests.get(url)
#     episode_json = response.json()
#     episode = Episode(**episode_json)
#     episodes.append(episode)

# # 2.8 Class Methods
# class Episode:
#     def __init__(self, id: int, name: str, air_date: str, episode: str, characters: List[str], url: str, created: str):
#         self.id = id
#         self.name = name
#         self.air_date = air_date
#         self.episode = episode
#         self.characters = characters
#         self.url = url
#         self.created = created

#     def get_character_count(self):
#         return len(self.characters)

#     def get_character_names(self):
#         character_names = []
#         for character_url in self.characters:
#             response = requests.get(character_url)
#             character_json = response.json()
#             character_name = character_json["name"]
#             character_names.append(character_name)
#         return character_names

# # 2.9 Character Response Structure
# url = "https://rickandmortyapi.com/api/character/1"
# response = requests.get(url)
# character_json = response.json()
# print(json.dumps(character_json, indent=4))

# # 2.10 Character Class Creation
# class Character:
#     def __init__(self, id: int, name: str, status: str, species: str, type: str, gender: str, origin: dict, location: dict, image: str, episode: List[str], url: str, created: str):
#         self.id = id
#         self.name = name
#         self.status = status
#         self.species = species
#         self.type = type
#         self.gender = gender
#         self.origin = origin
#         self.location = location
#         self.image = image
#         self.episode = episode
#         self.url = url
#         self.created = created

# # 2.11 Character Object Creation
# url = f"https://rickandmortyapi.com/api/character/{character_id}"
# response = requests.get(url)
# character_json = response.json()
# random_character = Character(**character_json)

# # 2.12 Character Class Methods
# class Character:
#     def __init__(self, id: int, name: str, status: str, species: str, type: str, gender: str, origin: dict, location: dict, image: str, episode: List[str], url: str, created: str):
#         self.id = id
#         self.name = name
#         self.status = status
#         self.species = species
#         self.type = type
#         self.gender = gender
#         self.origin = origin
#         self.location = location
#         self.image = image
#         self.episode = episode
#         self.url = url
#         self.created = created

#     def get_episode_count(self):
#         return len(self.episode)

#     def get_episode_names(self):
#         episode_names = []
#         for episode_url in self.episode:
#             response = requests.get(episode_url)
#             episode_json = response.json()
#             episode_name = episode_json["name"]
#             episode_names.append(episode)
