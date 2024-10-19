from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        self.name_ = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.name_}, на нас напали утки!')

        enemies_count = 100
        day_count = 0
        while enemies_count != 0:
            enemies_count -= self.power if self.power < enemies_count else enemies_count
            day_count += 1
            sleep(1)

            print(f'{self.name_} сражается {day_count} день(дня)..., осталось {enemies_count} уток.')

        print(f'{self.name_} одержал победу над утками спустя {day_count} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
