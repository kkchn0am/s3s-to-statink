import os
import sys
import shutil
import json

folder_path = sys.argv[1]

os.mkdir(folder_path + '/vs_regular')
os.mkdir(folder_path + '/vs_bankara')
os.mkdir(folder_path + '/vs_xmatch')
os.mkdir(folder_path + '/vs_event')
os.mkdir(folder_path + '/vs_private')

filelist = os.listdir(folder_path)
filelist.sort

for filename in filelist:
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        if data["data"]["vsHistoryDetail"]["vsMode"]["mode"] == "BANKARA":
            shutil.move(folder_path + '/' + filename, folder_path + '/vs_bankara')
        elif data["data"]["vsHistoryDetail"]["vsMode"]["mode"] == "XMATCH":
            shutil.move(folder_path + '/' + filename, folder_path + '/vs_xmatch')
        elif data["data"]["vsHistoryDetail"]["vsMode"]["mode"] == "LEAGUE":
            shutil.move(folder_path + '/' + filename, folder_path + '/vs_event')
        elif data["data"]["vsHistoryDetail"]["vsMode"]["mode"] == "PRIVATE":
            shutil.move(folder_path + '/' + filename, folder_path + '/vs_private')
        else:
            shutil.move(folder_path + '/' + filename, folder_path + '/vs_regular')
