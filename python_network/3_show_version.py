import sys


def my_function():
    pass


def main():
    file_name = "config.txt"
    with open(file_name, 'r') as file:
        data_list = file.readlines()
    
    for line in data_list:
        if 'Ios' in line:
            print(line)

if __name__ == "__main__":
    print("Running...")
    main()