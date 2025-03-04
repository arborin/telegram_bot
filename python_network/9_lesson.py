import jinja2

template_str = """
    vlan {{ data_dict['vlan_number'] }}
    name {{ data_dict['vlan_name']  }}
"""

data = {"vlan_number": 10, "vlan_name": "Office Vlan"}

template_env = jinja2.Environment(loader=jinja2.BaseLoader()).from_string(template_str)

render_str = template_env.render(data_dict=data)

print(render_str)