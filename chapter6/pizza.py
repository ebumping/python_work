#Store information about a pizza being ordered.
from ctypes.wintypes import PSIZE


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")