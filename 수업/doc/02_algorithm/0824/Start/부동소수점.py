import struct
a = 149.625
bits, = struct.unpack('I', struct.pack('f', a))
print(f'{bits:032b}')