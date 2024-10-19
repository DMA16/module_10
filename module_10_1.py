from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Duck № {i + 1}')
            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')

"""start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
print('Время выполнения программы:', end_time - start_time)"""


#Если сначало запускать все функции, а потом ставить их на ожидание, программа выполняется быстрее
#Иначе, если после запуска функции мы будем сразу ставить ожидание её результата, то программа замедляется в ~4 раза
start_time = datetime.now()
thr = []
for i in range(5, 9):
    thr.append(Thread(target=write_words, args=(10, f'example{i}.txt')))
    thr[i - 5].start()

for i in range(4):
    thr[i].join()

end_time = datetime.now()
print('Время выполнения программы:', end_time - start_time)