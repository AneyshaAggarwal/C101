import dropbox;

class TransferData:
    def __init__ (self, access_token):
        self.access_token = access_token;

    def upload_files(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token);
        f= open(file_from, 'rb');
        dbx.files_upload(f.read(), file_to);

def main():
    accessToken= 'sl.BIrBZX3HpwJsLnyrRk3PX1y1gyGCLCIMwzS5R8MHTHvM7GvEfZNQzrF2T-obKY-sCyyREmm2i64TWmZzV99VwvL2whowIgXPfudXh6gfv89d4Zzynht0PehPnZsWTwBDueLyQtgfyGs';
    transferData = TransferData(accessToken);

    file_from = input('Enter the path of the file needed to be transfered: ');
    file_to = input('Enter the path of the destination of the transfered file: ');

    transferData.upload_files(file_from, file_to)

    print("Your file ", file_from, " has been successfully transerfered to ", file_to);

main()
