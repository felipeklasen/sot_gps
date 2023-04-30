# Turn the content from island_coords.txt into a json file named "islands.json"
# The content from the file follows the following pattern
# Sanctuary Outpost : F7
# The json file should follow the following pattern
# {
#     "Name" : "Sanctuary Outpost",
#     "Coords" : "F7"
# }


import json

island_coords = {}

with open('island_coords.txt') as f:
    for line in f:
        name, coord = line.strip().split(':')
        url = f'island_images/{name.strip()}.png'
        # Insert the name and coord and image url into the dictionary as a dict object with the name as the key
        island_coords[name.strip()] = {"Name": name.strip(), "Coords": coord.strip(), "Image": url}

with open('islands.json', 'w') as f:
    json.dump(island_coords, f)

