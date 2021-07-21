#!/usr/bin/env python
# coding: utf-8

# In[1]:


def tiling_cost():
    while True:
        try:
            single_tile = float(input('Enter cost of single tile: ₦'))
            width = float(input('Enter Width of floor: (m)'))
            length = float(input('Enter Length of floor: (m)'))
            total_cost = width * length * single_tile
        except ValueError:
            print('Wrong input! Please enter a numerical value: (m)')
            continue
        else:
             print(f'Cost of tile for a {width} x {length} floor is: ₦{total_cost}')
        choice = input('Do you want to calculate again? Enter Yes or No: ').lower().startswith('y')
        if not choice:
            break

