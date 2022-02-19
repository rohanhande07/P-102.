import dropbox
import os
from dropbox.files import WriteMode
import shutil
import time

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
    
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, filename)
        
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'GrTrwNAJ-4AAAAAAAAAAASz0NyYTaFIIEjJjFQVre5u_b_I0DW-ade2jUoiWMpay'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer "))
    file_to = input("Enter the full path to upload to dropbox ")

    transferData.upload_file(file_from,file_to)
    print("The file has been moved")

main()


def delete():

    path = input("Enter the name of the directory to be sorted: ")
    days = 30
    seconds = time.time() - (days*24*60*60)
    deletedFoldersCount = 0
    deletedFilesCount = 0

    if(os.path.exists(path)):
        for rootFolder, folders, files in os.walk(path):
            #comparing the days
            if seconds >= getFileOrFolderAge(rootFolder):
                #removing the folders
                removeFolder(rootFolder)
                deletedFoldersCount = deletedFoldersCount + 1
                break
            else:
                #checking folder from root folder
                for folder in folders:
                    #folder path
                    folderPath = os.path.join(rootFolder, folder)

                    #comparing with the days
                    if seconds >= getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFoldersCount = deletedFoldersCount + 1

                #checking current directory files
                for file in files:
                    filePath = os.path.join(rootFolder, file)

                    if seconds >= getFileOrFolderAge(filePath):
                        removeFile(filePath)
                        deletedFilesCount = deletedFilesCount + 1

                    else:
                        #if path is not a directory
                        #comparing with the days
                        if seconds >= getFileOrFolderAge(path):
                            removeFile(path)
                            deletedFilesCount = deletedFilesCount + 1
        
    else:
        #file or folder is not found
        print(f"{path} is not found")
    print(f"Total folders deleted: {deletedFoldersCount}")
    print(f"Total filed deleted: {deletedFilesCount}")


            
        
def removeFolder(path):
    if(not shutil.rmtree(path)):
        print(f"{path} has been removed successfully")
    else:
        print("Unable to delete the path"+ path)
    
def removeFile(path):
    if(not os.remove(path)):
        print(f"{path} has been removed successfully")
    else:
        print("Unable to delete the path", path)

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__delete__':
    delete()