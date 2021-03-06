# file_mon.py
# Nick Anderson
#
#  Used to monitor all files in text file passed in argv.  Anytime
# a file is modified it is immediately restored from
# a readonly backup.  To be used at the CCDC.
#
#   TODO:  This system currently does not detect if a file has had
#  it's ntfs file permisions altered...  We should look into how to
#  detect this.  It might be as simple as running a check sum on the data
#  obtained from calling cacls once...?  That might be slow though.
#  This would definitely be a feature we could use...
# 
# 

import os, sys, time, shutil, stat, subprocess

def backup_files(files):
    # First, create a new folder specific to this
    # instance of the file_mon.  This is where the backups will
    # be stored.
    pTime = time.localtime()
    backup_dir = os.getcwd() + "\\backups\\" + str(pTime.tm_hour) + "_" + str(pTime.tm_min) + "_" + str(pTime.tm_sec) + "\\"
    
    # Make the new backup directory
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    fperms = {}
    for file in files:
        # This check shuold never fail, as we just made the directory, but let's leave it just to prevent
        # duplicates.
        if not os.path.exists(backup_dir + os.path.basename(file)):
            # Copy the file and all metadata.
            shutil.copy2(file, backup_dir + os.path.basename(file))
            
            # Store the files old NTFS file permissions for later use
            data = subprocess.Popen("cacls \"" + file + "\"", stdout=subprocess.PIPE, shell=True).stdout.readlines()
            permissions = []
            for d in data:
                p = d.split()
                if(len(p)):
                    t = []
                    cnt = 1
                    tmp = p[-cnt].split("\\")
                    while(len(tmp) == 1):
                        cnt+=1
                        t.append(tmp[0])
                        tmp = p[-cnt].split("\\")
                    t.append(tmp[1])
                    permissions.append(' '.join(t[::-1]))
            fperms[os.path.basename(file)] = permissions
            # Make the file strictly accesible to the current user.
            os.chmod(backup_dir + os.path.basename(file), stat.S_IREAD)
    
    # Make this directory readonly to the current user
    cacls_cmd = "cacls \"" + backup_dir + "\"" + " /T /G %username%:R"
    subprocess.Popen(cacls_cmd, stdin=subprocess.PIPE, shell=True).communicate('Y\r\n')
            
    return backup_dir, fperms
    
def restore_file(file, backup_dir, perm_list):
    # Copy the backed up file 
    shutil.copy2(backup_dir + os.path.basename(file), file)
    # Apply the old file permissions, so the correct users can read the file.
    cacls_cmd = "cacls \"" + file + "\"" + " /G " + ' '.join(perm_list)
    subprocess.Popen(cacls_cmd, stdin=subprocess.PIPE, shell=True).communicate('Y\r\n')
    

def file_mon(dirs):

    # Create a dictionary to hold the original file modified times.
    fmod_times = {}

    # Ensure that all files handed to us actually exist.
    exit = False
    for d in dirs:
        if not os.path.exists(d):
            print "File does not exist: " + d
            exit = True
        fmod_times[os.path.basename(d)] = os.stat(d).st_mtime
    if exit: sys.exit()
        
    # If this is our first run, make a folder in the current directory called backups.
    if not os.path.exists(os.getcwd() + "\\backups\\"):
        os.makedirs(os.getcwd() + "\\backups\\")
    backup_dir, fperms = backup_files(dirs)

    # Monitor the modified time of the files.
    while(True):
        for d in dirs:
            ## Check to ensure that the file hasn't been deleted.
            if not os.path.exists(d):
                print "File was moved or deleted!  Restoring from backup!"
                restore_file(d, backup_dir, fperms[d])
            else:        
                ## Used for debugging
                print os.path.basename(d) + "OMod time: " + str(fmod_times[os.path.basename(d)])
                print os.path.basename(d) + "CMod time: " + str(os.stat(d).st_mtime)
                if(fmod_times[os.path.basename(d)] != os.stat(d).st_mtime):
                    print os.path.basename(d) + " was modified!  Restoring from backup!"
                    restore_file(d, backup_dir, fperms[os.path.basename(d)])
                ## Print out the File Access time in a pretty format.
                #pTime = time.localtime(fInfo.st_atime)
                #print "File modified time: " + str(pTime.tm_hour) + ":" + str(pTime.tm_min) + ":" + str(pTime.tm_sec) + " - " + str(pTime.tm_mon) + "\\" + str(pTime.tm_mday) + "\\" + str(pTime.tm_year)
        print "All is well.  Sleeping."    
        time.sleep(5)
    
    
if __name__ == '__main__':
    dirs = []
    if(len(sys.argv) > 1):
        dir_file = open(sys.argv[1], 'r')
        for i in dir_file.readlines():
            dirs.append(i.split('\n')[0])
            print "File added: " + i.split('\n')[0]
        file_mon(dirs)
    else:
        print "Please specify the plain text file containing the list of directories."