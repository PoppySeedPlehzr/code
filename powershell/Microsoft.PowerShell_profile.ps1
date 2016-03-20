set-alias vi "C:\Program Files (x86)\Vim\vim74\vim.exe"

set-alias l "ls"

set-alias clearclip "echo off | clip"

set-alias vim "C:\Program Files (x86)\Vim\vim74\vim.exe"

set-alias subl "C:\Program Files\Sublime Text 3\subl.exe"

set-alias notepad "C:\WINDOWS\System32\notepad.exe"

set-alias rdp "C:\WINDOWS\System32\mstsc.exe"

set-alias .. "cd .."

set-alias chrome "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

function whereami
{
	echo Todo!
}

function sign ($filename) {
	$cert = @(gci "cert:\currentuser\My" -codesigning)[0]
	Set-AuthenticodeSignature $filename $cert
}
