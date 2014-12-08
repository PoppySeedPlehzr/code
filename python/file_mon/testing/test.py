
#####
#####   This file is used for herp-derping with Python.
#####


# import sys

# if __name__ == '__main__':
    # dirs = []
    # if(len(sys.argv) > 1):
        # dir_file = open(sys.argv[1], 'r')
        # for i in dir_file.readlines():
            # dirs.append(i.split('\n'))
            # print "File added: " + i.split('\n')[0]
        # file_mon(dirs)
    # else:
        # print "Please specify the plain text file containing the list of directories."

# permissions = []
# data = ["NT Authority\\Authenticated Users:C", "HANDEL\\nanderson:F", "BUILT IN\\Administrators:F"]
# for d in data:
    # p = d.split()
    # t = []
    # cnt = 1
    # tmp = p[-cnt].split("\\")
    # while(len(tmp) == 1):
        # cnt+=1
        # t.append(tmp[0])
        # tmp = p[-cnt].split("\\")
    # t.append(tmp[1])
    # permissions.append(' '.join(t[::-1]))

import sys, os, subprocess, hashlib, time

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
ntfs_hashes = {}

for f in files:
    data = subprocess.Popen("cacls \"" + f + "\"", stdout=subprocess.PIPE, shell=True).stdout.read()
    ntfs_hashes[f] = hash(data)

while(True):
    for f in files:
        v = hash(subprocess.Popen("cacls \"" + f + "\"", stdout=subprocess.PIPE, shell=True).stdout.read())
        if(v != ntfs_hashes[f]):
            print "Alert!  NTFS File Permissions have changed!  Recommend restore from backup!"
    print "Sleeping"
    time.sleep(5)
    

# fperms = {}
# # Stores all of the current file permissions, to be used in backup_files function
# for f in files:
    # data = subprocess.Popen("cacls \"" + f + "\"", stdout=subprocess.PIPE, shell=True).stdout.readlines()
    # permissions = []
    # for d in data:
        # p = d.split()
        # if(len(p)):
            # tmp = p[-1].split("\\")
            # if(len(tmp) > len(p[-1])):
                # permissions.append(tmp[1])
            # else: # This case should only ever happen if the username/group has spaces.
                # username = tmp[0]
                # for i in range(1,len(p)):
                    # tmp = p[-i-1].split(
            
    # fperms[f] = permissions
    # cacls_cmd = "cacls \"" + f + "\"" + " /G %username%:R"
    # subprocess.Popen(cacls_cmd, stdin=subprocess.PIPE, shell=True).communicate('Y\r\n')
    
    # print fperms[f]

    
# # Restore the previous file permissions, to be used in restore_file function
# fname = files[2]
# # Perform the copy of the file, then change it's permissions to be that of the users before
# #usrs = fperms[fname][0]
# usrs = ' '.join(fperms[fname])
# #if len(fperms[fname]) > 1:
# #    for s in range(1,len(fperms[fname])):
# #        usrs += " " + fperms[fname][s]
# cacls_cmd = "cacls \"" + f + "\"" + " /G " + usrs
# subprocess.Popen(cacls_cmd, stdin=subprocess.PIPE, shell=True).communicate('Y\r\n')



