import json

jason = open('Aatrox.json')
build = open('build.json')

loadedbuild = json.load(build)
loadedjason = json.load(jason)

numi = 0
numfinal = 0
objetosfinales = []

for items in loadedjason[0]["itemBuilds"][0]["blocks"]:
    numj = 0

    for item in items["items"]:
        # print(j)

        if numi <= 2:
            if numi == 2:
                # This line is duplicated because the third object has to be duplicated
                loadedbuild["blocks"][0]["items"].append(item)
                numfinal = 1
        elif numj == 0 or numi <= 4:
            numfinal = 1
        else:
            numfinal = 2

        if item["id"] not in objetosfinales:
            loadedbuild["blocks"][numfinal]["items"].append(item)
        objetosfinales.append(item["id"])
        numi += 1
        numj += 1


print(loadedbuild)
with open('build-1.json', 'w') as build:
    json.dump(loadedbuild, build, indent=4)
