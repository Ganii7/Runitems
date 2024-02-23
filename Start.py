import json
jason = open('Aatrox.json')
build = open('build.json')


loadedbuild = json.load(build)
#print(loadedbuild)


loadedjason = json.load(jason)
    #print(loadedjason)
for i in loadedjason[0]["itemBuilds"][0]["blocks"]:
    print(i)
