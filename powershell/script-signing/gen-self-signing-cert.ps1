makecert -n "CN=PowerShell CA" -eku 1.3.6.1.5.5.7.3.3 -r -sv PowerShellCA.pvk PowerShellCA.cer -ss Root -a sha256
makecert -n "CN=PowerShell Certificate" -eku 1.3.6.1.5.5.7.3.3 -pe -iv PowerShellCA.pvk -ic PowerShellCA.cer -ss My -a sha256
ci 'Cert:\CurrentUser\Powershell Cert Store\' -codesigning
