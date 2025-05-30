from bs4 import BeautifulSoup
from dicts import HtmlDicts, FileNamesDicts
from items_to_json import toJson

class Parser:
    

    def toParser(htmlDictsNum: int, params: str, fileNames: int):
        list_to_json = []
        file_path = HtmlDicts.html_dicts[htmlDictsNum]

        with open(file_path, encoding="utf-8") as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, "html.parser")
        modals = soup.find(class_='modal-body').find_all('div',class_='checkbox')
        modalsInput = soup.find_all('input',{'name': f'params[0][{params}][]'})


        for modal, value in zip(modals, modalsInput):
            if value.get('value'):
                tag = value.get('value')
                modalText = modal.text.strip()
                list_to_json.append({
                    f"{tag.strip()}": modalText
                })

        toJson.generateJson(list_to_json, FileNamesDicts.fileNames_dicts[fileNames])
        

