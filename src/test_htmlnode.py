import unittest
from htmlnode import HTMLNode

node_list = []
for i in range(1,61):
    if i > 50 and i < 60:
        node_list.append(HTMLNode(f"<tag{i}>", f"test{i}", None, None))
    elif i == 60:
        node_list.append(HTMLNode(f"<tag{i}>", f"test{i}", None, {"href": "https://wwww.google.com",
                                                                  "target": "_blank",
                                                                  "id": "you figured it out, you genius"}))
    else:
        node_list.append(HTMLNode(f"<tag{i}>", f"test{i}", None, {"Prop 1": "val 1",
                                                                  "Prop 2": "val 2",
                                                                  "Prop 3": "val 3"}))
for item in node_list:
    print("---------------------------------")
    print(item.__repr__())
    print(item.props_to_html())
