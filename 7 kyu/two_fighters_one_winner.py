__author__ = 'Alex Orlovskyi'

'''
"Two fighters, one winner" task, provided by codewars.com/users/MirzaI . 7 kyu difficulty level.

Create a function that returns the name of the winner in a fight between two fighters.
Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.
Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.
Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
'''


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    available_steps_of_p1 = fighter1.health//fighter2.damage_per_attack + (fighter1.health%fighter2.damage_per_attack>0) + (fighter1.name==first_attacker)
    available_steps_of_p2 = fighter2.health // fighter1.damage_per_attack + (fighter2.health % fighter1.damage_per_attack > 0) + (
                fighter2.name == first_attacker)
    if available_steps_of_p1 > available_steps_of_p2:
        return fighter1.name
    elif available_steps_of_p1 == available_steps_of_p2:
        return first_attacker
    return fighter2.name


f1 = Fighter("Jerry", 20, 5)
f2 = Fighter("Harald", 30, 3)

#some self-testing before send
print(declare_winner(f1,f2,"Harald"))
print(30//5 + (30%5>0))
print(20//3 + (20%3>0))