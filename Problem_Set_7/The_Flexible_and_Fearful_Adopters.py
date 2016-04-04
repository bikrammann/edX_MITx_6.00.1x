class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self,adoption_center):
        num_other = [adoption_center.get_number_of_species(n) for n in self.considered_species]
        return Adopter.get_score(self,adoption_center) + 0.3 * sum(num_other)

class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self,adoption_center):
        if Adopter.get_score(self,adoption_center) - 0.3 * adoption_center.get_number_of_species(self.feared_species) < 0:
            return 0.0
        else:
            return Adopter.get_score(self,adoption_center) - 0.3 * adoption_center.get_number_of_species(self.feared_species)

