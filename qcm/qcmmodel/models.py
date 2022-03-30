from pydantic import BaseModel


class RegimeAlimentaire(BaseModel):
    name: str
    description: str

    def __hash__(self):
        return hash((self.name, self.description))


class Animal(BaseModel):

    name: str
    regime: RegimeAlimentaire


class Animals(BaseModel):

    animals: list[Animal]

    def get_known_regime(self) -> set:
        return {animal.regime for animal in self.animals}


animals_dict = {
    "animals": [
        {
            "name": "Chevreuil",
            "regime": {
                "name": "Herbivore",
                "description": "Vegan quoi !"
            }
        },
        {
            "name": "Loup",
            "regime": {
                "name": "Omnivore",
                "description": "Mange de tout"
            }
        },
        {
            "name": "Chouette",
            "regime": {
                "name": "Carnivore",
                "description": "Mange d'autres animaux"
            }
        },
        {
            "name": "Herisson",
            "regime": {
                "name": "Insectivore",
                "description": "Mange des insectes"
            }
        }
    ]
}



