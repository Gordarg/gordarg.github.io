# In his name
# Title: Names PY
# Description: Create single names based on path
# Author: MohammadReza Tayyebi
# Source: https://mail.python.org/pipermail/python-win32/2005-April/003100.html
#         https://stackoverflow.com/questions/2510716/short-python-alphanumeric-hash-with-minimal-collisions

# Libraries
import base64
import hashlib

# BOF
class names:
    _storage = None

    def __init__(self):
        ''' Constructor for this class '''
        self._storage = ''

    def Generate(self, strr):
        # Method 1
        # for c in strr:
        #     self._storage += str(ord(c))

        # Method 2
        # self._storage = strr

        # Method 3
        self._storage = strr

    def __str__(self):
        # Method 1
        # return self._output

        # Method 2
        # return ''.join(x.encode('hex') for x in self._storage)

        # Method 3
        hasher = hashlib.sha1(self._storage.encode('utf-8'))
        output = str(base64.urlsafe_b64encode(hasher.digest()))[2:15]
        #print (output)
        return output
