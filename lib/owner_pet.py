class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  # This will use the pet_type setter for validation
        self.owner = owner  # This will use the owner setter for validation
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise ValueError('Not a valid pet type.')
        self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or owner is None):
            raise TypeError("Owner must be of type Owner or None")
        self._owner = owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Input must be of type Pet")
        pet.owner = self

    def sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


# Example usage
if __name__ == "__main__":
    alice = Owner("Alice")
    bob = Owner("Bob")

    fido = Pet("Fido", "dog", alice)
    whiskers = Pet("Whiskers", "cat", bob)
    
    # Attempting to create a pet with an invalid type
    try:
        nemo = Pet("Nemo", "fish")
    except ValueError as e:
        print(e)  # Output: Not a valid pet type.

    charlie = Pet("Charlie", "bird")
    alice.add_pet(charlie)

    print([pet.name for pet in alice.pets()])  # Output: ['Fido', 'Charlie']
    print([pet.name for pet in alice.sorted_pets()])  # Output: ['Charlie', 'Fido']
