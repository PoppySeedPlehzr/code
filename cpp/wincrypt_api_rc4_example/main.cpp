// main.cpp

#ifndef _WIN32_WINNT
#define _WIN32_WINNT 0x0400
#endif

#include <tchar.h>
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <wincrypt.h>
#include "crypto.h"

#define RW_SIZE         512
#define BUFFER_SIZE     RW_SIZE * 2

//---------------------------------------------------------------
void DisplayUsage(void)
{
    _tprintf(TEXT("Usage:\n"));
    _tprintf(TEXT("  Encrypt file1 to file2: "));
    _tprintf(TEXT("crypto -e password file1 file2\n"));
    _tprintf(TEXT("  Decrypt file1 to file2: "));
    _tprintf(TEXT("crypto -d password file1 file2\n"));
}

//---------------------------------------------------------------
BOOL myEOF(HANDLE hFile, DWORD dwFileSize)
{
    DWORD dwCurPos = SetFilePointer(hFile, 0, NULL, FILE_CURRENT);
    if (dwCurPos >= dwFileSize) {
        return TRUE;
    } else {
        return FALSE;

    }
}

//---------------------------------------------------------------
int main (int argc, char **argv)
{
    // Validate command line parameters

    if (argc < 5) {
        DisplayUsage();
        return 0;
    }

    BOOL bEncrypt;
    if (lstrcmpi(argv[1], TEXT("-e")) == 0) {
        bEncrypt = TRUE;
    } else if (lstrcmpi(argv[1], TEXT("-d")) == 0) {
        bEncrypt = FALSE;
    } else {
        DisplayUsage();
        return 0;
    }

    // Open the input and output files

    HANDLE hFile1 = CreateFile((LPSTR)argv[3], GENERIC_ALL, 0,
                               NULL, OPEN_EXISTING,
                               FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile1 == INVALID_HANDLE_VALUE) {
        DisplayUsage();
        _tprintf(TEXT("CreateFile %s failed (%x)\n"),
                 (LPSTR)argv[3], GetLastError());
        return 0;
    }

    HANDLE hFile2 = CreateFile((LPTSTR)argv[4], GENERIC_ALL, 0,
                               NULL, CREATE_ALWAYS,
                               FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile2 == INVALID_HANDLE_VALUE) {
        CloseHandle(hFile1);
        DisplayUsage();
        _tprintf(TEXT("CreateFile %s failed (%x)\n"),
                 (LPSTR)argv[4], GetLastError());
        return 0;
    }

    // Allocate buffer to read/write and encrypt.decrypt data

    LPBYTE pBuffer = (LPBYTE)malloc(BUFFER_SIZE);
    if (pBuffer == NULL) {
        CloseHandle(hFile1);
        CloseHandle(hFile2);
        _tprintf(TEXT("malloc failed (%x)\n"), GetLastError());
        return 0;
    }

    DWORD dwBytesW = 0, dwBytes = 0;
    DWORD dwFileSize = GetFileSize(hFile1, NULL);

    // Allocate a CMyCrypto object

    CMyCrypto myCrypto((LPSTR)argv[2], CALG_RC4);

    if (bEncrypt) {

        // Read data from file1, save encrypted data to file2

        while (ReadFile(hFile1, pBuffer, RW_SIZE, &dwBytes, NULL) && dwBytes > 0)
        {
            if (myCrypto.Encrypt(pBuffer, &dwBytes, BUFFER_SIZE, myEOF(hFile1, dwFileSize))) {
                WriteFile(hFile2, pBuffer, dwBytes, &dwBytesW, NULL);
            }
        }

    } else {

        // Read data from file1, save decrypted data to file2

        while (ReadFile(hFile1, pBuffer, RW_SIZE, &dwBytes, NULL)
               && dwBytes > 0) {
            if (myCrypto.Decrypt(pBuffer, &dwBytes,
                                 myEOF(hFile1, dwFileSize))) {
                WriteFile(hFile2, pBuffer, dwBytes, &dwBytesW,
                          NULL);
            }
        }
    }

    free(pBuffer);
    CloseHandle(hFile1);
    CloseHandle(hFile2);
    return 0;
}
