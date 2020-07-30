import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)  
                                 
def main():
    access_token = ''
        #access token to be coppied from https://www.dropbox.com/developers/apps/
            #For example: VF9FHe56WkAAAAAAAAAADe9jdM3IIhZMd2wqGZxRnW1eDaXhn0_6Es4qO-9Qw7r6
    transferData = TransferData(access_token)

    file_from = str(input("Enter The File Path To Transfer: "))
    file_to = input("Enter The Full Path To Upload To Dropbox: ")
    # API v2
    transferData.upload_file(file_from,file_to)
    print("!!The File(s)/ Folder(s) Has/ Have Been Moved!!")
main()
