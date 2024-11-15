#!/usr/bin/env python2
# --------------------------------------------------------------------------------------------------
# Flare-On 2020: 7 - re crowd
# --------------------------------------------------------------------------------------------------
import struct
import base64
from capstone import *
from unicorn import *
from unicorn.x86_const import *

file_1 = [
                                                                0xa4, 0xb1, 0x03, 0x73, 0x90, 0xe4,
    0xc8, 0x8e, 0x97, 0xb0, 0xc9, 0x5b, 0xc6, 0x30, 0xdc, 0x6a, 0xbd, 0xf4, 0x20, 0x38, 0x86, 0xf9,
    0x30, 0x26, 0xaf, 0xed, 0xd0, 0x88, 0x1b, 0x92, 0x4f, 0xe5, 0x09, 0xcd, 0x5c, 0x2e, 0xf5, 0xe1,
    0x68, 0xf8, 0x08, 0x2b, 0x48, 0xda, 0xf7, 0x59, 0x9a, 0xd4, 0xbb, 0x92, 0x19, 0xae, 0x10, 0x7b,
    0x6e, 0xed, 0x7b, 0x6d, 0xb1, 0x85, 0x4d, 0x10, 0x31, 0xd2, 0x8a, 0x4e, 0x7f, 0x26, 0x8b, 0x10,
    0xfd, 0xf4, 0x1c, 0xc1, 0x7f, 0xab, 0x5a, 0x73, 0x92, 0x02, 0xc0, 0xcb, 0x49, 0xd9, 0x53, 0xd6,
    0xdf, 0x6c, 0x03, 0x81, 0xa0, 0x21, 0x01, 0x6e, 0x87, 0x5f, 0x09, 0xfe, 0x9a, 0x69, 0x94, 0x35,
    0x84, 0x4f, 0x01, 0x96, 0x6e, 0x77, 0xec, 0xa3, 0xf3, 0xf5, 0x2f, 0x6a, 0x36, 0x36, 0xab, 0x47,
    0x75, 0xb5, 0x80, 0xcb, 0x47, 0xbd, 0x9f, 0x76, 0x38, 0xa5, 0x40, 0x48, 0x57, 0x9c, 0x36, 0xad,
    0x8e, 0x79, 0x45, 0xa3, 0x20, 0xfa, 0xed, 0x1f, 0x18, 0x49, 0xb8, 0x89, 0x18, 0x48, 0x2b, 0x5b,
    0x6f, 0xee, 0xf4, 0xc3, 0xd6, 0xdc, 0xcc, 0x84, 0xea, 0xb1, 0x01, 0x09, 0xb1, 0x31, 0x4b, 0xa4,
    0x05, 0x50, 0x98, 0xb0, 0x73, 0xae, 0x9c, 0x14, 0x10, 0x1b, 0x65, 0xbd, 0x93, 0x82, 0x6c, 0x57,
    0xb9, 0x75, 0x7a, 0x2a, 0xee, 0xde, 0x10, 0xfb, 0x39, 0xba, 0x96, 0xd0, 0x36, 0x1f, 0xc2, 0x31,
    0x2c, 0xc5, 0x4f, 0x33, 0xa5, 0x13, 0xe1, 0x59, 0x56, 0x92, 0xc5, 0x1f, 0xa5, 0x4e, 0x0e, 0x62,
    0x6e, 0xdb, 0x5b, 0xe8, 0x7f, 0x8d, 0x01, 0xa6, 0x7d, 0x01, 0x2b, 0x02, 0x43, 0x1f, 0x54, 0xb9,
    0xbc, 0xd5, 0xef, 0x2d, 0xb3, 0xda, 0xef, 0x3d, 0xd0, 0x68, 0xfe, 0xda, 0xde, 0x60, 0xb1, 0x17,
    0xfe, 0xea, 0x20, 0x4a, 0x2c, 0xa1, 0xbb, 0xa1, 0xb5, 0xc5, 0x12, 0x92, 0xa9, 0xdb, 0xf1, 0x11,
    0xe3, 0x8c, 0x58, 0xba, 0xdc, 0x3d, 0x28, 0x86, 0x66, 0xc8, 0x6d, 0x0e, 0xab, 0xfa, 0x83, 0xd5,
    0x24, 0x60, 0x10, 0x68, 0x1d, 0xc7, 0xaf, 0xc7, 0xac, 0x45, 0x13, 0xa3, 0xd9, 0x72, 0xe7, 0xcc,
    0x51, 0x79, 0xf5, 0x67, 0x41, 0x7c, 0xae, 0x7f, 0xc8, 0x7e, 0x95, 0x46, 0x09, 0xf6, 0xef, 0x4b,
    0x45, 0x02, 0x74, 0x52, 0x10, 0x50, 0x1c, 0xb7, 0x6a, 0x7c, 0xeb, 0x00, 0xd7, 0x59, 0xc3, 0x29,
    0x02, 0x37, 0xd0, 0x47, 0x2e, 0x1e, 0x3a, 0xf7, 0xe6, 0xac, 0x82, 0x14, 0x74, 0xeb, 0x4f, 0x6b,
    0x57, 0x22, 0x13, 0xf6, 0xf2, 0x48, 0xd6, 0x6b, 0xcb, 0xb4, 0xed, 0xa7, 0x32, 0x68, 0xcb, 0xd0,
    0x66, 0x42, 0xd3, 0xc5, 0xf2, 0xc5, 0x37, 0xdf, 0x7d, 0x9f, 0x9f, 0x28, 0xc0, 0x74, 0x3a, 0xbe,
    0xb8, 0xc0, 0xa7, 0x73, 0xd0, 0xbb, 0xfa, 0x50, 0x7c, 0x10, 0x1e, 0xda, 0xb1, 0x23, 0xd6, 0xc4,
    0x81, 0xa5, 0xd3, 0xb6, 0x22, 0x29, 0x09, 0x6b, 0x21, 0xa6, 0x5c, 0x38, 0xc6, 0x80, 0x3d, 0xbe,
    0x08, 0x23, 0xc7, 0xb1, 0x1f, 0x6d, 0xe6, 0x64, 0x66, 0x95, 0xdc, 0x10, 0xa7, 0x13, 0x42, 0xcd,
    0x3b, 0xfa, 0xdc, 0xda, 0x14, 0x8d, 0xd0, 0x5a, 0xc8, 0x81, 0x35, 0x54, 0x2f, 0xb5, 0xdc, 0x61,
    0xd6, 0x28, 0x77, 0x88, 0xc5, 0x58, 0x70, 0xb5, 0x2f, 0xcf, 0xea, 0x4f, 0x4d, 0x85, 0x56, 0x04,
    0x07, 0xf3, 0x90, 0x74, 0xce, 0x5d, 0x3c, 0x8a, 0x2b, 0x06, 0xb4, 0x9f, 0xe6, 0x6d, 0x79, 0xc0,
    0x6e, 0x3d, 0xd8, 0x3e, 0x20, 0x08, 0xb7, 0x74, 0x3d, 0x36, 0x99, 0xcd, 0x7f, 0x60, 0x7d, 0x9c,
    0xc9, 0xb3, 0xad, 0x0c, 0x8e, 0x45, 0x6d, 0xea, 0x3d, 0xdd, 0x09, 0x1d, 0xda, 0x0b, 0x3a, 0x1c,
    0xfc, 0xcb, 0x81, 0x48, 0xed, 0x5a, 0xfa, 0xce, 0xf8, 0xc6, 0x23, 0xb0, 0x1e, 0x26, 0x44, 0xa3,
    0xd9, 0xab, 0x0e, 0xd5, 0x98, 0xb1, 0x33, 0x65, 0x5d, 0xed, 0x6a, 0xd3, 0x23, 0x7f, 0x02, 0x4a,
    0xb3, 0xa2, 0xf8, 0x1d, 0x7e, 0xd1, 0x2f, 0x5f, 0xbe, 0x89, 0x61, 0x5e, 0x2c, 0xe4, 0xb8, 0x96,
    0x19, 0xe5, 0x49, 0x76, 0x4e, 0x7a, 0xe8, 0x92, 0xa3, 0x70, 0x55, 0x6f, 0x7d, 0x3c, 0xf9, 0xc1,
    0x36, 0x44, 0x69, 0x33, 0x7d, 0xdf, 0x79, 0x37, 0xb8, 0xe0, 0xaa, 0xe8, 0x6a, 0x5d, 0xc9, 0x3b,
    0x18, 0x0f, 0x4e, 0x28, 0x3a, 0x31, 0xa8, 0x7f, 0xef, 0xb8, 0x19, 0xac, 0x36, 0x63, 0xe8, 0x89,
    0x21, 0x4d, 0x83, 0xa7, 0x7e, 0x57, 0x03, 0x48, 0x9b, 0xe1, 0x27, 0x93, 0x06, 0xe4, 0x3b, 0x67,
    0x5f, 0xe5, 0x69, 0x50, 0x00, 0x3e, 0x8b, 0x01, 0xb7, 0xef, 0xa6, 0xb5, 0x4b, 0x36, 0x82, 0xd4,
    0xfb, 0x9f, 0xde, 0x8b, 0x27, 0xcc, 0xa4, 0x57, 0xce, 0x25, 0x37, 0x44, 0x50, 0x42, 0xf7, 0x7e,
    0xa2, 0xbf, 0x4f, 0xdf, 0x0f, 0x72, 0xd8, 0x66, 0x4a, 0x3e, 0xf5, 0xc8, 0x26, 0x2a, 0xc5, 0x88,
    0x7b, 0x97, 0xab, 0x23, 0x5b, 0x2b, 0x61, 0xd8, 0x3f, 0x00, 0x37, 0x0e, 0x7e, 0x14, 0xfa, 0xfd,
    0x7d, 0xf7, 0x81, 0x49, 0xc2, 0xa1, 0x85, 0x1b, 0xd0, 0x28, 0xbe, 0xa5, 0x24, 0xfd, 0x60, 0xb2,
    0x78, 0x27, 0x4e, 0xac, 0xe8, 0x79, 0x3b, 0x3b, 0x7a, 0xdc, 0x56, 0xd0, 0x76, 0xc5, 0x01, 0x0f,
    0xcf, 0x43, 0xb5, 0xd4, 0x5f, 0x48, 0x70, 0xbd, 0xac, 0x65, 0x76, 0xdb, 0x11, 0x3b, 0x5b, 0xcf,
    0x9c, 0x52, 0x8b, 0x00, 0x1e, 0x83, 0xf1, 0xfa, 0x92, 0x5b, 0x77, 0x79, 0x07, 0x6a, 0xe0, 0xd4,
    0x33, 0x9a, 0x71, 0xba, 0x24, 0xa5, 0xa5, 0xc8, 0xeb, 0x4c, 0x01, 0xb3, 0xd3, 0xcd, 0x2c, 0x22,
    0x8c, 0x0b, 0x4c, 0xcd, 0x2d, 0x5a, 0x8c, 0x9a, 0xb1, 0x67, 0x70, 0x7f, 0x75, 0x96, 0xe2, 0x56,
    0xc1, 0x1d, 0xff, 0x05, 0x7e, 0x77, 0xa2, 0xba, 0xe5, 0x9a, 0xae, 0xf9, 0xf8, 0xb2, 0xf1, 0x78,
    0xd2, 0xb1, 0xdc, 0xe9, 0x03, 0xc2, 0xd4, 0xff, 0x1f, 0x66, 0xcd, 0xb0, 0x47, 0xf0, 0xb4, 0xd1,
    0xf6, 0x72, 0xfa, 0x1e, 0xb7, 0xf1, 0x4d, 0xe7, 0x6e, 0x42, 0x10, 0xec, 0x5d, 0x94, 0x30, 0xdd,
    0x7f, 0x75, 0x1c, 0x01, 0x45, 0x46, 0xb6, 0x14, 0x6c, 0xf7, 0x45, 0x36, 0x58, 0xec, 0xef, 0xf3,
    0x37, 0x04, 0x9c, 0x21, 0xeb, 0x94, 0x54, 0xa3, 0xfe, 0x23, 0xcb, 0xbb, 0x31, 0x5c, 0x62, 0x75,
    0xbd, 0xed, 0x27, 0x90, 0xfe, 0x91, 0x17, 0xe2, 0xae, 0x42, 0x9b, 0x79, 0x04, 0xd1, 0x5c, 0xef,
    0xcd, 0x4b, 0x86, 0x93, 0x4a, 0x74, 0x41, 0x2d, 0xad, 0x0b, 0x35, 0x1d, 0x81, 0xfd, 0x10, 0x2c,
    0x8e, 0xfd, 0x8c, 0x68, 0x1d, 0xf5, 0x45, 0x0a, 0xb5, 0xb4, 0x09, 0xbe, 0x0e, 0xfa, 0xfa, 0xd2,
    0xf7, 0x4e, 0x58, 0xd8, 0x3c, 0x1a, 0x1b, 0x11, 0x3d, 0x99, 0x25, 0x53, 0xab, 0x78, 0xac, 0x54,
    0x49, 0xbb, 0x2a, 0x42, 0xb3, 0x80, 0x66, 0xb5, 0x63, 0xe2, 0x90, 0xf8, 0xa5, 0x8f, 0x37, 0xaf,
    0x97, 0x13, 0x2b, 0xe8, 0xfc, 0x5d, 0x4b, 0x71, 0x8b, 0x4d, 0x9f, 0xc8, 0xec, 0x07, 0x28, 0x1f,
    0xcb, 0x30, 0x92, 0x1e, 0x6d, 0xdc, 0xb9, 0xde, 0x94, 0xb8, 0xe9, 0xcb, 0x5a, 0xf7, 0xa2, 0xb0,
    0xbb, 0x0f, 0xc3, 0x38, 0xb7, 0x27, 0x33, 0x1b, 0xe9, 0xbf, 0x45, 0x2d, 0x86, 0x3e, 0x34, 0x6d,
    0x12, 0xf6, 0x05, 0x12, 0x27, 0xc5, 0x28, 0xe4, 0xd2, 0x61, 0x26, 0x7e, 0x99, 0x2b, 0x3f, 0x1f,
    0x03, 0x4d, 0x79, 0x72, 0xb9, 0x83, 0x56, 0x6d, 0x8e, 0x82, 0x33, 0xc2, 0x09, 0xeb, 0x21, 0x4a,
    0x0c, 0x13, 0xad, 0xea, 0x29, 0x1b, 0x58, 0xda, 0x10, 0x16, 0x43, 0x20, 0x55, 0x7d, 0xf4, 0xb7,
    0xfc, 0x26, 0x34, 0x68, 0x8b, 0xa0, 0x54, 0xaf, 0x07, 0xd5, 0xd5, 0x23, 0xb5, 0x23, 0xb8, 0xfb,
    0x07, 0xc6, 0x64, 0x4a, 0x56, 0x7f, 0xa0, 0x6d, 0x86, 0x7c, 0x33, 0x3b, 0x23, 0xb7, 0x9d, 0x9c,
    0xa8, 0x22, 0xb1, 0x79, 0x9f, 0x00, 0xe7, 0x76, 0xe9, 0xc7, 0x68, 0xae, 0x5c, 0x23, 0xae, 0x9f,
    0xc6, 0x45, 0x91, 0x48, 0x83, 0x6f, 0xbf, 0x0a, 0xd8, 0xc9, 0x77, 0xab, 0x2c, 0x2d, 0x85, 0x47,
    0xbf, 0xe9, 0x81, 0x80, 0x13, 0xd9, 0xdc, 0x1c, 0x21, 0x0f, 0xf4, 0xc7, 0x79, 0x07, 0x52, 0xa8,
    0x06, 0x8c, 0x57, 0x63, 0x53, 0xb2, 0xfb, 0x7d, 0xbe, 0x6c, 0x1a, 0xae, 0x2e, 0xbd, 0xc6, 0xfd,
    0x97, 0x0a, 0x04, 0xed, 0xc0, 0xa3, 0x05, 0x45, 0xdb, 0x9b, 0x62, 0xbd, 0x34, 0xa9, 0x08, 0x25,
    0x53, 0x00, 0x90, 0x36, 0xcf, 0xd9, 0x63, 0x15, 0xa5, 0xf7, 0xf8, 0xe0, 0xd8, 0x69, 0xfd, 0x79,
    0x24, 0x60, 0x7b, 0xa2, 0xae, 0xbd, 0xf2, 0xb4, 0xb9, 0xc2, 0x08, 0x84, 0x65, 0xa9, 0x6d, 0xeb,
    0xa5, 0xd8, 0x72, 0xa7, 0xb6, 0x59, 0x21, 0xb9, 0xf4, 0x11, 0x12, 0x5d, 0x39, 0x1d, 0x15, 0x75,
    0x6d, 0x8a, 0x2f, 0x58, 0xc2, 0xfc, 0x80, 0x02, 0x51, 0x78, 0xa9, 0xfc, 0x7d, 0xde, 0x0d, 0x85,
    0xa5, 0x57, 0x18, 0xf8, 0xf0, 0xcc, 0x8e, 0x4c, 0x5e, 0xd7, 0x65, 0x58, 0x74, 0x4e, 0x8a, 0x44,
    0x33, 0xa2, 0x24, 0xe3, 0x56, 0x57, 0x68, 0xba, 0xbb, 0xf2, 0xb2, 0x32, 0x98, 0xf1, 0x88, 0x2e,
    0xc3
]

file_2 = [
    0x43, 0x66, 0x57, 0x83, 0xa5, 0x23, 0x89, 0x77, 0xbe, 0xac,
    0x1b, 0x1f, 0x87, 0x8f, 0x58, 0x93, 0x3f, 0x24, 0xcf, 0x2c, 0xd3, 0x9a, 0xa8, 0xd1, 0x11, 0xc4,
    0xbc, 0xa6, 0x7f, 0xcd, 0x38, 0xdb, 0xb3, 0x3c, 0x03, 0x4b, 0xab, 0xf5, 0x60, 0xc5, 0x60, 0xd2,
    0x0d, 0x1d, 0x18, 0x88, 0x41, 0x5b, 0x4f, 0x06, 0x17, 0x6c, 0x9e, 0x0b, 0x01, 0x73, 0x9d, 0x83,
    0x60, 0x18, 0xfa, 0x8b, 0xff, 0xf8, 0x4d, 0x78, 0xb2, 0xa4, 0x24, 0x6f, 0xae, 0xbd, 0x92, 0xd1,
    0xec, 0xcc, 0x2d, 0x7c, 0x8b, 0xbf, 0xd0, 0x8c, 0xbd, 0xe2, 0x45, 0xef, 0x15, 0xb2, 0x88, 0xbc,
    0xa4, 0x59, 0xbe, 0x20, 0xac, 0xf9, 0x57, 0xdf, 0x10, 0xba, 0xbc, 0xd9, 0x11, 0x93, 0x41, 0x19,
    0x00, 0x9c, 0x02, 0x25, 0xef, 0xc4, 0x4a, 0x26, 0xfd, 0x25, 0xca, 0x9b, 0x85, 0x19, 0x64, 0x4e,
    0xc5, 0x84, 0x9f, 0xa1, 0x00, 0x18, 0x2c, 0x68, 0x30, 0xdc, 0x70, 0x4c, 0xfe, 0x83, 0xf1, 0xc7,
    0x00, 0x2b, 0x49, 0x7a, 0x83, 0x09, 0x05, 0x77, 0x6e, 0x0a, 0x08, 0x8d, 0x56, 0xe4, 0x38, 0x7e,
    0x88, 0x0f, 0x2c, 0x41, 0xe4, 0x33, 0x66, 0xc9, 0xbc, 0x06, 0xaa, 0x2a, 0xa1, 0x96, 0x2d, 0x94,
    0xc0, 0x08, 0x16, 0x1e, 0xa4, 0xf2, 0x81, 0x1a, 0x83, 0xf7, 0x7c, 0xb5, 0x7d, 0x63, 0x13, 0x00,
    0x41, 0x96, 0xca, 0x69, 0x80, 0xae, 0x49, 0xe9, 0x5d, 0x0f, 0x7d, 0x89, 0x43, 0xd4, 0x89, 0x1a,
    0x01, 0xb4, 0x61, 0x61                                                                        
]                                                                                              


# --------------------------------------------------------------------------------------------------
# RC4 Implementation (copied from: https://github.com/bozhu/RC4-Python/blob/master/rc4.py)
def KSA(key):
    keylength = len(key)
    S = range(256)
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)


# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print '[+] Flare-On 2020: 7 - re crowd'

    # Step 1: Decrypt handle.
    print '[+] Decrypting the first 4 bytes ...'
    key = 'KXOR'
    for b, k in zip([0x9c, 0x5c, 0x4f, 0x52], key):
        print '[+]\t 0x%02X' % (b ^ ord(k))

    # Step 2: Decrypt the first file.
    print '[+] Decrypting the first file ...'
    key = '6B696C6C657276756C74757265313233'.decode('hex')
    print '[+] RC4 key: %s' % key
    key = [ord(k) for k in key]

    keystream = RC4(key)
    plain = ''.join(chr(b ^ keystream.next()) for b in file_1)
    print '='*100
    print plain
    print '='*100

    # Step 3: Decrypt the second file.
    print '[+] Decrypting C:\\accounts.txt ...'

    key = 'intrepidmango'
    print '[+] RC4 key: %s' % key
    key = [ord(k) for k in key]

    keystream = RC4(key)
    plain = ''.join(chr(b ^ keystream.next()) for b in file_2)
    print '='*100
    print plain
    print '='*100

# --------------------------------------------------------------------------------------------------
