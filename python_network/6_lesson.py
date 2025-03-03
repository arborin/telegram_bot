import sys
import os
import dotenv
import getpass


def getOsEnv():
    print(os.environ)
    
def getEnvFile():
    # LOAD .env file in enviroment
    dotenv.load_dotenv(verbose=True)
    
    # READ ENV VARIABLE
    print(os.getenv('RED_PASSWORD'))

def main():
    print(sys.argv)
    username = input("Username: ") 
    password = getpass.getpass('Password: ')
    
    print(f"Username: {username}, Password: {password}")

if __name__ == "__main__":
    print("Running...")
    # main()
    # getOsEnv()
    getEnvFile()