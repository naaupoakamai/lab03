from itertools import permutations

def print_word_permutations():
    user_input = input("Введите строку: ")
    words = user_input.split()  # Разделяем строку на слова
    perm_list = [' '.join(p) for p in permutations(words)]  # Генерируем перестановки слов
    for perm in perm_list:
        print(perm)

# Вызов функции
print_word_permutations()



