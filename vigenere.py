#!/usr/bin/env python3

import caesar


def keyvalue(key, index):
    for n, c in enumerate(caesar.ALPHABET_LOWER):
        if c == key[index % len(key)]:
            return n


def encode(msg, key):
    output = ''
    counter = 0
    for char in msg:
        if char in caesar.ALPHABET_LOWER:
            for c in caesar.ALPHABET_LOWER:
                if c == char:
                    output += caesar.encode(char, keyvalue(key, counter))
                    counter += 1
        elif char in caesar.ALPHABET_UPPER:
            for c in caesar.ALPHABET_UPPER:
                if c == char:
                    output += caesar.encode(char, keyvalue(key, counter))
                    counter += 1
        else:
            output += char
    return output


def decode(msg, key):
    output = ''
    counter = 0
    for char in msg:
        if char in caesar.ALPHABET_LOWER:
            for c in caesar.ALPHABET_LOWER:
                if c == char:
                    output += caesar.decode(char, keyvalue(key, counter))
                    counter += 1
        elif char in caesar.ALPHABET_UPPER:
            for c in caesar.ALPHABET_UPPER:
                if c == char:
                    output += caesar.decode(char, keyvalue(key, counter))
                    counter += 1
        else:
            output += char
    return output


if __name__ == "__main__":

    print("Welcome to the Vigenere Cipher encoder/decoder!")
    print("[E]ncode\n[D]ecode")

    while True:
        method = input("Please enter the method: ").lower()
        if method == 'e' or method == 'd':
            break
        else:
            print("Please enter a valid character!")

    message = input("Please enter the message: ")

    while True:
        invalid_key = False
        key = input("Please enter the key: ").lower()
        for char in key:
            if char not in caesar.ALPHABET_LOWER:
                invalid_key = True
        if invalid_key == False:
            break
        else:
            print("Please enter a valid key!")

    if method == 'e':
        print(f"Encoded message: {encode(message, key)}")
    elif method == 'd':
        print(f"Decoded message: {decode(message, key)}")
