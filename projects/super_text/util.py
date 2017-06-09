import re
# from Crypto.Cipher import AES
# import base64

def search(text, word, i):
    pattern = "(%s)" % word
    it = re.finditer(pattern, text[i:], re.MULTILINE)
    for match in it:
        return match.span(1)[0] + i
    return -1

def open_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

def save_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

# def encrypt(text, password):
#     # TODO: Encrypt
#     msg_text = text.rjust(32)
#     secret_key = password # create new & store somewhere safe

#     cipher = AES.new(secret_key, AES.MODE_ECB) # never use ECB in strong systems obviously
#     encoded = base64.b64encode(cipher.encrypt(msg_text))
#     # ...
#     # decoded = cipher.decrypt(base64.b64decode(encoded))
#     # print decoded.strip()

#     return encoded

# def decrypt(encoded, password):
#     # TODO: Encrypt
#     secret_key = password # create new & store somewhere safe

#     cipher = AES.new(secret_key, AES.MODE_ECB) # never use ECB in strong systems obviously
#     decoded = cipher.decrypt(base64.b64decode(encoded))

#     return decoded