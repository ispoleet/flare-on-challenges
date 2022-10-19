#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------
# FLARE-ON 2021: 10 - Wizardcult
# ----------------------------------------------------------------------------------------

# Since we know the first 8 bytes of the PNG header, we can test the encryption.
Input = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]    
Output = []

ROM0 = [
    90, 132, 6, 69, 174, 203, 232, 243, 87, 254, 166, 61, 94, 65, 8, 208, 51,
    34, 33, 129, 32, 221, 0, 160, 35, 175, 113, 4, 139, 245, 24, 29, 225, 15,
    101, 9, 206, 66, 120, 62, 195, 55, 202, 143, 100, 50, 224, 172, 222, 145,
    124, 42, 192, 7, 244, 149, 159, 64, 83, 229, 103, 182, 122, 82, 78, 63, 131,
    75, 201, 130, 114, 46, 118, 28, 241, 30, 204, 183, 215, 199, 138, 16, 121,
    26, 77, 25, 53, 22, 125, 67, 43, 205, 134, 171, 68, 146, 212, 14, 152, 20
]

ROM1 = [
    185, 155, 167, 36, 27, 60, 226, 58, 211, 240, 253, 79, 119, 209, 163, 12,
    72, 128, 106, 218, 189, 216, 71, 91, 250, 150, 11, 236, 207, 73, 217, 17,
    127, 177, 39, 231, 197, 178, 99, 230, 40, 54, 179, 93, 251, 220, 168, 112,
    37, 246, 176, 156, 165, 95, 184, 57, 228, 133, 169, 252, 19, 2, 81, 48, 242,
    105, 255, 116, 191, 89, 181, 70, 23, 194, 88, 97, 153, 235, 164, 158, 137,
    238, 108, 239, 162, 144, 115, 140, 84, 188, 109, 219, 44, 214, 227, 161,
    141, 80, 247, 52
]

ROM2 = [
    213, 249, 1, 123, 142, 190, 104, 107, 85, 157, 45, 237, 47, 147, 21, 31,
    196, 136, 170, 248, 13, 92, 234, 86, 3, 193, 154, 56, 5, 111, 98, 74, 18,
    223, 96, 148, 41, 117, 126, 173, 233, 10, 49, 180, 187, 186, 135, 59, 38,
    210, 110, 102, 200, 76, 151, 198
]

ROM3 = 'a11_mY_hom1es_h4t3_b4rds'

i_3 = 0
i = 0


# ----------------------------------------------------------------------------------------
def get_Input():
  global Input, i
  b = Input[i]
  i += 1  
  return b

# ----------------------------------------------------------------------------------------
def get_ROM0():
  global ROM0, i_0
  b = ROM0[i_0]
  i_0 += 1
  return b

# ----------------------------------------------------------------------------------------
def CPU0():
    Acc = get_Input()
    # There's code get executed between get & set!
    b = CPU1(Acc)
    Output.append(b)

# ----------------------------------------------------------------------------------------
def CPU1(cpu0_r2):
  b = CPU2(cpu0_r2)
  c = CPU5(b)
  Dat = CPU2(c)

  if Dat & 128 == 128:
    Dat ^= 66

  return Dat ^ 0xFF

# ----------------------------------------------------------------------------------------
def CPU2(cpu1_r1):
  Acc = cpu1_r1

  if Acc > 99:
    ret = CPU3(Acc)
  else:
    ret = ROM0[Acc]

  return ret

# ----------------------------------------------------------------------------------------
def CPU3(cpu2_r3):
  Acc = cpu2_r3
  if Acc > 199:    
    ret = CPU4(Acc)
  else:    
    ret = ROM1[Acc - 100]

  return ret

# ----------------------------------------------------------------------------------------
def CPU4(cpu3_r3): 
  Acc = cpu3_r3
  ret  = ROM2[Acc - 200]
  
  return ret

# ----------------------------------------------------------------------------------------
def CPU5(cpu1_r2):
  global i_3

  Acc = ord(ROM3[i_3])
  
  if i_3 & 1 == 1:
    Acc ^= 0xFF
  
  i_3 += 1
  if i_3 == len(ROM3):
    i_3 = 0    

  Acc ^= cpu1_r2

  return Acc

# ----------------------------------------------------------------------------------------
def compact():
  Output = []
  i_3 = 0

  for inp in Input:
    if inp > 99:
      if inp > 199:    
        b = ROM2[inp - 200]
      else:    
        b = ROM1[inp - 100]
    else:
      b = ROM0[inp]
       
    Acc = ord(ROM3[i_3])
    if i_3 & 1 == 1:
      Acc ^= 0xFF 

    i_3 = i_3+1 if i_3+1 < len(ROM3) else 0
    Acc ^= b

    if Acc > 99:
      if Acc > 199:    
        Dat = ROM2[Acc - 200]
      else:    
        Dat = ROM1[Acc - 100]
    else:
      Dat = ROM0[Acc]
    
    if Dat & 128 == 128:
      Dat ^= 66
    b = Dat ^ 0xFF

    Output.append(b)

  print('Compact:', ' '.join('%02X' % x for x in Output))

# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
  print('[+] Wizardcult test started.')
  
  for i in range(len(Input)):
    print('[+] Encrypting: %02X' % Input[i])
    CPU0()

  print('Output: ', ' '.join('%02X' % x for x in Output))
  print('Expect: ', '50 74 9D 0E 9B A5 5D 2C F8')

  compact()

# ----------------------------------------------------------------------------------------