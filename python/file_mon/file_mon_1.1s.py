import os, sys, time, shutil, stat, subprocess

def backup_files(files):
    pTime = time.localtime()
    backup_dir = os.getcwd() + "\\backups\\" + str(pTime.tm_hour) + "_" + str(pTime.tm_min) + "_" + str(pTime.tm_sec) + "\\"
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    fperms = {}
    for file in files:
        if not os.path.exists(backup_dir + os.path.basename(file)):
            shutil.copy2(file, backup_dir + os.path.basename(file))

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
            os.chmod(backup_dir + os.path.basename(file), stat.S_IREAD)

    cacls_cmd = "cacls \"" + backup_dir + "\"" + " /T /G %username%:R"
    subprocess.Popen(cacls_cmd, stdin=subprocess.PIPE, shell=True).communicate('Y\r\n')
            
    return backup_dir, fperms
    
def restore_file(file, backup_dir, perm_list):
    shutil.copy2(backup_dir + os.path.basename(file), file)
    cacls_cmd = "cacls \"" + file + "\"" + " /G " + ' '.join(perm_list)
    subprocess.Popen(cacls_cmd, stdin=subprocess.PIPE, shell=True).communicate('Y\r\n')
    

def file_mon(dirs):
    fmod_times = {}

    exit = False
    for d in dirs:
        if not os.path.exists(d):
            print "File does not exist: " + d
            exit = True
        fmod_times[os.path.basename(d)] = os.stat(d).st_mtime
    if exit: sys.exit()
        
    if not os.path.exists(os.getcwd() + "\\backups\\"):
        os.makedirs(os.getcwd() + "\\backups\\")
    backup_dir, fperms = backup_files(dirs)

    while(True):
        for d in dirs:
            if not os.path.exists(d):
                print "File was moved or deleted!  Restoring from backup!"
                restore_file(d, backup_dir, fperms[d])
            else:        
                if(fmod_times[os.path.basename(d)] != os.stat(d).st_mtime):
                    restore_file(d, backup_dir, fperms[os.path.basename(d)])
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