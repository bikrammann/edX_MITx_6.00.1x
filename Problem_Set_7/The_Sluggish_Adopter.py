class SluggishAdopter(Adopter):
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        import math
        return math.sqrt((to_location[0] - self.location[0])**2 + (to_location[1] - self.location[1])**2)

    def get_score(self, adoption_center):
        import random
        distance = self.get_linear_distance(adoption_center.get_location())
        if distance < 1:
            return 1 * Adopter.get_score(self, adoption_center)
        if 1 <= distance < 3:
            return random.uniform(0.7, 0.9) * Adopter.get_score(self, adoption_center)
        if 3 <= distance < 5:
            return random.uniform(0.5, 0.7) * Adopter.get_score(self, adoption_center)
        if distance >= 5:
            return random.uniform(0.1, 0.5) * Adopter.get_score(self, adoption_center)
