import os, sys, time, shutil, stat

def backup_files(files):
    for file in files:
        if not os.path.exists(os.getcwd() + "\\backups\\" + os.path.basename(file)):
            shutil.copy2(file, os.getcwd() + "\\backups\\" + os.path.basename(file))
            os.chmod(os.getcwd() + "\\backups\\" + os.path.basename(file), stat.S_IREAD)
            
def file_mon(dirs):
    fmod_times = {}

    for d in dirs:
        if not os.path.exists(d):
            print "File does not exist: " + d
            sys.exit()
        fmod_times[os.path.basename(d)] = os.stat(d).st_mtime
        
    if not os.path.exists(os.getcwd() + "\\backups"):
        os.makedirs(os.getcwd() + "\\backups")
    backup_files(dirs)
    
    while(True):
        for d in dirs:
            if(fmod_times[os.path.basename(d)] != os.stat(d).st_mtime):
                print os.path.basename(d) + " was modified!  Restoring from backup!"
                shutil.copy2(os.getcwd() + "\\backups\\" + os.path.basename(d), d)
                os.chmod(d, stat.S_IWRITE)
        print "All is well.  Sleeping."    
        time.sleep(5)
    
if __name__ == '__main__':
    dirs = []
    if(len(sys.argv) > 1):
        for i in range(1,len(sys.argv)):
            dirs.append(sys.argv[i])
            print "File added: " + sys.argv[i]
        file_mon(dirs)