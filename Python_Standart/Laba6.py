firstList = input('Введите слова через запятую: ').split(",")

print("Количество слов в списке", len(firstList))

secondList = input('Введите {} слов(а): '.format(len(firstList))).split(",")

if len(firstList) != len(secondList):
    print("Количество слов в списке различается")

a = dict(zip(firstList, secondList))

print(a)