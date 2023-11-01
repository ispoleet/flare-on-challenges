#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------
# Flare-On 2023: 04 - Aim Bot
# ----------------------------------------------------------------------------------------
import zlib


# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    print('[+] Aimbot crack started.')

    """
    hexdump -C '/home/ispo/.wine/drive_c/Program Files (x86)/Sauerbraten/packages/base/spcr2.cfg' 
        00000000  6d 61 70 73 6f 75 6e 64  20 61 6d 62 69 65 6e 63  |mapsound ambienc|
        00000010  65 2f 66 6f 72 65 73 74  31 2e 6f 67 67 20 32 35  |e/forest1.ogg 25|
        00000020  35 0d 0a 6d 61 70 73 6f  75 6e 64 20 61 6d 62 69  |5..mapsound ambi|
        00000030  65 6e 63 65 2f 68 75 6d  2e 6f 67 67 0d 0a 6d 61  |ence/hum.ogg..ma|
        00000040  70 73 6f 75 6e 64 20 6b  61 69 73 65 72 2f 66 78  |psound kaiser/fx|
        00000050  2f 63 6f 6d 70 75 74 65  72 31 2e 77 61 76 0d 0a  |/computer1.wav..|
        00000060  6d 61 70 73 6f 75 6e 64  20 6b 61 69 73 65 72 2f  |mapsound kaiser/|
    """
    str_2_dword = lambda s: ord(s[0]) | (ord(s[1]) << 8) | (ord(s[2]) << 16) | (ord(s[3]) << 24)
    
    # If we do know exactly how spcr.cfg starts, we can iterate over 
    # `first_line_of_spcr.cfgs` that contains the first line of various configs.
    #
    # We can check which one makes sense:
    #    [+] Flag: 'computer.xw{6jpmcFg|a....' using cfg byte: 'texturereset\n'
    #    [+] Flag: 'computer.ass1sted_ctf....' using cfg byte: 'mapsound soundsn'
    #    [+] Flag: 'computer.j}dbxzr7Tmc5....' using cfg byte: 'fog 768\n'
    #    [+] Flag: 'computer.j}dbxzr7Tmc5....' using cfg byte: 'fog 1500\n'
    #
    # So the correct one is `mapsound`
    for cfg_1st_4 in open('first_line_of_spcr.cfgs', 'r').readlines():
        if len(cfg_1st_4) < 4:
            continue
        
        cfg_1st_4 = 'mapsound'

        flag = [ord(c) for c in 'computer'] + [ord('.')]*(25 - 8)
        pt4 = str_2_dword(cfg_1st_4[:4])
        flag[9] = (pt4 ^ 0xC) & 0xFF
        flag[10] = ((pt4 ^ 0x120C) & 0xFF00) >> 8
        flag[11] = ((pt4 ^ 0x4203120C) & 0xFF0000) >> 16
        flag[12] = ((pt4 ^ 0x4203120C) & 0xFF000000) >> 24
        flag[13] = 0

        pt5 = pt4 ^ 0x1715151E;
        flag[13] = pt5 & 0xFF
        flag[14] = (pt5 >> 8) & 0xFF
        flag[15] = (pt5 >> 16) & 0xFF
        flag[16] = (pt5 >> 24) & 0xFF

        pt5 = pt4 ^ 0x15040232
        flag[17] = pt5 & 0xFF
        flag[18] = (pt5 >> 8) & 0xFF
        flag[19] = (pt5 >> 16) & 0xFF
        flag[20] = (pt5 >> 24) & 0xFF

        flag = ''.join(chr(x) for x in flag[:])
        print(f'[+] Flag: {repr(flag)} using cfg bytes: {repr(cfg_1st_4[:16])}')
        
        break

    flag = 'computer.ass1sted_ctf...@'
    print('[+] Brute forcing the remaining 4 characters ...')

    for a in range(0x21, 0x7e):
        print(f'[+] Brute forcing {chr(a)} ...')
        for b in range(0x21, 0x7e):
            for c in range(0x21, 0x7e):
                for d in range(0x21, 0x7e):
                    flag = f'computer{chr(a)}ass1sted_ctf{chr(b)}{chr(c)}{chr(d)}@'

                    chksum = zlib.crc32(flag.encode('utf-8'))
                    if chksum == 0xA5561586:
                        print(f'[+] Flag FOUND: {flag}flare-on.com (CRC32: {chksum:08X}h)')
                        exit()

    print('[+] Program finished. Bye bye :)')

# ----------------------------------------------------------------------------------------
r'''
ispo@ispo-glaptop2:~/ctf/flare-on-challenges/flare-on-2023/04_aimbot$ time ./aimbot_crack.py 
[+] Aimbot crack started.
[+] Flag: 'computer.ass1sted_ctf....' using cfg bytes: 'mapsound'
[+] Brute forcing the remaining 4 characters ...
[+] Brute forcing ! ...
[+] Brute forcing " ...
[+] Brute forcing # ...
[+] Brute forcing $ ...
[+] Brute forcing % ...
[+] Brute forcing & ...
[+] Brute forcing ' ...
[+] Brute forcing ( ...
[+] Brute forcing ) ...
[+] Brute forcing * ...
[+] Brute forcing + ...
[+] Brute forcing , ...
[+] Brute forcing - ...
[+] Brute forcing . ...
[+] Brute forcing / ...
[+] Brute forcing 0 ...
[+] Brute forcing 1 ...
[+] Brute forcing 2 ...
[+] Brute forcing 3 ...
[+] Brute forcing 4 ...
[+] Brute forcing 5 ...
[+] Brute forcing 6 ...
[+] Brute forcing 7 ...
[+] Brute forcing 8 ...
[+] Brute forcing 9 ...
[+] Brute forcing : ...
[+] Brute forcing ; ...
[+] Brute forcing < ...
[+] Brute forcing = ...
[+] Brute forcing > ...
[+] Brute forcing ? ...
[+] Brute forcing @ ...
[+] Brute forcing A ...
[+] Brute forcing B ...
[+] Brute forcing C ...
[+] Brute forcing D ...
[+] Brute forcing E ...
[+] Brute forcing F ...
[+] Brute forcing G ...
[+] Brute forcing H ...
[+] Brute forcing I ...
[+] Brute forcing J ...
[+] Brute forcing K ...
[+] Brute forcing L ...
[+] Brute forcing M ...
[+] Brute forcing N ...
[+] Brute forcing O ...
[+] Brute forcing P ...
[+] Brute forcing Q ...
[+] Brute forcing R ...
[+] Brute forcing S ...
[+] Brute forcing T ...
[+] Brute forcing U ...
[+] Brute forcing V ...
[+] Brute forcing W ...
[+] Brute forcing X ...
[+] Brute forcing Y ...
[+] Brute forcing Z ...
[+] Brute forcing [ ...
[+] Brute forcing \ ...
[+] Brute forcing ] ...
[+] Brute forcing ^ ...
[+] Brute forcing _ ...
[+] Flag FOUND: computer_ass1sted_ctfing@flare-on.com (CRC32: A5561586h)

real    0m17.119s
user    0m17.112s
sys 0m0.010s
'''
# ----------------------------------------------------------------------------------------

