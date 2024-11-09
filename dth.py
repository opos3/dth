import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.mood = 50
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.energy += 5
        self.mood += 2

    def to_sleep(self):
        print("Time to sleep")
        self.energy += 3
        self.mood -= 1

    def to_play(self):
        print("Time to play")
        self.mood += 5
        self.energy -= 4

    def is_alive(self):
        if self.energy <= 0:
            print("Too tired")
            self.alive = False
        elif self.mood <= 0:
            print("DEPREST")
            self.alive = False
        elif self.energy > 100:
            print("Too hyperactive")
            self.alive = False

    def end_of_day(self):
        print(f"Energy - {self.energy}")
        print(f"Mood - {self.mood}")

    def live(self, day):
        day = f"Day {day} of {self.name}'s life"
        print(f"{day:=^50}")
        action = random.randint(1, 3)
        if action == 1:
            self.to_eat()
        elif action == 2:
            self.to_sleep()
        elif action == 3:
            self.to_play()
        self.end_of_day()
        self.is_alive()

buddy = Dog("Buddy")
for day in range(365):
    if not buddy.alive:
        break
    buddy.live(day)