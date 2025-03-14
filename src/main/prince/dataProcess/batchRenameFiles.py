import os


def batch_rename_files_ui():
    for foldName, subfolders, filenames in os.walk(path):  # os.walk() get folderName, subfolders, filenames in the path
        for filename in filenames:  # traverse all files in the path
            if filename.endswith('.json'):  # when the filename ends with .json
                if filename == 'en.json':  # if the filename is en.json, skip
                    continue
                if filename.startswith('zh'):
                    new_name = filename.lower()  # rename the filename to lower case
                else:
                    new_name = filename.split('-')[
                                   0] + '.json'  # split the filename by '-', get the first part, then add '.json' suffix
            elif filename.endswith('.properties'):  # when the filename ends with .properties
                if filename == 'en.properties':  # if the filename is en.properties, skip
                    continue
                if filename.startswith('zh'):
                    new_name = filename.lower()  # rename the filename to lower case
                else:
                    new_name = filename.split('-')[
                                   0] + '.properties'  # split the filename by '-', get the first part, then add '.properties' suffix

            else:
                continue  # skip other files
            os.rename(os.path.join(foldName, filename), os.path.join(foldName, new_name))  # rename the file
            print(filename, "has been renamed successfully! New name is: ", new_name)  # print the result


def batch_rename_files_rest(filepath):
    new_name = ''
    for foldName, subfolders, filenames in os.walk(path):  # os.walk() get folderName, subfolders, filenames in the path
        for filename in filenames:  # traverse all files in the path
            country_prefix = 'countries_'
            mail_prefix = 'mail_'
            if filename.endswith('.properties'):  # when the filename ends with .properties
                if filepath.find('Countries') != -1:  # if the filepath contains Countries, add prefix 'countries_'
                    if filename == 'en.properties':  # if the filename is en.properties
                        new_name = country_prefix + filename  # add prefix
                    elif filename.startswith('zh'):
                        new_name = country_prefix + filename.lower()  # rename the filename to lower case
                    else:
                        new_name = country_prefix + filename.split('-')[
                            0] + '.properties'  # split the filename by '-', get the first part, then add '.properties' suffix
                elif filepath.find('e-mails') != -1:
                    if filename == 'en.properties':  # if the filename is en.properties
                        new_name = mail_prefix + filename  # add prefix
                    elif filename.startswith('zh'):
                        new_name = mail_prefix + filename.lower()  # rename the filename to lower case
                    else:
                        new_name = mail_prefix + filename.split('-')[
                            0] + '.properties'  # split the filename by '-', get the first part, then add '.properties' suffix
            else:
                continue  # skip other files
            os.rename(os.path.join(foldName, filename), os.path.join(foldName, new_name))  # rename the file
            print(filename, "has been renamed successfully! New name is: ", new_name)  # print the result


def batch_rename_files_sarba(filepath):
    new_name = ''
    for foldName, subfolders, filenames in os.walk(path):  # os.walk() get folderName, subfolders, filenames in the path
        for filename in filenames:  # traverse all files in the path
            messages_prefix = 'pingfederate-messages_'
            email_messages_prefix = 'pingfederate-email-messages_'
            if filename.endswith('.properties'):  # when the filename ends with .properties
                if 'e-mails' not in filepath:  # if the filepath contains Authentication Service
                    if filename == 'en.properties':  # if the filename is en.properties
                        new_name = 'pingfederate-messages.properties'
                    elif filename.startswith('zh'):
                        new_name = messages_prefix + filename.replace("-", "_")  # special case for zh files
                    else:
                        new_name = messages_prefix + filename.split('-')[
                            0] + '.properties'  # split the filename by '-', get the first part, then add '.properties' suffix
                elif 'e-mails' in filepath:
                    if filename == 'en.properties':  # if the filename is en.properties
                        new_name = 'pingfederate-email-messages.properties'
                    elif filename.startswith('zh'):
                        new_name = email_messages_prefix + filename.replace("-", "_")  # special case for zh files
                    else:
                        new_name = email_messages_prefix + filename.split('-')[
                            0] + '.properties'  # split the filename by '-', get the first part, then add '.properties' suffix
            else:
                continue  # skip other files
            os.rename(os.path.join(foldName, filename), os.path.join(foldName, new_name))  # rename the file
            print(filename, "has been renamed successfully! New name is: ", new_name)  # print the result

def batch_rename_files_core(filepath):
    new_name = ''
    for foldName, subfolders, filenames in os.walk(path):  # os.walk() get folderName, subfolders, filenames in the path
        for filename in filenames:  # traverse all files in the path
            if filename.endswith('.properties'):  # when the filename ends with .properties
                if 'zh' in filename:  # if the filename contains 'zh'
                    new_name = filename.replace("-", "_")  # special case for zh files
                else:
                    name, ext = os.path.splitext(filename)  # split the filename by '.'
                    new_name = name[:-3] + ext  # remove the last 3 characters of the filename
            else:
                continue  # skip other files
            os.rename(os.path.join(foldName, filename), os.path.join(foldName, new_name))  # rename the file
            print(filename, "has been renamed successfully! New name is: ", new_name)  # print the result


if __name__ == '__main__':
    path = r'C:\Working\Demand\Add_translation\5.2.0.RC3\core'  # the path of the files
    if path.find('ui') != -1:  # if path contains string 'ui', invoke batch_rename_files_ui()
        print("rename language artifacts in Self Service UI...")
        batch_rename_files_ui()
    elif path.find('rest') != -1:  # if path contains string 'rest', invoke batch_rename_files_rest()
        print("rename language artifacts in Self Service Rest...")
        batch_rename_files_rest(path)
    elif path.find('sarba') != -1:  # if path contains string 'sarba', invoke batch_rename_files_sarba()
        print("rename language artifacts in Auth Service...")
        batch_rename_files_sarba(path)
    elif path.find('core') != -1:  # if path contains string 'core', invoke batch_rename_files_core()
        print("rename language artifacts in Core...")
        batch_rename_files_core(path)
    print("All files have been renamed successfully!")
