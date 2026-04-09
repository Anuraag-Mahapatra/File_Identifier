import os
import argparse

SIGNATURES = {
    'JPEG': [0xFF, 0xD8, 0xFF],
    'PNG': [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A],
    'PDF': [0x25, 0x50, 0x44, 0x46],  # %PDF
    'ZIP': [0x50, 0x4B, 0x03, 0x04],
    'EXE': [0x4D, 0x5A],  # MZ
    'GIF': [0x47, 0x49, 0x46, 0x38],  # GIF8
}


def identify_file(filename):
    if not os.path.exists(filename):
        return "File not Found",None
    
    with open(filename, "rb") as f:
        firstBytes = f.read(16)
        if not firstBytes:
            return "Empty File",None
    
    for filetype,sig in SIGNATURES.items():
        if firstBytes[:len(sig)] == bytes(sig):
            return filetype,firstBytes
    return "Unknown",firstBytes

def main():
    parser = argparse.ArgumentParser(description="File Identifier")
    parser.add_argument("files", nargs='+', help="List of files to check")
    parser.add_argument("-v","--verbose", action="store_true", help="Verbose")
    
    args = parser.parse_args()
    for file in args.files:
        result,firstBytes = identify_file(file)
        print(result)
        if args.verbose and firstBytes:
            header_hex = firstBytes.hex()
            print(f"Header: {header_hex[:32]}...")
        print()

if __name__=="__main__":
    main()