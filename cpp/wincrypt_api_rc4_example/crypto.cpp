#ifndef _WIN32_WINNT
#define _WIN32_WINNT 0x0400
#endif

#include <windows.h>
#include <wincrypt.h>
#include "crypto.h"

//---------------------------------------------------------------
CMyCrypto::CMyCrypto(LPTSTR pszPassword, ALG_ID algorithm)
{
    m_hProv = NULL;
    m_hKey  = NULL;

    // Get handle to the default key container in default CSP
    if (CryptAcquireContext(&m_hProv,     // handle to CSP
                            NULL,         // default container
                            MS_DEF_PROV,  // default CSP
                            PROV_RSA_FULL,// provider type
                            0)) {         // action

        HCRYPTHASH hHash;

        // Get handle to hash object
        if (CryptCreateHash(m_hProv,   // handle to CSP
                            CALG_MD5,  // hashing algorithm
                            0,         // non-keyed hash
                            0,         // reserved, must be zero
                            &hHash)) { // hash object

            // Hash the password
            if (CryptHashData(hHash,   // handle to hash object
                              (LPBYTE)pszPassword, // data buffer
                              lstrlen(pszPassword)*sizeof(TCHAR),
                              0)) {    // flags

                // Create the session key using the hashed password
                CryptDeriveKey(m_hProv,   // handle to CSP
                               algorithm, // encryption algorithm
                               hHash,     // hashed data
                               CRYPT_EXPORTABLE | 0x00280000,
                               &m_hKey);  // session key
            }
            CryptDestroyHash(hHash);
        }
    }
}

//---------------------------------------------------------------
CMyCrypto::~CMyCrypto()
{
    if (m_hKey != NULL) {
        CryptDestroyKey(m_hKey);
    }
    if (m_hProv != NULL) {
        CryptReleaseContext(m_hProv, 0);
    }
}

//---------------------------------------------------------------
BOOL CMyCrypto::Encrypt(LPBYTE pData, LPDWORD pdwDataSize,
                        DWORD dwBufferSize, BOOL bFinal)
{
    return CryptEncrypt(m_hKey,        // encryption key handle
                        0,             // optional hash handle
                        bFinal,        // true if last block
                        0,             // flag (reserved)
                        pData,         // data to encrypt
                        pdwDataSize,   // data size (in bytes)
                        dwBufferSize); // buffer size (in bytes)
}

//---------------------------------------------------------------
BOOL CMyCrypto::Decrypt(LPBYTE pData, LPDWORD pdwDataSize,
                        BOOL bFinal)
{
    return CryptDecrypt(m_hKey,        // encryption key handle
                        0,             // optional hash handle
                        bFinal,        // true if last block
                        0,             // flag (reserved)
                        pData,         // data to encrypt
                        pdwDataSize);  // data size (in bytes)
}
