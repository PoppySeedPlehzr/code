"""
http://msdn.microsoft.com/en-us/library/windows/desktop/ms685996%28v=vs.85%29.aspx
"""

import win32service
import win32con

service_types = {
  0x1:"0x1\tSERVICE_KERNEL_DRIVER",
  0x2:"0x2\tSERVICE_FILE_SYSTEM_DRIVER",
  0x4:"0x4\tADAPTER_ARGS",
  0x8:"0x8\tFILE_SYSTEM_DRIVER",
  0x10:"0x10\tSERVICE_WIN32_OWN_PROCESS",
  0x20:"0x20\tSERVICE_WIN32_SHARE_PROCESS",
  0x110:"0x110\tWIN32_PROC_SELF",
  0X120:"0x120\tWIN32_PROC_SHARE"
}

service_status = {
  1:"0x1\tSERVICE_STOPPED",
  2:"0x2\tSERVICE_START_PENDING",
  3:"0x3\tSERVICE_STOP_PENDING",
  4:"0x4\tSERVICE_RUNNING",
  5:"0x5\tSERVICE_CONTINUE_PENDING",
  6:"0x6\tSERVICE_PAUSE_PENDING",
  7:"0x7\tSERVICE_PAUSED"
}

accessSCM = win32con.GENERIC_READ
hscm = win32service.OpenSCManager(None, None, accessSCM)
SCMdata = win32service.EnumServicesStatus(hscm)

for sname, sdesc, flags in SCMdata:
  if int(flags[1] == 4):
    print "[+] Service Name: " + sname
    print "[+] Service Desc: " + sdesc
    print "[+] Flags:"
    print "\t" + service_types[int(flags[0])]
    print "\t" + service_status[int(flags[1])]
