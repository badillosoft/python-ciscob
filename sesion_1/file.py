# _*_ coding: utf-8 _*_

# open(name, mode) 
# name - Name of file (with path)
# mode - The opened mode (read / write / append)

# w - write mode
# r - read mode
# a - append mode
# w+ | r+ - read + wirte
# a+ - append + read

# Binary modes
# wb | rb | ab | wb+ | rb+ | ab+

# f binds to the file
f = open("my_file.txt", "r")

# To read the file content
contents = f.read()

# If file is not loger used, close it
f.close()

print "The content:"
print contents
print "=" * 40
print "The file contents %d characters" % len(contents)

# Format strings: Replace %* with type value
# %d - integers
# %f - floats
# %s - strings

# %10s - string filled with a max 10 "blank spaces"
# %3.4f - a float with 3 units and 4 decimals