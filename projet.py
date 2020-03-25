# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:49:59 2020
@author: mary-
"""


import time
import random

tf = 0.0001
status2str = {"attente": "en attente", "transit": "en transit"}

# Information sur le colis


class colis:
    def __init__(self, num_commande, type_):
        self.num_commande = num_commande
        self.status = "new"
        self.type = None
        print(f"creating {type_} colis")
        if type_ == "medium":
            weight, duration = 5, 5
        elif type_ == "large":
            weight, duration = 5, 10
        elif type_ == "extra_large":
            weight, duration = 7, 15
        else:
            self.type = False
            print(f"Error {type_} is unknown")
        if self.type is None:
            self.type = type_

    def __bool__(self):
        return bool(self.type)

    def en_transit(self):
        self.status = "transit"

    def __str__(self):
        return f"Le colis numéro {self.num_commande} est {status2str[self.status]}"


class camion:
    def __init__(self, imat="12344"):
        self.imat = imat
        self.colis = []

    def __str__(self):
        return (
            f"Le camion immatricule {self.imat} contient"
            f"{' ,'.join( '%s' %  colis.num_commande for colis in self.colis)}"
        )


if __name__ == "__main__":
    mon_colis = colis(random.randint(1, 10000))
    print(mon_colis)
    mon_colis.en_transit()
    print(mon_colis)
    camion = camion()
    camion.colis.append(mon_colis)
    print(camion)


def type_de_colis(type_):

    print(f"creating {type_} colis")
    if type_ == "medium":
        weight, duration = 5, 5
    elif type_ == "large":
        weight, duration = 5, 10
    elif type_ == "extra_large":
        weight, duration = 7, 15
    else:
        print(f"Error {type_} is unknown")
        return {}
    return {"type ": type_, "duration": duration, "weight": weight, "status": "new"}


def types(type):
    for type in types:
        t = time.time()
        yield type_de_colis(type)
        print(f"time taken for creating gift {time.time() - t:.4f}")

    # return [ for kind in kinds]


def wrap_colis(colis):
    sleep_time = 0
    print("Starting to wrap")
    time.sleep(sleep_time * tf)
    print(f"Wrapped {colis}")
    colis["status"] = "wrapped"


def compute_free_load(camion):
    return camion["max_load"] - sum(colis["weight"] for colis in camion["colis"])


def camion_load(camion):
    return sum(colis["weight"] for colis in camion["colis"])


def take_parcel(camion, colis):

    if colis["weight"] <= compute_free_load(camion):
        camion["colis"].append(colis)
        print("Le colis peut être mis dans le camion !")
    else:
        print("Le colis ne peut pas être mis dans le camion !")
    return colis in camion["colis"]


def livraison(camion):
    print(f"Shipping {len(camion['colis'])}")
    print(f"{camion_load(camion)} kg to be shipped")

    for colis in camion["colis"]:
        time.sleep(camion["time_per_gift"] * tf)

    pri(f"Shipped  {len(camion['colis'])}")
    camion["colis"] = []


def process_gifts(camion, parcels2ship):
    for colis in parcels2ship:
        wrap_colis(colis)
        taken = take_parcel(camion)
        if taken:
            print(f"current load {camion_load(camion)}")
            continue
        else:
            livraison(camion)
            taken = take_parcel(camion, colis)
            if not taken:
                print("Error, sledge should take the gift after shipping")
    else:
        livraison(camion)


def create_and_process(gift_types):

    process_gifts(type_de_colis(gift_types))


"""
if __name__ == "__main__":

    import sys

    if len(sys.argv) == 2:

        n_colis = int(sys.argv[1])

    else:

        n_colis = 5


if __name__ == '__main__':
    from random import choices
    colis_types = choices(["medium", "large", "extra large"], k=n_colis)
    li = []
    for i in range(4):
        li.append(type_de_colis(colis_types[i]))
        print(li)


    camion = {"colis": li, "max_load": 100, "time_per_gift": 5}


    print("la charge disponible est de ", compute_free_load(camion, li), "kg")


    print(take_parcel(camion))

import sys
#import pygame as pg

#ship = pg.image.load("C:/Users/mary-/Documents/stid2/S4/Pyhton Avancée/La poste.jpg")
# à mettre dans vos dépots

# Test a mettre dans le fichier de test
"""

import unittest


class Tests(unittest.TestCase):
    def test_type_de_colis(self):
        mauvais = type_de_colis("deedwedw")
        moyen = colis(0000, "medium")
        self.assertEqual(
            moyen.__dict__,
            {
                "type ": "medium",
                "num_commande": 0,
                "status": "new",
                "duration": 5,
                "weight": 5,
            },
        )

    def test_objectify_colis(self):
        mauvais = colis(123, "deedwedw")
        self.assertFalse(mauvais)

    def test_wrap_colis(self):
        colis = type_de_colis("medium")
        self.assertEqual(colis["status"], "new")
        wrap_colis(colis)
        self.assertEqual(colis["status"], "wrapped")

    def test_take_parcel(self):

        camion = {"colis": [], "max_load": 100, "time_per_gift": 5}
        colis = type_de_colis("medium")
        self.assertTrue(take_parcel(camion, colis))


if __name__ == "__main__":
    unittest.main()
