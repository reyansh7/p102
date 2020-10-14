import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='TNjrPSdtXewAAAAAAAAAATFMhwvOqTlUS-40ScaIRaVBL22b10mMPrX6YmqXJsxT'
    transferData=TransferData(access_token)

    file_from = 'algorithm.txt'
    file_to = ' /test_dropbox/algorithm.txt'

    transferData.upload_file(file_from,file_to)
    print('file has been moved')

main()

input('Enter to exit')