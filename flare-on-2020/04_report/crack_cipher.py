#!/usr/bin/env python2
# --------------------------------------------------------------------------------------------------
# Flare-On 2020: 4 - Report 
# --------------------------------------------------------------------------------------------------
import magic



# --------------------------------------------------------------------------------------------------
def decrypt(cipher, offset, size, key=None):
    if not key:
        key = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee]
    plain = ''
    it = 0

    # Split ciphertext into groups of 4. Use only 2 bytes for decryption.
    for grp in [cipher[i:i+4] for i in range(0, len(cipher), 4)]:
        plain += chr(int(grp[offset:offset+2], 16) ^ key[it % len(key)])
        it += 1
        if it == size: break

    return plain


# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print '[+] Flare-On 2020: 4 - Report'

    # --------------------------------------------------------------------------
    # Decrypt the first blob (stomp.mp3).
    # --------------------------------------------------------------------------
    print "[+] Decrypting 1st blob ('stomp.mp3') ..."
    plain = decrypt(encr_buf, 0, 168667)
    filetype = magic.from_buffer(plain)

    print '[+] First 32 bytes: %s' % repr(plain[:32])
    print '[+] Filetype: %s' % filetype
    print "[+] Writing blob into 'stomp.mp3' ..."

    with open('stomp.mp3', 'w') as fp:
        fp.write(plain)

    # --------------------------------------------------------------------------
    # Second blob is a PNG file. Find the key.
    # --------------------------------------------------------------------------
    print "[+] Finding the decryption key ..."

    # Get the first 8 ciphertext bytes using a NULL key.
    plain = decrypt(encr_buf, 2, 8, key=[0]*8)

    png_header = [137, 80, 78, 71, 13, 10, 26, 10]
    key = []
    for i in range(8):
        key.append(png_header[i] ^ ord(plain[i]))

    print "[+] Decryption key found: ", ' '.join('%02X' % x for x in key)
    print "[+] Key in ASCII: ", ''.join(chr(x) for x in key)

    # --------------------------------------------------------------------------
    # Key is 'NO-ERALF'. Decrypt the image
    # --------------------------------------------------------------------------
    print "[+] Decrypting the image ..."

    plain = decrypt(encr_buf, 2, 168667, key)
    filetype = magic.from_buffer(plain)

    print '[+] First 32 bytes: %s' % repr(plain[:32])
    print '[+] Filetype: %s' % filetype
    print "[+] Writing blob into 'v.png' ..."

    with open('v.png', 'w') as fp:
        fp.write(plain)

    filetype = magic.from_buffer(plain)
    
# --------------------------------------------------------------------------------------------------
