# jabbers = open("/Users/S-Mac/Dropbox/Shiven/Python Learning 2020 Summer/FileIO/sample.txt", 'r')
#
# for line in jabbers:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabbers.close()
#
# with open("/Users/S-Mac/Dropbox/Shiven/Python Learning 2020 Summer/FileIO/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("/Users/S-Mac/Dropbox/Shiven/Python Learning 2020 Summer/FileIO/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()
#
# with open("/Users/S-Mac/Dropbox/Shiven/Python Learning 2020 Summer/FileIO/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line)
#

with open("/Users/S-Mac/Dropbox/Shiven/Python Learning 2020 Summer/FileIO/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line)

with open("/Users/S-Mac/Dropbox/Shiven/Python Learning 2020 Summer/FileIO/sample.txt", 'r') as jabber:
    lines = jabber.read()
print("=" * 50)
for line in lines[::-1]:
    print(line, end='')


