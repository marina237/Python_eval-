


import time

import random



tf = 0.0001

status2str = {"attente": "en attente", "transit": "en transit"}



# Information sur le colis





class colis:

    def __init__(self, num_commande, type_):

        self.num_commande = num_commande

        self.status = "new"

        self.type_ = None

        print(f"creating {type_} colis")

        if type_ == "medium":

            weight, duration = 5, 5

        elif type_ == "large":

            weight, duration = 5, 10

        elif type_ == "extra_large":

            weight,duration = 7, 15

        else:

            self.type_ = False

            print(f"Error {type_} is unknown")

        if self.type_ is None:

            self.type_ = type_
            
        

    def __bool__(self):

        return bool(self.type_)



    def en_transit(self):

        self.status = "transit"



    def __str__(self):

        return f"Le colis numéro {self.num_commande} est {self.status}"





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

    mon_colis = colis(random.randint(1, 10000),"medium")

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

    return camion["max_load"] - sum([colis["weight"] for colis in camion["colis"]])



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



    print(f"Shipped  {len(camion['colis'])}")

    camion["colis"] = []





def process_gifts(camion, parcels2ship):

    for colis in parcels2ship:

        wrap_colis(colis)

        taken = take_parcel(camion,colis)

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




