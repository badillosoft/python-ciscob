# _*_ coding: utf-8 _*_

# Split one file into n-files using "modules" and indexes

# Example:
# my_file.txt:
#   Hello this is a secret file,
#   please ensure to mantain it safely

# N = 3 # define by user
# my_file_1.txt
#   Hltss cti, ... and so
# my_file_2.txt
#   eoh  sr l ... and so
# my_file_3.txt
#   l i i a e ... and so

def split_file(source_name, n):
    # Open the source file
    f = open(source_name, "r")

    # Get the (full) content
    content = f.read()

    # Don't forget close the file
    f.close()

    # i joins from 0 to n - 1 (don't tocuh the last)
    for i in range(n):
        # Get the content for the i-time
        # it's the string split by n, with offset of i
        ci = content[i::n]

        # Open the file "my_file_<i>.txt" in "w" mode
        # In "w" mode the file is created if not exists
        fi = open("output_%d.txt" % (i + 1), "w")

        # Write the content "ci" for this file
        fi.write(ci)

        fi.close()


split_file("my_file.txt", 4) # Split my_file.txt in 4 files