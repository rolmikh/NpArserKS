import json


class toJson:

    def generateJson(list, name: str):

        list_json = json.dumps(list, indent=4, ensure_ascii=False)

        with open(f"done_json/{name}.json", "w", encoding="utf-8") as file:
            file.write(list_json)


