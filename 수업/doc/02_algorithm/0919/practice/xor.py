a = 0x86
key = 0xAA
print(f'{a:d}')
print(f'{a:X}')
print(f'{a:b}')
print(f'{key:b}')
a = a ^ key
print(f'{a:08b}')
print(f'{a:d}')
print(f'{a:X}')
a = a ^ key
print(f'{a:08b}')
print(f'{a:d}')
print(f'{a:X}')
