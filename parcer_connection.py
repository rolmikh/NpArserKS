from bs4 import BeautifulSoup
from dicts import HtmlDicts

def parser_connection():
    file_path = HtmlDicts.html_dicts[0]

    with open(file_path, encoding="utf-8") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    modals = soup.find(class_='modal-body').find_all('div',class_='checkbox')
    modalsInput = soup.find_all('input',{'name': 'params[0][connection][]'})


    for modal in modals:
        print(modal.text)

    for value in modalsInput:
        if value.get('value'):
            tag = value.get('value')
            print(tag)



if __name__ == '__main__':
   parser_connection()



