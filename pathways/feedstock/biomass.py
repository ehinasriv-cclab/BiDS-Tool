"""
Created on Mon March 23 

@author: ehinasriv
"""

from core.material import Material

def create_woody_biomass(amount):
    return Material(
        name="woody_biomass",
        amount=amount,
        properties={
            "moisture_content": 0.30,
            "carbon_fraction": 0.50,
            "ash_content": 0.02,
            "HHV": 18
        }
    )

print("this is me trying to print the parameters")