from bs4 import BeautifulSoup
from dicts import HtmlDicts, FileNamesDicts
from items_to_json import toJson
from format_data import FormatData

class Parser:
    

    def toParser(htmlDictsNum: int, params: str, fileNames: int):
        list_to_json = {}
        file_path = HtmlDicts.html_dicts[htmlDictsNum]

        with open(file_path, encoding="utf-8") as file:
            html_content = file.read()

        name = file_path
        soup = BeautifulSoup(html_content, "html.parser")
        modals = soup.find(class_='modal-body').find_all('div',class_='checkbox')
        modalsInput = soup.find_all('input',{'name': f'params[0][{params}][]'})

        result = FormatData.formattingData(list_to_json, modals, modalsInput, name)

        toJson.generateJson(result, FileNamesDicts.fileNames_dicts[fileNames])
        

