#! /usr/bin/env python

import magic

def get_mime(file_descr):
    mime = magic.from_buffer(file_descr.read(), mime=True)
    return mime

if __name__=="__main__":
    with open('cat.jpg','rb') as finput:
        print(get_mime(finput))
