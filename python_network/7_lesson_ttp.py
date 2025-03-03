import ttp
import os

template_str = """{{ ip }} {{ status }}"""


with open("show_ip.txt") as file:
    data = file.read()
    
print(data)

ttp_parser_obj = ttp.ttp(data=data, template=template_str)

ttp_parser_obj.parse()
print(ttp_parser_obj.result())