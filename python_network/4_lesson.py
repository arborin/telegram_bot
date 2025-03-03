import sys
import yaml
import pythonping
import json


def my_function():
    pass


def main():
    hfile = "hosts.yml"
    
    with open(hfile) as file:
        data = yaml.full_load(file)
    
    print(json.dumps(data, indent=4))
    
    for dev, info in data.items():
        print("="*30)
        print(f">>> Device: {dev}")
        print("="*30)
        pythonping.ping(info['hostname'], verbose=True)
        # print(info)

if __name__ == "__main__":
    print("Running...")
    main()