import pickle
import pyAesCrypt
import io
from os import stat, remove

class FileEncryptionManager:
    filename = "passwords"
    bufferSize = 64 * 1024

    def save(self, passwords, master_pass):
        # serialize passwords list  to binary:
        binary_passwords = pickle.dumps(passwords)
        f_input = io.BytesIO(binary_passwords)
        # initialize cipher binary stream
        f_output = io.BytesIO()
        # encrypt binary stream to file_stream
        pyAesCrypt.encryptStream(
            f_input, f_output, master_pass, self.bufferSize)
        # get encrypted data
        encrypted_data = f_output.getvalue()
        # open file where data will be saved (in "write binary" mode)
        file = open(self.filename, 'wb')
        file.write(encrypted_data)
        file.close()

    def load(self, master_pass):
        # open file where data was saved (in "read binary" mode)
        try:
            f_input = open(self.filename, 'rb')
        except FileNotFoundError:
            return {}
        # initialize decrypted binary stream
        f_output = io.BytesIO()
        # get encrypted file size
        file_size = stat(self.filename).st_size
        # decrypt stream
        try:
            pyAesCrypt.decryptStream(
                f_input, f_output, master_pass, self.bufferSize, file_size)
        except ValueError:
            print("Wrong password, try again")
            return
        binary_data = f_output.getvalue()
        return pickle.loads(binary_data)
