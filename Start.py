import json

jason = open('Aatrox.json')
build = open('build.json')

loadedbuild = json.load(build)
loadedjason = json.load(jason)

for i in loadedjason[0]["itemBuilds"][0]["blocks"]:
    for j in i["items"]:
        # print(j)
        loadedbuild["blocks"][0]["items"].append(j)



print(loadedbuild)
with open('build-1.json', 'w') as build:
    json.dump(loadedbuild, build, indent=4)
