from dicts import HtmlDicts
import re

class FormatData:

    

    def formattingData(list_to_json, modals, modalsInput, name: str ):
        count = 0

        result = name.split(HtmlDicts.base_dir)[1]
        if result == "connection.html":
            for modal, value in zip(modals, modalsInput):
                if value.get('value'):
                    tag = value.get('value')
                    modalText = modal.text.strip()
                    list_to_json[f"{tag.strip()}"] = {"text": f"{modalText}"}
        if result == "gsm.html":
            for modal, value in zip(modals, modalsInput):
                if value.get('value'):
                    tag = value.get('value')
                    modalText = modal.text.strip()
                    list_to_json[f"{tag.strip()}"] = {"text": f"{modalText}"}
        else:
            for modal, value in zip(modals, modalsInput):
                count += 1
                if value.get('value'):
                    tag = value.get('value')
                    modalText = modal.text.strip()
                    full_text = FormatData.splitStringFull(modalText)
                    short_text = FormatData.splitStringShort(modalText)
                    list_to_json[f"{tag.strip()}"] = {"full_text": f"{full_text}", "short_text": f"{short_text}"}
                    
        
        return list_to_json
    

    def splitStringFull(text: str) -> str:
        result = text.split("(", 1)[0]
        return result.strip()
    
    def splitStringShort(text: str) -> str:
        value = text.split("(")[1]
        result = value[:-1]
        return result.strip()

