#todo: Модифицировать программу таким образом чтобы она выводила
# приветствие "Hello", которое только что записали в файл text.txt

f = open("text.txt", "w+t")
f.write("Hello\n")
# Ваше решение.


f.flush()
with open("text.txt", "r+t") as ff:
    print(''.join(ff.readlines()))


f.close()