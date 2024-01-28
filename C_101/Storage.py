import dropbox

class TransferData:
        def __init__(self, access_token):
            self.access_token=access_token
        def upload_file(self,file_from, file_to):
            dbx=dropbox.Dropbox(self.access_token)

            f =open(file_from, 'rb')
            dbx.files_upload(f.read(), file_to)
def main():
    access_token="sl.BphRvJb7-9GegzRv8srmeGfYKizMowtoZ8_wnJH_PXx5GUi9TEibD-dPm7SMFGDNWs8Wp4G4U9jIakIlZ6BAfpsOVQ1nIVjKjymtjHvlhBOx3AU1naTMso80oGezcSwpDgCKp8zXpdvV"
    transferData=TransferData(access_token)

    file_from=input("Enter file path: ")
    file_to = input("Enter full path to upload to Dropbox: ")

    transferData.upload_file(file_from, file_to)
    print('file has been transferred!!!')
          


main()