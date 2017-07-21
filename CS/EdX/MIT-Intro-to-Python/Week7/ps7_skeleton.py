import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        # Your Code Here
        self.name = name
        self.species_types = species_types
        self.location = location

    def get_name(self):
        # Your Code Here 
        return self.name

    def get_location(self):
        # Your Code Here 
        x = self.location[0]*1.0
        y = self.location[1]*1.0
        return (x,y)
        
    def get_species_count(self):
        # Your Code Here 
        species_copy = self.species_types.copy()
        
        for key in self.species_types:
            if self.species_types[key] == 0:
                del species_copy[key]
        #print(species_copy, self.species_types)
        
        return species_copy

    def get_number_of_species(self, animal):
        # Your Code Here 
        num = self.species_types[animal]
        return num


    def adopt_pet(self, species):
        # Your Code Here 
        self.species_types[species] -= 1


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        # Your Code Here 
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        # Your Code Here 
        return self.name

    def get_desired_species(self):
        # Your Code Here 
        return self.desired_species

    def get_score(self, adoption_center):
        # Your Code Here 
        #dicti = AdoptionCenter.get_species_count()
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        return num_desired



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        for animal in self.considered_species:
            adopter_score += 0.3*adoption_center.get_number_of_species(animal)
        return adopter_score

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        adopter_score -= 0.3*adoption_center.get_number_of_species(self.feared_species)
        if adopter_score < 0:
            return 0.0
        else:
            return adopter_score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        center_animals = adoption_center.get_species_count().keys()
        for allergy in self.allergic_species:
            if allergy in center_animals:
                return 0.0
        return Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        center_animals = adoption_center.get_species_count().keys()
        lowest_effectiveness = 1.0
        for allergy in self.allergic_species:
            if allergy in center_animals:
                if self.medicine_effectiveness[allergy] < lowest_effectiveness:
                    lowest_effectiveness = self.medicine_effectiveness[allergy]
        return Adopter.get_score(self, adoption_center)*lowest_effectiveness


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.

    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):

        x, y = to_location.get_location()
        self_x, self_y = self.location

        d = ((x-self_x)**2 + (y-self_y)**2)**(1/2)
        return d


    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        d = self.get_linear_distance(adoption_center)

        if d < 1:
            return adopter_score
        elif 1 <= d < 3:
            return rand.uniform(0.7, 0.9)*adopter_score
        elif 3 <= d < 5:
            return rand.uniform(0.5, 0.7)*adopter_score
        elif d >= 5:
            return rand.uniform(0.1, 0.5)*adopter_score


'''    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here 

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 
'''

species_list = {"Dog": 10, "Cat": 5, "Lizard": 3, 'Wolf': 2, 'Owl': 5, 'Usagi': 2}
vermont = AdoptionCenter('vermont', species_list, (10.0, 11.0))
print(vermont.get_number_of_species('Dog'))
vermont.adopt_pet('Wolf')
print(vermont.get_location())
print(vermont.get_species_count())

madeleine = Adopter('Madeleine', 'Dog')
print(madeleine.get_desired_species())
print(madeleine.get_score(vermont))

naoko = FlexibleAdopter("Naoko", 'Dog', ['Cat', 'Wolf'])
print(naoko.get_score(vermont))

Natsumi = AllergicAdopter("Natsumi", 'Owl', ['Komodo', 'Usagi', 'Dog'])
print(Natsumi.get_score(vermont))

Ueno = MedicatedAllergicAdopter("Ueno", 'Owl', ['Komodo', 'Usagi', 'Dog'], {'Dog': 0, 'Usagi': 1, 'Komodo': 0})
print(Ueno.get_score(vermont))

Aika = SluggishAdopter("Natsumi", 'Usagi', (1.0, 1.0))
print(Aika.get_linear_distance(vermont))
print(Aika.get_score(vermont))