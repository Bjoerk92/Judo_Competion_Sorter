"""

"""
from typing import Literal


class CSV():

    def __init__(self, fileName : str, deliter : Literal[";", ","]):
        
        self.header : list[list[str]] = []
        self.csv : list[list[str|int|bool]] = []
        
        try:
            file = open(fileName, '+r')

            fileString = file.read()
            
            print("test")






        except Exception:
            print("Couldn't open file ")




    def __del__(self):
        pass

