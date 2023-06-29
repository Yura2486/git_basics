class Animal:
    def __init__(self, age):
        self.age = age

    def change_age(self, age):
        self.age = age

    def age(self):
        return self.age

    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.name = name

class Person(Human):
    def __init__(self, name, age, taxid):
        super().__init__(name, age)
        self.taxid = taxid

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls} (name = {self.name!r})'


# TODO: fill classes above with the required logic
#       to represent human and person (probably with tax number, ...)
# TODO: try to make an Enterprise able to own Pets
# TODO: - add class to represent vaccine
#       - add class to represent generic chip,
#           and separate subclasses for concrete animal ID chips
#       - anything other you want to extend here

class Vaccine:
    def __init__(self, type_vac, starts, due):
        self.type_vac = type_vac
        self.starts = starts
        self.due = due

    def show_type(self):
        return self.type_vac

    def show_starts(self):
        return self.starts

    def show_due(self):
        return self.due

    def __str__(self):
        return f'{self.type_vac}, {self.starts.strftime("%x")}, {self.due.strftime("%x")}'

    def __repr__(self):
        return f'{self.__class__.__name__}()'

class Chip:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_size_str(self):
        return f'({self.width} x {self.length}) mm'

    def __repr__(self):
        return f'{self.__class__.__name__}()'

class GPSChip(Chip):
    def __init__(self, width, length, due):
        super().__init__(width, length)
        self.due = due

    def __repr__(self):
        return "GPSChip"

class Pet(Animal):
    """Abstracts an animal with an owner and name.

    Each pet is an animal having an owner and a name --
    that is how we model it.
    """

    def __init__(self, owner, nickname):
        """Set owner at instantiation."""
        self.change_owner(owner)
        self.nickname = nickname
        self.vaccines = []
        self.chip = None

    def change_owner(self, new_owner):
        """Called to transfer ownership or set a new owner."""
        self.owner = new_owner

    def add_vaccine(self, type_vac, starts, due):
        self.vaccines.append(Vaccine(type_vac, starts, due))

    def list_vaccines(self):
       return self.vaccines

    def add_chip(self, chip):
        self.chip = chip

    def get_chip(self):
        return self.chip

    def del_chip(self, chip):
        self.chip = None

    def __str__(self):
        return f'{self.nickname}'

#    def del_vaccine(self, type_vac, ):

    @property
    def owner(self):
        """Dummy getter for hidden method."""
        return self.__owner

    @owner.setter
    def owner(self, value):
        """This is called when setting owner.

        The difference is that here we can check
        what the user sets owner to. E.g. check
        that owner is not number.

        Called at dog.owner = value
        """
        # do some checks here
        if isinstance(value, Person):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance  or subclass of Person.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname} (owner = {self.owner!r})'

def print_info(pet):
    print("nickname:", pet)
    listvac = pet.list_vaccines()
    if len(listvac):
        print("vaccines list:")
    else:
        print("vaccines list:\nNone")
    for nmb in range(len(listvac)):
        print(f'\t{nmb}: {listvac[nmb]}')
    print(f'chip: {pet.get_chip()}')

if __name__ == '__main__':
    import datetime

    pets = []

    gchip = GPSChip(1, 2, datetime.datetime(2024,1,2))

    owner0 = Person("Mykola", 24, 987654321)
    owner1 = Person("Vasyl", 21, 1234567890)

    pet = Pet(owner0, "Patron")
    pet.add_vaccine("Pfizer", datetime.datetime(2020,1,2), datetime.datetime(2024,1,2))
    pet.add_vaccine("Rabies", datetime.datetime(2021,2,5), datetime.datetime(2022,4,7))
    pets.append(pet)

    pet = Pet(owner0, "duke2")
    pet.add_chip(gchip)
    pets.append(pet)

    pet = Pet(owner1, "Paws")
    pet.add_vaccine("Rabies", datetime.datetime(2000,1,2), datetime.datetime(2024,1,2))
    pets.append(pet)

    for ind, nms in enumerate(pets):
        print(f'\nPet {ind}')
        print_info(nms)


