#!/usr/bin/env python3
import time

from encoder import encode_utf8


def main():
    # test encoder correctness
    for i in range(0x10ffff + 1):
        try:
            assert encode_utf8(i) == chr(i).encode("utf-8")
        except UnicodeEncodeError:
            # surrogate pairs cannot be encoded with standard library
            print(hex(i), encode_utf8(i))

    # benchmark
    start = time.time()
    for i in range(0x10ffff + 1):
        encode_utf8(i)
    print(f"encode_utf8: {time.time() - start}")
    start = time.time()
    for i in range(0x10ffff + 1):
        try:
            chr(i).encode("utf-8")
        except:
            pass
    print(f"str.encode: {time.time() - start}")


if __name__ == "__main__":
    main()
