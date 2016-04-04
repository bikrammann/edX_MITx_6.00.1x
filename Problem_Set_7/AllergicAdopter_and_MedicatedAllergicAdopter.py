class AllergicAdopter(Adopter):
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        for species in self.allergic_species:
            if adoption_center.get_species_count().get(species, 0) > 0:
                return 0.0
        return Adopter.get_score(self, adoption_center)


class MedicatedAllergicAdopter(AllergicAdopter):
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        min_med_effect = 1.0
        for species in self.allergic_species:
            if species in adoption_center.get_species_count():
                med_effect = self.medicine_effectiveness.get(species, 0)
                if med_effect < min_med_effect:
                    min_med_effect = med_effect
        return Adopter.get_score(self, adoption_center) * min_med_effect

