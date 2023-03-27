import os
import pathlib
from cryptography.fernet import Fernet



secret_key:str = "#######################"

def encrypt_dir(input_dir, output_dir):
    # get key
    key = secret_key

    # create Fernet object with key
    fer = Fernet(key)

    # folder to be encrypted
    input_dir = pathlib.Path(input_dir)
    # encrypted folder
    output_dir = pathlib.Path(output_dir)
    # create output dir if does not exist
    output_dir.mkdir(exist_ok=True, parents=True)

    # iterate over input dir and encrypt content
    for path in input_dir.glob("*"):
        _path_bytes = path.read_bytes()
        data = fer.encrypt(_path_bytes)
        rel_path = path.relative_to(input_dir)
        dest_path = output_dir / rel_path
        #write encrypted data to ouput dir
        dest_path.write_bytes(data)

def decrypt_dir(input_dir, output_dir):
    
    key = secret_key

    fer = Fernet(key)
    
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    # iterate over input dir and decrypt content
    for path in input_dir.glob("*"):
        _path_bytes = path.read_bytes()
        data = fer.decrypt(_path_bytes)
        rel_path = path.relative_to(input_dir)
        dest_path = output_dir / rel_path
        #write decrypted data to ouput dir
        dest_path.write_bytes(data)
