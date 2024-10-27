import threading
from queue import Queue
from random import randint
from time import sleep


class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest



class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name


    def run(self):
        sleep(randint(3, 10))



class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()


    def guest_arrival(self, *guests):
        for g in guests:
            occupied_tables = 0

            for table in self.tables:
                if table.guest is None:
                    table.guest = g
                    g.start()

                    print(f"{g.name} сел(-а) за стол номер {table.number}")

                    break
                else:
                    occupied_tables += 1

            if occupied_tables == len(self.tables):
                self.queue.put(g)
                print(f"{g.name} в очереди")


    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")

                    table.guest = None

                    if not self.queue.empty():
                        g = self.queue.get()
                        table.guest = g

                        print(f"{g.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

                        g.start()



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()