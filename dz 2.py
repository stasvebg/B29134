import random
class Cat:
    def init (self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.alive = True

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.satiety -= 5

    def satiety(self):
        print('time for eat')
        self.gladness += 5
        self.satiety += 5

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.satiety -= 5

    def is_alive(self):
        if self.gladness <= 0:
            print('Depression...')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'satiety = {round(self.progress, 2)}')

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cude = random.randint(1,3)
        if live_cude == 1:
            self.to_study()
        elif live_cude == 2:
            self.to_sleep()
        elif live_cude == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

kora = Cat (name = 'Kora')
for day in range(365):
    if nick.alive ==  False:
        break
    kora.live(day)