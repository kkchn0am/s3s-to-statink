import os
import sys
import shutil
import json

os.mkdir(args[1]/regular)
os.mkdir(args[1]/bankara)
os.mkdir(args[1]/xmatch)
os.mkdir(args[1]/event)
os.mkdir(args[1]/private)

for filename in filelist
    with open(filelist) as f
        d = json.loads(f)
        if d["bankara"] == True:
            shutil.move(args[1]/bankara)
        elif d["Xmatch"] == True:
            shutil.move(args[1]/xmatch)
        elif d["event"] == True:
             shutil.move(args[1]/event)
        elif d["private"] == True:
             shutil.move(args[1]/event)
        else:
             shutil.move(args[1]/regular)
