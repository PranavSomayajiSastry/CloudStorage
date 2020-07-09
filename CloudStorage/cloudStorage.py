import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token= access_token
    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
def main():
    access_token= ' '
    transferData = TransferData(access_token)

    file_from= input('Enter Your File Path To Upload To Dropbox: ')
    file_to= input('Enter The File Path: ')
    transferData.upload_file(file_from, file_to)
    print("File(s)/Folder(s) Has Been Moved")


main()