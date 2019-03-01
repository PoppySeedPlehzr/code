#!/usr/bin/env python3

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(process)d][%(name)s][%(asctime)s]: %(message)s',
    datefmt='%m-%d-%Y %H:%M'
)
logger = logging.getLogger(__name__)


class RC4(object):

    def __init__(self, key: str=None):
        self.key: list = [ord(x) for x in key]
        self.sbox: list = list(range(256))
        self.init_sbox()

    def init_sbox(self):
        j: int = 0
        for i in range(256):
            j = (j + self.sbox[i] + self.key[i % len(self.key)]) % 256
            self.sbox[i], self.sbox[j] = self.sbox[j], self.sbox[i]
        logger.info("S-box has been initialized")

    def encrypt(self, clear: str) -> str:
        i: int = 0
        j: int = 0
        enc: str = ''
        for c in clear:
            i = (i + 1) % 256
            j = (j + self.sbox[i]) % 256
            self.sbox[i], self.sbox[j] = self.sbox[j], self.sbox[i]
            enc += chr(ord(c) ^ self.sbox[(self.sbox[i] + self.sbox[j]) % 256])
        return enc

    def decrypt(self, encrypted: str) -> str:
        return self.encrypt(encrypted)





