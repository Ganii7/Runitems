import json

objetosfinales = set()
loadedbuild = {}

with open('Aatrox.json') as jason, open('build.json') as build:
    loadedbuild = json.load(build)
    loadedjason = json.load(jason)

    for i, items in enumerate(loadedjason[0]["itemBuilds"][0]["blocks"]):
        for item in items["items"]:
            numfinal = 1 if i <= 2 or i <= 4 else 2

            if i == 2 or item["id"] not in objetosfinales:
                loadedbuild["blocks"][numfinal]["items"].append(item)
            objetosfinales.add(item["id"])

# print(loadedbuild)

with open('build-1.json', 'w') as build:
    json.dump(loadedbuild, build, indent=4)
