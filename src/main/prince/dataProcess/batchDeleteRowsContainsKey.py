import json
import os

folder_path = 'C:/MyProjects/gitlab_repo/sims-selfservice-3-ui/src/assets/i18n-password'


# read json file from folder
def readJsonFile(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


# delete rows contains keyword
def deleteRowsContainsKey(jsonData, keyword):
    for key in list(jsonData):
        if key.find(keyword) != -1:
            del jsonData[key]
    return jsonData


# write json data to file
def writeJsonFile(jsonData, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(jsonData, f, ensure_ascii=False, indent=4)


# main method
if __name__ == '__main__':
    # traverse json files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json") and file != 'en.json':
                # retrieve json data from the file
                data = readJsonFile(folder_path + '/' + file)
                print("before: " + str(data))
                # delete key value pair which contains the keyword
                deleteRowsContainsKey(data, 'E-100')
                print("after: " + str(data))
                # write the json data back to file
                writeJsonFile(data, folder_path + '/' + file)
                print("filename: " + file + " write success")
    print("all files have been processed successfully!")
