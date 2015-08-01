
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
using namespace std;


char xor_key;
BYTE flag[] = {"\x24\x2e\x23\x25\x1d\x39\x2e\x72\x2e\x23\x1d\x35\x76\x2c\x36\x31\x1d\x36\x72\x1d\x2c\x72\x2f\x1d\x3b\x71\x30\x1d\x35\x23\x30\x27\x38\x3f\x0"};


/* Decrypt the flag blob */
void decrypt(BYTE* flag){

	for(size_t i = 0; flag[i] != 0x0; i++){
		flag[i] = flag[i] ^ xor_key;
	}
}


int main(){

	xor_key = 0x42;
	DWORD flen = 35;
	DWORD bufflen = MAX_PATH;
	LPSTR buff = (LPSTR)malloc(MAX_PATH); // :P
	BYTE outbuff[MAX_PATH];
	memset(buff, 0x0, sizeof(buff));
	memset(outbuff, 0x0, sizeof(outbuff));

	decrypt(flag);

	cout << "[+] Decrypted Flag - " << flag << endl;


	BOOL ret = CryptBinaryToStringA(flag, flen, CRYPT_STRING_BASE64, buff, &bufflen);

	cout << "[+] CryptBinaryToStringA Returned - " << ret << endl;

	cout << "[+] Base64 Encoded Flag - " << buff << endl;

	ret = CryptStringToBinaryA(buff, flen, CRYPT_STRING_BINARY, outbuff, &bufflen, NULL, NULL);

	cout << "[+] CryptStringToBinaryA Returned - " << ret << endl;

	cout << "[+] Base64 Decoded Flag - " << outbuff << endl;


	return 0;
}