#!/usr/bin/env python3

import argparse
from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def encrypt_file(input_file, output_file):
    key = generate_key()
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as file:
        plaintext = file.read()
    encrypted_data = cipher_suite.encrypt(plaintext)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
    print("File encrypted successfully.")
    print("Encryption key:", key.decode())

def decrypt_file(input_file, output_file, key):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
    print("File decrypted successfully.")

def main():
    parser = argparse.ArgumentParser(description="File Encryption and Decryption Tool")
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help="Action to perform: 'encrypt' or 'decrypt'")
    parser.add_argument('input_file', help="Input file path")
    parser.add_argument('--output_file', help="Output file path")

    args = parser.parse_args()

    if args.action == 'encrypt':
        if not os.path.isfile(args.input_file):
            print(f"Error: Input file '{args.input_file}' not found.")
            return
        if not args.output_file:
            print("Error: Output file path required.")
            return
        encrypt_file(args.input_file, args.output_file)
    elif args.action == 'decrypt':
        if not args.output_file:
            print("Error: Output file path required.")
            return
        key = input("Enter encryption key: ").encode()
        decrypt_file(args.input_file, args.output_file, key)

if __name__ == "__main__":
    main()
#test