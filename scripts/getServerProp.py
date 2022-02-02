import os
import json

prop_names = [ 
    'enable-command-block',
    'pvp',
    'difficulty',
    'max-players',
    'allow-flight',
    'view-distance',
    'server-port',
    'op-permission-level',
    'hide-online-players',
    'simulation-distance', 
    'hardcore',
    'spawn-monsters',
]

curr_props = {
    'a': '',
    'b': '',
    'c': '',
    'd': '',
    'e': '',
    'f': '',
    'g': '',
    'h': '',
    'i': '',
    'j': '', 
    'k': '',
    'l': ''
}

i = 97
for name in prop_names:
    query = "grep '^" + name + "'" + " /var/minecraft/server/server.properties"
    result = os.popen(query).read().rstrip().split('=')
    key = chr(i)
    curr_props[key] = result[1]
    i += 1


json_object = json.dumps(curr_props, indent = 4)
  
# Writing to sample.json
with open("curr_props.json", "w") as outfile:
    outfile.write(json_object)
