from cryptography.fernet import Fernet
import base64
import hashlib
import random

chave_secreta_texto = '#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista'
chave_secreta_bytes = hashlib.sha256(chave_secreta_texto.encode()).digest()
chave_secreta_base64 = base64.urlsafe_b64encode(chave_secreta_bytes)
fernet = Fernet(chave_secreta_base64)

def metodo1(senha):
    senha_ascii = [str(ord(char)) for char in senha]
    senha_criptografada = fernet.encrypt(','.join(senha_ascii).encode())
    return senha_criptografada

def metodo2(senha):
    senha_criptografada = ''
    for caractere in senha:
        if caractere.isalpha():
            if caractere.islower():
                senha_criptografada += chr(((ord(caractere) - ord('a') + 4) % 26) + ord('a'))
            else:
                senha_criptografada += chr(((ord(caractere) - ord('A') + 4) % 26) + ord('A'))
        elif caractere.isdigit():
            senha_criptografada += str((int(caractere) - 3) % 10)
        else:
            senha_criptografada += caractere
    senha_criptografada = fernet.encrypt(senha_criptografada.encode())
    return senha_criptografada

def metodo3(senha):
    senha_embaralhada = ''.join(random.sample(senha, len(senha)))
    senha_criptografada = ''
    for i, char in enumerate(senha_embaralhada):
        if char.isalpha():
            offset = 2 * (i + 1)
            if char.islower():
                senha_criptografada += chr(((ord(char) - ord('a') + offset) % 26) + ord('a'))
            else:
                senha_criptografada += chr(((ord(char) - ord('A') + offset) % 26) + ord('A'))
        elif char.isdigit():
            senha_criptografada += str((int(char) - 2) % 10)
        else:
            senha_criptografada += chr(((ord(char) - ord(' ') + 1) % 26) + ord(' '))
    senha_criptografada = fernet.encrypt(senha_criptografada.encode())
    return senha_criptografada

senha1 = "12modal3"
senha2 = "MoDaLGr2023"
senha3 = "Modal@2023"

senha1_criptografada = metodo1(senha1)
senha2_criptografada = metodo2(senha2)
senha3_criptografada = metodo3(senha3)