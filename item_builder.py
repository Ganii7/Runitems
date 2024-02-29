import json


def add_item(item, final_objects, loaded_build, block_index):
    if item["id"] not in final_objects:
        loaded_build["blocks"][block_index]["items"].append(item)
        final_objects.add(item["id"])
    return final_objects, loaded_build


def process_json_files(champ, lane, build_file):
    champ = "champions/" + champ + ".json"
    with open(champ) as champion, open(build_file) as build:
        loaded_build = json.load(build)
        loaded_champion = json.load(champion)
        final_objects = set()
        alternative_items = []
        laneid = 0
        
        # for block in loaded_build["blocks"]:
        #     block["items"].clear()
        
        # sort the line and saving the apropiated id
        for i, mylane in enumerate(loaded_champion):
            if mylane["position"] == lane:
                laneid = i

        # sort the items and descarting the repited ones
        for i, items in enumerate(loaded_champion[laneid]["itemBuilds"][0]["blocks"]):
            for x, item in enumerate(items["items"]):
                if i == 1 or (i >= 1 and x == 0):
                    final_objects, loaded_build = add_item(
                        item, final_objects, loaded_build, 1
                    )
                    # Boots exception
                    if x == 0 and i == 1:
                        loaded_build["blocks"][0]["items"].append(item)
                elif i == 0:
                    final_objects, loaded_build = add_item(
                        item, final_objects, loaded_build, 0
                    )
                else:
                    alternative_items.append(item)

        # add alternative items to the build if there is repited ones or at the end
        for alternative_item in alternative_items:
            if len(loaded_build["blocks"][1]["items"]) < 6:
                final_objects, loaded_build = add_item(
                    alternative_item, final_objects, loaded_build, 1
                )
            else:
                final_objects, loaded_build = add_item(
                    alternative_item, final_objects, loaded_build, 2
                )

    return loaded_build


def write_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    modified_build = process_json_files("Aatrox", "top", "build.json")
    write_to_file(modified_build, "build-1.json")
