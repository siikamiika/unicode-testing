#!/usr/bin/env python3
import sys


def encode_utf8(codepoint):
    if codepoint < 128:
        return codepoint.to_bytes(length=1, byteorder="big")

    parts = []
    tmp = codepoint
    #         1       2       3       4
    for c in [0x007f, 0x07ff, 0xffff, 0x10ffff]:
        # add 6 least significant bits to parts
        parts.append(tmp & 0o77)
        # end when byte size is found
        if codepoint <= c:
            break
        # shift 6 bits to the right
        tmp = tmp >> 6
    part_length = len(parts)

    # part length of ones shifted part length bytes left
    output = 2 ** part_length - 1 << 7 * part_length

    first = True
    for i in range(part_length - 1, -1, -1):
        # add continuation marker to the beginning of all but the most significant byte
        if first:
            continuation_marker = 0
            first = False
        else:
            continuation_marker = 0b10000000
        # add part to result
        output += continuation_marker + parts[i] << 8 * i

    return output.to_bytes(length=len(parts), byteorder="big")


def main():
    print(encode_utf8(int(sys.argv[1])))


if __name__ == "__main__":
    main()
