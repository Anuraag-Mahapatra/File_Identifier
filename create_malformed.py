# Creates malformed_jpg.jpg (valid JPEG with broken header)
with open('malformed_jpg.jpg', 'wb') as f:
    f.write(b'\x00\x00\x00')  # BROKEN: Should be FF D8 FF for JPEG
    f.write(b'\xe0\x00\x10JFIF')  # Rest of JPEG header
    f.write(b'\xff\xdb\x00C\x00\x01\x01')  # JPEG data...
    