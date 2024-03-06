import json
import time
from utils.champions_update import *


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


def process_json_files(champion, lane, build_file):
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
    with open(f"champions/{champion}.json") as champion_file, open(build_file) as build:
        loaded_build = json.load(build)
        loaded_champion = json.load(champion_file)
        final_objects = set()
        alternative_items = []

        # Find the lane ID for the given lane
        laneid = 0
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

        # Add alternative items to the build if there are repeated ones or at the end
        for alternative_item in alternative_items:
            block_index = 1 if len(
                loaded_build["blocks"][1]["items"]) < 6 else 2
            final_objects, loaded_build = add_item(
                alternative_item, final_objects, loaded_build, block_index)
        # Update associated champions and uid
        loaded_build["associatedChampions"].append(loaded_champion[0]["id"])
    loaded_build["uid"] = str(time.time())
    return loaded_build


def write_json(data, filepath):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def update_lol_file(data, lol_filepath):
    """
    Update the League of Legends (LoL) file with new data.

    Args:
        data: The new data to be added to the LoL file.
        lol_filepath: The file path to the LoL file.

    Returns:
        None
    """

    lol_filepath += "\Config\ItemSets.json"
    with open(lol_filepath) as old_lol_file:
        lol_data = json.load(old_lol_file)
        lol_data["itemSets"].append(data)
    write_json(lol_data, lol_filepath)


if __name__ == "__main__":
    update_local_files("./champions")
    modified_build = process_json_files("Aatrox", "top", "build.json")
    # write_json(modified_build, "build-1.json") # Test build
    # update_lol_file(process_json_files("Aatrox", "top", "build.json"), r"C:\Games\Riot Games\League of Legends")
    update_lol_file(modified_build, r"C:\Riot Games\League of Legends")
