#!/usr/bin/env python3
from encoder import encode_utf8


def main():
    for i in range(0x10ffff + 1):
        try:
            assert encode_utf8(i) == chr(i).encode("utf-8")
        except UnicodeEncodeError:
            # surrogate pairs cannot be encoded with standard library
            print(hex(i), encode_utf8(i))


if __name__ == "__main__":
    main()
