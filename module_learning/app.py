# 2 different ways of importing
from ecommerce.shopping.sales import calc_shipping, calc_tax
from ecommerce.shopping import sales
import sys

print(dir(sales))
sales.calc_shipping()
sales.calc_tax()

calc_shipping()
calc_tax()

# print(sys.path)
