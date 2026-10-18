import sys

print(sys.path)

'''
Use path.append() if the module is in another directory
'''

import module as m


names = ['sam', 'ana', 'karthi', 'venkat']
target = 'venkat'

x = m.search_index_in_list(names, target)
print(x)