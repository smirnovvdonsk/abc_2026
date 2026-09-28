#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
# .....

FILE_NAME = 'task19.csv'

with open(FILE_NAME, 'w') as file:
    file.close()

with open(FILE_NAME, 'a', encoding='utf-8') as file:
    for line in algoritm:
        file.write(f"{line}\n")
    file.close()

