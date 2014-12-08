# file_mon.py
# Nick Anderson
#
#  Used to monitor all files passed in argv.  Anytime
# a file is modified it is immediately restored from
# a readonly backup.  To be used at the CCDC.
# 

import os, sys, time, shutil, stat

def backup_files(files):
    for file in files:
        if not os.path.exists(os.getcwd() + "\\backups\\" + os.path.basename(file)):
            # Copy the file and all metadata.
            shutil.copy2(file, os.getcwd() + "\\backups\\" + os.path.basename(file))
            # Make the file readonly
            os.chmod(os.getcwd() + "\\backups\\" + os.path.basename(file), stat.S_IREAD)
    
#def restore_file(file):
#    shutil.copy2(os.getcwd() + "backups\\" + os.path.basename(file), file)

def file_mon(dirs):

    # Create a dictionary to hold the original file modified times.
    fmod_times = {}

    # Ensure that all files handed to us actually exist.
    for d in dirs:
        if not os.path.exists(d):
            print "File does not exist: " + d
            sys.exit()
        fmod_times[os.path.basename(d)] = os.stat(d).st_mtime
        
    # Back up the files to a readonly directory.
    if not os.path.exists(os.getcwd() + "\\backups"):
        os.makedirs(os.getcwd() + "\\backups")
    backup_files(dirs)
    
    # Monitor the modified time of the files.
    while(True):
        for d in dirs:
            ## Used for debugging
            print os.path.basename(d) + "OMod time: " + str(fmod_times[os.path.basename(d)])
            print os.path.basename(d) + "CMod time: " + str(os.stat(d).st_mtime)
            if(fmod_times[os.path.basename(d)] != os.stat(d).st_mtime):
                print os.path.basename(d) + " was modified!  Restoring from backup!"
                shutil.copy2(os.getcwd() + "\\backups\\" + os.path.basename(d), d)
                os.chmod(d, stat.S_IWRITE)
                #restore_file(d)
            ## Print out the File Access time in a pretty format.
            #pTime = time.localtime(fInfo.st_atime)
            #print "File modified time: " + str(pTime.tm_hour) + ":" + str(pTime.tm_min) + ":" + str(pTime.tm_sec) + " - " + str(pTime.tm_mon) + "\\" + str(pTime.tm_mday) + "\\" + str(pTime.tm_year)
        print "All is well.  Sleeping."    
        time.sleep(5)
    
    
if __name__ == '__main__':
    dirs = []
    if(len(sys.argv) > 1):
        for i in range(1,len(sys.argv)):
            dirs.append(sys.argv[i])
            print "File added: " + sys.argv[i]
        file_mon(dirs)
    else:
        print "Please enter the full file path of each file to be monitored, enclosed in quotes"
        print "Example:  \"C:\Users\testuser\Documents\test file.txt\""