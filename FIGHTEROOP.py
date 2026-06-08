import random
import time

class Plane:
    def __init__(self, name, hp, aim120, aimsx, flares):
        self.name = name
        self.__health = hp
        self.aim120 = aim120
        self.aimsx = aimsx
        self.flares = flares

    def report(self):
        print(self.name + " hp remaining: " + str(self.__health))

    def is_dead(self):
        return self.__health <= 0

    def use_flare(self):
        print(self.name + " used flares.")
        return True

    def attack_aim120(self):
        print(self.name + " shot an AIM-120")
        return self.aim120

    def attack_aimsx(self):
        print(self.name + " shot an AIM SX")
        return self.aimsx

    def take_damage(self, dmg):
        if dmg > 0:
            self.__health -= dmg
            print("Took " + str(dmg) + " damage")
        else:
            print("No damage taken")


class EnemyPlane(Plane):
    def __init__(self, name, hp, aim120, aimsx, flares, jet_type):
        super().__init__(name, hp, aim120, aimsx, flares)
        self.jet_type = jet_type

    def enemy_attack(self):
        print("Enemy is an " + self.jet_type)
        
        if self.jet_type == "A-10":
            print("A-10 strafing run")
            return 100
        elif self.jet_type == "Dassault Rafale":
            print("Rafale payload strike")
            return 400
        elif self.jet_type == "F-35":
            print("F-35 instant kill")
            return 9999
            
        return 0


print("--- INITIATE PLANES ---")
p_name = input("Enter jet name: ") #ENTER F-22 :)
player = Plane(p_name, 1000, 200, 500, "yes")

pool = ["A-10", "Dassault Rafale", "F-35"]
enemy_type = random.choice(pool)
enemy = EnemyPlane("Enemy", 1000, 0, 0, 0, enemy_type)

print("\n--- START ---")
player.report()
enemy.report()
time.sleep(1)

while True:
    print("\nPlayer turn...")
    time.sleep(1)
    
    print("1. FLARE\n2. AIM-120\n3. AIM SX")
    move = input("Pick a number: ")
    
    flared = False
    p_dmg = 0
    
    if move == "1":
        flared = player.use_flare()
    elif move == "2":
        p_dmg = player.attack_aim120()
    elif move == "3":
        p_dmg = player.attack_aimsx()
    else:
        print("Invalid move, skipped turn")

    if p_dmg > 0:
        enemy.take_damage(p_dmg)
    
    enemy.report()
    time.sleep(1)

    if enemy.is_dead():
        print("\nPLAYER WINS")
        break

    print("\nEnemy turn...")
    time.sleep(1)
    
    e_dmg = enemy.enemy_attack()
    
    if flared:
        print("Attack deflected by flares!")
    else:
        player.take_damage(e_dmg)
        
    player.report()
    time.sleep(1)

    if player.is_dead():
        print("\nGAME OVER")
        break

print("\nGame closed.")