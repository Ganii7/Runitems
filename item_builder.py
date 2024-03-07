import json
import os
from utils.file_updater import *


def add_item(item, final_objects, loaded_build, block_index):
    """
    Adds an item to the final_objects and loaded_build if the item's id is not already present in final_objects. 
    Parameters:
    - item: the item to be added
    - final_objects: a set of the final objects
    - loaded_build: the loaded build object
    - block_index: the index of the block in loaded_build
    Returns:
    - final_objects: the updated set of final objects
    - loaded_build: the updated loaded build object
    """
    if item["id"] not in final_objects:
        loaded_build["blocks"][block_index]["items"].append(item)
        final_objects.add(item["id"])
    return final_objects, loaded_build


def process_json_files(champion, build_file):
    """
    Processes the JSON files for a given champion and lane to generate a final build.
    Args:
    champion (str): The name of the champion.
    lane (str): The lane of the champion.
    build_file (str): The file path of the build file.
    Returns:
    dict: The final build for the champion in the specified lane.
    """

    # Load champion and build files
    with open(f"champions/{champion}") as champion_file, open(build_file) as build:
        loaded_build = json.load(build)
        loaded_champion = json.load(champion_file)
        final_objects = set()
        alternative_items = []

        # Find the lane ID for the given lane
        laneid = 0

        # sort the items and descarting the repited ones
        for i, items in enumerate(loaded_champion[laneid]["itemBuilds"][0]["blocks"]):
            try:
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
            except TypeError:
                pass

        # Add alternative items to the build if there are repeated ones or at the end
        for alternative_item in alternative_items:
            block_index = 1 if len(
                loaded_build["blocks"][1]["items"]) < 6 else 2
            final_objects, loaded_build = add_item(
                alternative_item, final_objects, loaded_build, block_index)
        # Update associated champions and uid
        loaded_build["associatedChampions"].append(loaded_champion[0]["id"])
    loaded_build["title"] = "RunitemsBuild - "+loaded_champion[0]["alias"]
    loaded_build["uid"] = "Runeitems"
    return loaded_build


if __name__ == "__main__":
    update_local_files("./champions")
    for filename in os.listdir("./champions"):
        if filename.endswith(".json"):
            print(filename)
            modified_build = process_json_files(filename, "build.json")
            update_lol_file(modified_build, r"C:\Games\Riot Games\League of Legends")
