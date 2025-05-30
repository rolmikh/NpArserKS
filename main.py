from parcer import Parser
from dicts import FileNamesDicts

sub_dict = FileNamesDicts.fileNames_dicts[5]

Parser.toParser(5, str(sub_dict), 5)
