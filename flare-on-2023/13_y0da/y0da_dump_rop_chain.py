#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------
# Flare-On 2023: 13 - y0da
# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    print('[+] y0da ROP chain extractor started.')
    print('[+] Please make sure execution has stopped at 0x0180012E72')

    rop_start = idc.get_reg_value('rsp')
    # .text:00000001800115E4         mov     eax, [rsp+38h+var_14]
    rop_end   = 0x167DED8
    print(f'[+] ROP start in stack: {rop_start:08X}')
    print(f'[+] ROP end   in stack: {rop_end:08X}')

    rop_prog = b''
    for stack_addr in range(rop_start, rop_end, 8):
      insn_addr = ida_bytes.get_qword(stack_addr)
      asm = idc.generate_disasm_line(insn_addr, flags=GENDSM_FORCE_CODE)

      insn = idaapi.insn_t()
      length = idaapi.decode_insn(insn, insn_addr)
      print(f'[+] ROP instruction at: {insn_addr:08X}: {asm} ({length} bytes)')

      rop_prog += ida_bytes.get_bytes(insn_addr, length)

    rop_prog += b'\xC3'  # finish with a return instruction, so IDA will know where the function ends

    for i, p in enumerate(rop_prog):
      ida_bytes.patch_byte(0x19F0000 + i, p)


    print('[+] Program finished. Bye bye :)')
# ----------------------------------------------------------------------------------------
'''
[+] y0da ROP chain extractor started.
[+] Please make sure execution has stopped at 0x0180012E72
[+] ROP start in stack: 0167CD98
[+] ROP end   in stack: 0167DED8
[+] ROP instruction at: 019F0060: mov     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F006C: mov     rcx, [rbp+40h] (4 bytes)
[+] ROP instruction at: 019F007B: movzx   eax, byte ptr [rcx+rax] (4 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009F: sar     eax, 3 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BA: shl     ecx, 5 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0000: add     eax, 0ACh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0104: sub     eax, 4 (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009F: sar     eax, 3 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BA: shl     ecx, 5 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009B: sar     eax, 2 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BE: shl     ecx, 6 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00A7: sar     eax, 6 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00B2: shl     ecx, 2 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0153: xor     eax, 0Dh (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F001E: add     eax, 7Bh ; '{' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F013B: xor     eax, 0BFh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00D2: sub     eax, 0C3h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0016: add     eax, 60h ; '`' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00A3: sar     eax, 5 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00B6: shl     ecx, 3 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00F0: sub     eax, 18h (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00E4: sub     eax, 0F3h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009B: sar     eax, 2 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BE: shl     ecx, 6 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00D8: sub     eax, 0C5h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AB: sar     eax, 7 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AF: shl     ecx, 1 (2 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00EA: sub     eax, 0FFh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AB: sar     eax, 7 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AF: shl     ecx, 1 (2 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F017F: xor     eax, 8Fh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F001A: add     eax, 70h ; 'p' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0100: sub     eax, 36h ; '6' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009B: sar     eax, 2 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BE: shl     ecx, 6 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F000C: add     eax, 0E8h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F010C: sub     eax, 56h ; 'V' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00A7: sar     eax, 6 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00B2: shl     ecx, 2 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00A3: sar     eax, 5 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00B6: shl     ecx, 3 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0173: xor     eax, 40h ; '@' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0120: sub     eax, 9Ah (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0163: xor     eax, 16h (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0114: sub     eax, 81h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00CC: sub     eax, 0B2h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009B: sar     eax, 2 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BE: shl     ecx, 6 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F011A: sub     eax, 90h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00FC: sub     eax, 28h ; '(' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009B: sar     eax, 2 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BE: shl     ecx, 6 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00DE: sub     eax, 0DCh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AB: sar     eax, 7 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AF: shl     ecx, 1 (2 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F017B: xor     eax, 7Ch ; '|' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009B: sar     eax, 2 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BE: shl     ecx, 6 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0028: add     eax, 96h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F012F: xor     eax, 0A3h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00A7: sar     eax, 6 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00B2: shl     ecx, 2 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F014D: xor     eax, 0CBh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00F4: sub     eax, 1Ah (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0135: xor     eax, 0B6h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00C6: sub     eax, 0B1h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0157: xor     eax, 0E1h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0022: add     eax, 8Fh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0098: sar     eax, 1 (2 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00C2: shl     ecx, 7 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0012: add     eax, 5Ah ; 'Z' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0177: xor     eax, 78h ; 'x' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F015D: xor     eax, 0EBh (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F016F: xor     eax, 25h ; '%' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AB: sar     eax, 7 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AF: shl     ecx, 1 (2 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0147: xor     eax, 0C9h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F009F: sar     eax, 3 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00BA: shl     ecx, 5 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0108: sub     eax, 49h ; 'I' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00F8: sub     eax, 1Eh (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00A3: sar     eax, 5 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00B6: shl     ecx, 3 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0167: xor     eax, 20h ; ' ' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F016B: xor     eax, 22h ; '"' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0110: sub     eax, 58h ; 'X' (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00A7: sar     eax, 6 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00B2: shl     ecx, 2 (3 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0006: add     eax, 0E4h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0185: xor     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0141: xor     eax, 0C2h (5 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0126: sub     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F002E: add     eax, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0092: not     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F008F: neg     eax (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AB: sar     eax, 7 (3 bytes)
[+] ROP instruction at: 019F008A: movzx   ecx, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F00AF: shl     ecx, 1 (2 bytes)
[+] ROP instruction at: 019F0095: or      eax, ecx (2 bytes)
[+] ROP instruction at: 019F004B: mov     [rbp+20h], al (3 bytes)
[+] ROP instruction at: 019F0080: movzx   eax, byte ptr [rbp+20h] (4 bytes)
[+] ROP instruction at: 019F0068: mov     ecx, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F0076: mov     rdx, [rbp+50h] (4 bytes)
[+] ROP instruction at: 019F0085: movzx   ecx, byte ptr [rdx+rcx] (4 bytes)
[+] ROP instruction at: 019F018C: xor     eax, ecx (2 bytes)
[+] ROP instruction at: 019F0068: mov     ecx, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F018F: inc     ecx (2 bytes)
[+] ROP instruction at: 019F0192: mov     ecx, ecx (2 bytes)
[+] ROP instruction at: 019F0076: mov     rdx, [rbp+50h] (4 bytes)
[+] ROP instruction at: 019F0085: movzx   ecx, byte ptr [rdx+rcx] (4 bytes)
[+] ROP instruction at: 019F00AF: shl     ecx, 1 (2 bytes)
[+] ROP instruction at: 019F0195: and     ecx, 0FFh (6 bytes)
[+] ROP instruction at: 019F019C: mov     edx, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F01A0: add     edx, 2 (3 bytes)
[+] ROP instruction at: 019F01A4: mov     edx, edx (2 bytes)
[+] ROP instruction at: 019F01A7: mov     r8, [rbp+50h] (4 bytes)
[+] ROP instruction at: 019F01AC: movzx   edx, byte ptr [r8+rdx] (5 bytes)
[+] ROP instruction at: 019F01B2: sar     edx, 1 (2 bytes)
[+] ROP instruction at: 019F01B5: and     edx, 0FFh (6 bytes)
[+] ROP instruction at: 019F01BC: and     ecx, edx (2 bytes)
[+] ROP instruction at: 019F018C: xor     eax, ecx (2 bytes)
[+] ROP instruction at: 019F0068: mov     ecx, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F01BF: add     ecx, 3 (3 bytes)
[+] ROP instruction at: 019F0192: mov     ecx, ecx (2 bytes)
[+] ROP instruction at: 019F0076: mov     rdx, [rbp+50h] (4 bytes)
[+] ROP instruction at: 019F0085: movzx   ecx, byte ptr [rdx+rcx] (4 bytes)
[+] ROP instruction at: 019F00B2: shl     ecx, 2 (3 bytes)
[+] ROP instruction at: 019F0195: and     ecx, 0FFh (6 bytes)
[+] ROP instruction at: 019F018C: xor     eax, ecx (2 bytes)
[+] ROP instruction at: 019F0068: mov     ecx, [rbp+24h] (3 bytes)
[+] ROP instruction at: 019F0071: mov     rdx, [rbp+40h] (4 bytes)
[+] ROP instruction at: 019F003E: mov     [rdx+rcx], al (3 bytes)
[+] Program finished. Bye bye :)
'''
# ----------------------------------------------------------------------------------------