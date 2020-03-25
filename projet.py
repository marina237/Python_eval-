# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:49:59 2020
@author: mary-
"""


import time
import random

  
    #Information sur le colis
class colis():
    
        def __init__(self, num_commande):
    
            self.num_commande = num_commande
        
        def en_transit(self):
            print(f"Le colis numéro {self.num_commande} est en transit.")
    
    
mon_colis = colis(random.randint(1,10000))
mon_colis.en_transit()
    
    
    
def type_de_colis(type):

    print(f"creating {type} colis")

    if type == "medium":

        weight = int(5)

        duration = int(5)

        return {"type ": type, "duration": duration, "weight": weight}

    elif type == "large":

        weight =int(5)

        duration = int(10)

        return {"type": type, "duration": duration, "weight": weight}



    elif type == "extra large":

        weight = int(7)

        duration = int(15)

        return {"type ": type, "duration": duration, "weight": weight}

    else:
        print(f"Error {type} is unknown")


def types(type):

    for type in types:

        t = time.time()

        yield type_de_colis(type)

        print(f"time taken for creating gift {time.time() - t:.4f}")

    # return [ for kind in kinds]






def wrap_colis(colis):
    print("Starting to wrap")

    time.sleep(2)

    #print("Wrapped a % s colis"  % kind["kind"] )
    print("Wrapped a %s colis" %colis)
    
    
    

      


def compute_free_load(camion,colis):
   
   return camion["max_load"] - sum(colis["weight"] for colis in camion["colis"])





def camion_load(cam):
   return sum(colis["weight"] for colis in cam["colis"])





def take_gift(camion):

    if camion["colis"][1]["weight"] <= compute_free_load(camion,colis):

       camion['colis'].append(camion)
       print("Le colis peut être mis dans le camion !")

       return 1
      

    else:
        print("Le colis ne peut pas être mis dans le camion !")
        return 0




# Tiends mais il faudrait qu'on puisse savoir si le cadeau a été pris

# Soit a la valeur de return

#  (exception)





def livraison(camion):

    print(f"Shipping {len(camion['colis'])}")

    print(f"{camion_load(camion)} kg to be shipped")



    for colis in camion["colis"]:

        time.sleep(camion["time_per_gift"])

    print(f"Shipped  {len(camion['colis'])}")

    camion["colis"] = []





def process_gifts(camion):

    for colis in camion:

        wrap_colis(colis)

        taken = take_gift(camion)

        if taken == 1:

            print(f"current load {camion_load(camion)}")

            continue

        else:

            livraison(camion)

            taken = take_gift(camion, colis)

            if taken == 0:

                print("Error, sledge should take the gift after shipping")

    else:

       livraison(camion)
       
       




def create_and_process(gift_types):

    process_gifts(type_de_colis(gift_types))

if __name__ == "__main__":

    import sys



    if len(sys.argv) == 2:

        n_colis = int(sys.argv[1])

    else:

        n_colis = 5

    from random import choices



    colis_types = choices(["medium", "large", "extra large"], k=n_colis)

    

li=[]
for i in range(4) :
    
    li.append(type_de_colis(colis_types[i]))
    print(li)
    


camion = {"colis":li, "max_load": 100, "time_per_gift": 5}







print("la charge disponible est de ",compute_free_load(camion,li),"kg")

 
print(take_gift(camion))

import sys
import pygame as pg   
ship =pg.image.load('C:/Users/mary-/Documents/stid2/S4/Pyhton Avancée/La poste.jpg')

#Test

import unittest

class Tests(unittest.TestCase):

    def test_type_de_colis(self):
        self.assertEqual(type_de_colis("medium"), {'type ': 'medium', 'duration': 5, 'weight': 5})


    def test_wrap_colis(self):
        self.assertEqual(wrap_colis(colis), 2)


    def test_take_gift(self):
        self.assertEqual(take_gift(camion), 10)
         

if __name__ == '__main__':
    unittest.main()
