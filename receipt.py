import os
import tempfile
import win32api

def prnt(txt):
    print(txt)
    temp_file = tempfile.mktemp('.txt')
    open(temp_file, 'w', encoding='utf-8').write(txt)
    # os.startfile(temp_file, 'print')
    win32api.ShellExecute(0, "print", temp_file, None, ".", 0)