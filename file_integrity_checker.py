# Python script that calculates the hash of a usig a hash function (like SHA256) and then allows you to verify that hash later to ensure the file has not been modified..
# Here is a basic outline of what our script will do:
# 1. Calculate the hash of a file and save it
# 2. Check if the hash of the file is the same as the saved hash. 
# 3. Report whether the file has been altered or not. 

import hashlib
import os
import datetime

def hash_file(filename):
    """This function returns the SHA-256 hash of the file passed into it."""
    h = hashlib.sha256()
    try:
        with open(filename, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def check_integrity(filename, hash_value):
    """Check the integrity of the file against the provided hash value."""
    # ... [rest of the check_integrity function] ...

def save_hash(filename, hash_value):
    """Save the hash value to a file."""
    # ... [rest of the save_hash function] ...

def main():
    file_to_check = input("Enter the path of the file to check: ")
    calculated_hash = hash_file(file_to_check)
    print(f"The SHA-256 hash of the file is: {calculated_hash}")

    hash_file_name = file_to_check + "_hash.txt"

    # Open the log file to append the results
    with open('integrity_check_log.txt', 'a') as log:
        current_time = datetime.datetime.now()
        log.write(f"{current_time} - Checked {file_to_check}: ")

        if os.path.exists(hash_file_name):
            with open(hash_file_name, 'r') as file:
                saved_hash = file.read()
            if check_integrity(file_to_check, saved_hash):
                print("The file is intact and unmodified.")
                log.write("File is intact and unmodified.\n")
            else:
                print("The file has been altered or corrupted.")
                log.write("File has been altered or corrupted.\n")
        else:
            print("No previously saved hash. Saving the current hash.")
            save_hash(file_to_check, calculated_hash)
            log.write("Saved new hash.\n")

if __name__ == "__main__":
    main()


                       
