import base64
import binascii
import urllib.parse

from twofish import Twofish



def show_cookie_view(request):
    cookie = request.COOKIES.get('DjangoENC')
    cookie = urllib.parse.unquote(cookie).encode('utf-8')
    key = 'AFBC88806825247863001E4F4B105BDB'
    cookie_data = decrypt64(cookie, key)
    return cookie_data
    #print(f'El valor de la cookie es {cookie_data}')


def decrypt64(data, key):
    key = binascii.unhexlify(key)
    T = Twofish(key)

    # Decodificar los datos cifrados en base64
    encrypted_data = base64.b64decode(data)

    # Dividir los datos en bloques de 16 bytes
    block_size = 16
    data_blocks = [encrypted_data[i:i + block_size] for i in range(0, len(encrypted_data), block_size)]

    # Desencriptar cada bloque y concatenar los resultados
    decrypted_data = b''
    for block in data_blocks:
        decrypted_block = T.decrypt(block)
        decrypted_data += decrypted_block

    return decrypted_data.decode('utf-8')