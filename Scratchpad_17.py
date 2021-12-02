# def search_and_replace(file, string1, string2):
#     with open(file, "r") as fo:
#         contents = fo.read()

#         with open("sampletext2.txt", "w") as fo:        
#             fo.write(contents.replace("john", "jane"))

#         with open("sampletext2.txt", "r") as fo:
#             print(fo.read())

# search_and_replace("sampletext.txt", "john", "jane")



# def letter_count(file):
#     with open(file, "r") as file:
#         contents = file.read()
#         count = 0
#         for i in contents:
#             if i == " " or i == "\n":
#                 continue
#             else:
#                 count += 1
#         print(count)

# letter_count("text1.txt")

# def line_count(file):
#     with open(file, "r") as file:
#         contents = file.read()
#         count = 0
#         for i in contents:
#             if i == "\n":
#                 count  =+ 1
#             else:
#                 continue
#         print(count)

# line_count("text1.txt")
