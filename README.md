## League of Legends Champion Items Importer

This Python script is designed to import items to all League of Legends champions at once. It reads item data from JSON files located in a specified folder, then updates the League of Legends item sets accordingly.

### Dependencies

- Python 3.x
- GitPython library (`pip install GitPython`)

### Usage

1. Clone or download this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Make sure you have League of Legends installed and know the path to your League of Legends directory.
4. Place your champion item JSON files in the `champions` directory.
5. Run the script using `python import_items.py`.

### Functionality

- `update_local_files(folder)`: This function updates local files by pulling the specified repository. If the repository does not exist, it clones it and prints an error message.
  
- `write_json(data, filepath)`: Writes JSON data to a file specified by the file path.

- `update_lol_file(filename, lol_filepath)`: Updates the League of Legends item sets file with new data from the specified JSON file.

### Example
bash
$ python import_items.py

### Acknowledgments
Special thanks to [Al Cheung](https://github.com/cangzhang).