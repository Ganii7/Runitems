import json


def read_build_json(champion):
    jason = open(champion)
    build = open('build.json')
    loadedbuild = json.load(build)
    loadedjason = json.load(jason)
    objetosfinales = []
    objetosrepetidos = []
    switch = True

    def write_item(item,numfinal):
        loadedbuild["blocks"][numfinal]["items"].append(item)
    
    
    
    for i,items in enumerate(loadedjason[0]["itemBuilds"][0]["blocks"]):
        for j,item in enumerate(items["items"]):
            # print(j)

            if i == 0:
                numfinal = 0
            elif i ==1 and j ==0:
                write_item(item,0)
                numfinal= 1
            elif i == 1:
                numfinal = 1
                objetosrepetidos.append(item["id"])
            elif i> 1 and item["id"] not in objetosrepetidos:
                if j == 0:
                    numfinal = 1
                    objetosrepetidos.append(item["id"])
                    switch = True
                elif item["id"] not in objetosrepetidos:
                    objetosfinales.append(item)
                    objetosrepetidos.append(item["id"])
                    switch = False
            if switch:
                write_item(item,numfinal)
    while len(loadedbuild["blocks"][1]["items"]) <= 5:
        write_item(objetosfinales[0],1)
        del objetosfinales[0]
    write_item(objetosfinales,2)
                
                
    return loadedbuild

def write_to_file(archivo,contenido):
    with open(archivo, 'w') as build:
        json.dump(contenido, build, indent=4)
    
if __name__ == "__main__":
    write_to_file("build-1.json",read_build_json('Aatrox.json'))