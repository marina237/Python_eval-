# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:07:13 2020

@author: mary-
"""

from la_poste import type_de_colis,compute_free_load,wrap_colis,take_parcel

import unittest




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





    print("la charge disponible est de ", compute_free_load(camion), "kg")





    print(take_parcel(camion))







class Tests(unittest.TestCase):

    def test_type_de_colis(self):


        moyen = type_de_colis(0000, "medium")

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

        mauvais = type_de_colis(123, "deedwedw")

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


