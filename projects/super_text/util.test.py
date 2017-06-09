import util

print util.search("Hola mundo, este es un mensaje.", "e", 18)

enc = util.encrypt("Hola mundo, este es un mensaje.", "1234567890123456")
dec = util.decrypt(enc, "1234567890123456")

print enc
print dec