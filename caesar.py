#!/usr/bin/env python3


ALPHABET_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET_UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encode(msg, shift):
    output = ''
    for char in msg:
        if char in ALPHABET_LOWER:
            for n, c in enumerate(ALPHABET_LOWER):
                if c == char:
                    n = (n + shift) % 26
                    output += ALPHABET_LOWER[n]
        elif char in ALPHABET_UPPER:
            for n, c in enumerate(ALPHABET_UPPER):
                if c == char:
                    n = (n + shift) % 26
                    output += ALPHABET_UPPER[n]
        else:
            output += char
    return output


def decode(msg, shift):
    output = ''
    for char in msg:
        if char in ALPHABET_LOWER:
            for n, c in enumerate(ALPHABET_LOWER):
                if c == char:
                    n = (n - shift) % 26
                    output += ALPHABET_LOWER[n]
        elif char in ALPHABET_UPPER:
            for n, c in enumerate(ALPHABET_UPPER):
                if c == char:
                    n = (n - shift) % 26
                    output += ALPHABET_UPPER[n]
        else:
            output += char
    return output


if __name__ == "__main__":

    print("Welcome to the Caesar Cipher encoder/decoder!")
    print("[E]ncode\n[D]ecode")

    while True:
        method = input("Please enter the method: ").lower()
        if method == 'e' or method == 'd':
            break
        else:
            print("Please enter a valid character!")

    message = input("Please enter the message: ")

    while True:
        shift = input("Please enter the shift amount: ")
        try:
            shift = int(shift)
            break
        except:
            print("Please enter an interger!")

    if method == 'e':
        print(f"Encoded message: {encode(message, shift)}")
    elif method == 'd':
        print(f"Decoded message: {decode(message, shift)}")
