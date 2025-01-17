import json
import os
import colorama

RED = colorama.Fore.RED
colorama.init(autoreset=True)
def read_json(name_json: str) -> dict:
    try:
        path_to_json = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "jsons", name_json))
        
        with open(path_to_json, "r") as file:
            my_dict = json.load(file)
            return my_dict
        
    except Exception as exception:
        print(f"{RED}Сталася помилка: {exception}")
        return {}
