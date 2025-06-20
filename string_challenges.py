# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.lower().count("а"))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
counter = 0 # Счетчик букв
# Список гласных букв
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
for letter in range(len(word) - 1):
    if word[letter] in vowels:
        counter += 1
print(f'Количество гласных букв в строке: {counter}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
words_list = sentence.split() # разбиваем фразу на список слов
counter_words = 0 # счетчик слов для определения их количества.

# Цикл основной
while counter_words < len(words_list):
    print(words_list[counter_words][0])
    counter_words += 1

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
words_list = sentence.split() # разбиваем фразу на список слов
counter_words = 0 # счетчик слов для определения их количества.
len_of_word = 0 # счетчик слов
all_lens = 0 # подсчет суммы длин всех слов

# Цикл основной
while counter_words < len(words_list):
    len_of_word = len(words_list[counter_words])
    # Бонус . Вывожу длину каждого слова
    print(f'Длина слова "{words_list[counter_words]}" - {len_of_word} знаков')
    counter_words += 1
    all_lens += len_of_word

# Вывожу результат по задаче:
print(f'Средняя длина всех слов {all_lens / counter_words}')
