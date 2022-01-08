from keystone import *
import numpy

def ConvertToNSO(offset):
    return offset + 0x100

BID = "E9A68278EDF6287D6543DE1B96A69A16"

ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)

file = open("%s.ips" % BID, "wb")
file.write(b"PATCH")

# Change font scale.
# Default is 32
value = 24
if (value != 32):
    value *= 65536
    file.write(ConvertToNSO(0x44580).to_bytes(3, byteorder="big"))
    code = b"mov w1, #0x%x; mov w4, #0x%x" % (value, value)
    encoding, count = ks.asm(code)
    file.write(len(encoding).to_bytes(2, byteorder="big"))
    for i in range(0, len(encoding)):
        file.write(numpy.uint8(encoding[i]))

# Force game to write all glyphs in non-fixed width
file.write(ConvertToNSO(0x44674).to_bytes(3, byteorder="big"))
code = b"b #0x3c"
encoding, count = ks.asm(code)
file.write(len(encoding).to_bytes(2, byteorder="big"))
for i in range(0, len(encoding)):
    file.write(numpy.uint8(encoding[i]))

# Change date formatting in save/load menu
file.write(ConvertToNSO(0xABCAF).to_bytes(3, byteorder="big"))
code = b"%d/%d\n%02d:%02d\x00"
file.write((len(code)).to_bytes(2, byteorder="big"))
file.write(code)

#Change boldness of font
#Default value: 1 << 10
#Max: 100 (%)
#Doesn't work
value = 1 << 10
if (value != (1 << 10)):
    value *= 65536
    file.write(ConvertToNSO(0x44598).to_bytes(3, byteorder="big"))
    code = b"mov w1, #0x%x" % value
    encoding, count = ks.asm(code)
    file.write(len(encoding).to_bytes(2, byteorder="big"))
    for i in range(0, len(encoding)):
        file.write(numpy.uint8(encoding[i]))

#Change outline width of font
#Default value: 2
value = 2
if (value != 2):
    file.write(ConvertToNSO(0x447F8).to_bytes(3, byteorder="big"))
    code = b"mov w1, #0x%x" % value
    encoding, count = ks.asm(code)
    file.write(len(encoding).to_bytes(2, byteorder="big"))
    for i in range(0, len(encoding)):
        file.write(numpy.uint8(encoding[i]))

file.write(b"EOF")
file.close()