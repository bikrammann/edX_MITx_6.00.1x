class AdoptionCenter(object):
    def __init__(self, name, species_types, location):
        self.name = name
        self.location = (float(location[0]),float(location[1]))
        self.species_count = species_types

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_count.copy()

    def get_number_of_species(self, species_name):

        if species_name not in self.species_count:
            return 0
        return self.species_count[species_name]

    def adopt_pet(self, species_name):
        if species_name in self.species_count.keys():
            if self.species_count[species_name] > 0:
                self.species_count[species_name] = self.species_count[species_name] - 1
                if self.species_count[species_name] == 0:
                    del self.species_count[species_name]





