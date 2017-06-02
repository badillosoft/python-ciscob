import h_2_3_module as h23

f = open("conversation.txt", "r")
text = f.read()
f.close()

print h23.mask3(text)