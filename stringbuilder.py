# In his name
# Title: String Builder
# Description: Handle's large string operations
# Author: MohammadReza Tayyebi
# Source: https://stackoverflow.com/questions/2414667/python-string-class-like-stringbuilder-in-c

# Libraries
import io

# BOF
class stringbuilder:
    _file_str = None

    def __init__(self):
        ''' Constructor for this class '''
        self._file_str = io.StringIO()

    def Append(self, str):
        self._file_str.write(str)

    def Cls(self):
        self.__init__();

    def __str__(self):
        return self._file_str.getvalue()
