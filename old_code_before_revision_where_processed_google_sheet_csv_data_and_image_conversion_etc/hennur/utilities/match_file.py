#!/usr/bin/python3

import os
import re


def match_photos(famid):
    matches = [re.search(fr'\b{famid}\b\..*', i).string for i in os.listdir('photos/resized') if
               re.search(fr'\b{famid}\b\..*', i)]
    if len(matches) == 1:
        return 'photos/resized/' + matches[0]
    else:
        return "img.jpg"
