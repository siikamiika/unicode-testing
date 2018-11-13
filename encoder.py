#!/usr/bin/env python3
import sys

#                  1       2       3       4
LAST_CODEPOINTS = [0x007f, 0x07ff, 0xffff, 0x10ffff]


def split_codepoint(codepoint):
    tmp = codepoint
    for c in LAST_CODEPOINTS:
        yield tmp & 0o77
        tmp = tmp >> 6
        if codepoint <= c:
            break


def encode_utf8(codepoint):
    if codepoint < 128:
        return codepoint.to_bytes(length=1, byteorder='big')

    parts = list(split_codepoint(codepoint))
    # print([f'{p:06b}' for p in reversed(parts)])
    output = int(2 ** len(parts) - 1) << (8 * len(parts) - len(parts))
    # print(bin(output))

    for i, part in enumerate(parts):
        continuation_marker = 0
        if i < len(parts) - 1:
            continuation_marker = 0b10000000
        part = (continuation_marker + part) << (8 * i)
        # print(f'{part >> (8 * i):08b}')
        output += part

    return output.to_bytes(length=len(parts), byteorder='big')


def main():
    print(encode_utf8(int(sys.argv[1])))


if __name__ == "__main__":
    main()
