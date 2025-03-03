import sys
import os
import dotenv
import getpass


def my_function():
    pass

def main():
    print(sys.argv)
    username = input("Username: ") 
    password = getpass.getpass('Password: ')
    
    print(f"Username: {username}, Password: {password}")

if __name__ == "__main__":
    print("Running...")
    main()