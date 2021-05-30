# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:50:12 2021

@author: AU000MZG
"""

class Freshie:
    
    freshies = { "Name" : ['Freshie1' , 'Freshie2', 'Freshie3'],
                "Age" : [21,19,20],
                "University" : ['SUSS', 'SUTD', 'SIT']
        }
    
    def __init__(self, name):
        self.name = name
        
    def intro(self):
        return "Dear" + self.name + "Welcome to Campus!"
    
#new branch

print('Hello world!')

print("change")
        
