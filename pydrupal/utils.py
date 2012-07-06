import os
import string
from itertools import imap
from itertools import repeat
from collections import defaultdict

env = { "module_path":None }

def find_modules():
    path = '.'
    while os.path.split(os.path.abspath(path))[1]:
        joined = os.path.join(path, 'modules')
        if os.path.exists(joined):
            return os.path.abspath(joined)
        path = os.path.join('..', path)

class ModuleInfoParser(defaultdict):
    
    def read(self, path):
        with open(path) as info:
            for line in info:
                line = line.strip();
                if line.startswith(';') or len(line) == 0:
                    continue
                parts = line.split("=")
                parts = imap(string.strip, map(string.strip, parts), repeat("\"'"))
                
                key, value = list(parts)
                if key.rfind('[]') == -1:
                    self[key.lower()] = value

    def __missing__(self, key):
        return None