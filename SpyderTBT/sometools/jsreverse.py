import base64
import json

from Crypto.Cipher import AES


class AESCipher:
    # def __init__(self):
    # self.data="OKxA/6gIjg88CPPUUltdsPexelr5h3bu2fviJKx2J141oei10p+55AntxCUL3AQacXOh/GIETIUKTZRcX13gYZJucPF1VwBtiRE5M8hICcJ3F5ig/bIUBjb1YrzDr6qPDYvvN9COJquiwAHIyJbVHeGKB0VcZ2RR1wQ2ViLqs0KIxBOzRfol0t0izKdfsl26pMOptmLidmPH/LuPZv2wqE3QpZbCnZiLsF93kHcfxjkLAygQLyHnT2b7/6Zy7h1cLQvrBHwfEGltGuGxdlTpbS8FaVNwnINpsFSVREPAMKkZhtiSuyQ7EuscKoeCJpJhwLndJaxMQlU/+mtuwxnrZOAwowfijzkyEws8Hb/7Xl8l+DHJ6k26LT4I+5vv/z2pKEGDx16nvvaIkI0s14XpfoSXPS6Ffl+543GVbcNXG9QzHsIgh2FjiMeeQaGxT72j1BY/dvycuKCQedYOIePjNMZLqf5Apf/j4k6IZWUGimgOO1h0/FY0jLoE+UbQ1w7Ivw7j4EHuFmJigALUD9lEuW8JY5iWU7kINAX3fguSLSbtu2Y9sMypyJPdz9fDjWu5LzymhmRb+n1IC+27EXOXfKr+n8wt+SZnP9DbdaPi9gXE6jnOOgzR3EivlEbI5+3HStgtRFIInuCfbuUI0O9sa5V9sdf4AuiipR6RzG0AAFXdgMX0hhPYbRTZggpK1bEVmvSrYyG3QY58Q/TSS+nKujBrRGDoPkzILLV2u0Oz37udiIu4eVeCzLnPTM1mT90+EfUsb/abNBki3GQv6vw3lWonw66P2Jmd6VGs8+k3kNOBJydfc0H5Q6xJwZ3v++jrtbCbHD05lY9x1yzLGaB0PdXl+ADwyLvVDT6fGzCOwTL8JHOGRKief+3WVvTMTSqbUygKS1O/S0AIhL0ZkSnqS+QkBlEdpA3QMpGkRBfaXI8WeHTrmNHMncY2CD2/mfETeebiJ0Q1t96O6YmS+wdw30pxscePWnuTol13qnrhMV81kwiFYStqV2mS4tJcTRQe0CxCoHaUABFf3tuYL7Qtkqt67zabgO5D/Iwn8rEnlSgvtUNHG+/8qRTytSxOKqCZj0svfcembOgkkODLu6YbOxMQX0uBrAppTlIBSnz5+phKVcj6aSJIvGlanE2IzSvRWaz15s3H/eaO7piIbraEV11K+4dr/kcPRmsa+B1mxAlpkmvkK4qJDqbhV7C3u+K0si9VR0cfd+4YkXIr97bg5yMleJpcyqADZPiC7PlsfQRCcjfQrBZPLqDwIbrsqUPrMZQFgFCTt3EWENmyhejV7rhvpCP9qkbn9JvnYv3a3asJkZlfPNAaOn0Fuy8E1RwxcyocPN89NNmYQ0H/4ignow=="

    def decrypt_data(self, data):
        key = b'1234123412ABCDEF'  # 密钥
        iv = b'ABCDEF1234123412'  # 向量（IV）

        encrypted_data = base64.b64decode(data)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data)
        # unpadded_data = unpad(decrypted_data, AES.block_size)
        decrypted_str = decrypted_data.decode('utf-8')
        decrypted_json = json.loads(decrypted_str.rstrip('\x00'))
        print(decrypted_json)
        return decrypted_json

# if __name__ == '__main__':
#     aes=AESCipher()
#     aes.decrypt_data()
