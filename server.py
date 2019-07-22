# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:12:38 2019

@author: 74606
"""

from socket import *
import random


def main():
    sk = socket(AF_INET, SOCK_DGRAM)
    sk.bind(('', 12345))
    while true:
        message, addr = sk.recvfrom(1024)
        message = message.upper()
        rand = random.randint(0, 10)
        if rand < 4:
            continue
        sk.sendto(message, addr)


if __name__ == '__main__':
    main()
