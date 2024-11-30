import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {
            'english_word': english_word,
            'word_definition': word_definition
        }
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None

def translate_to_russian(word, definition):
    translator = Translator()
    try:
        translated_word = translator.translate(word, src='en', dest='ru').text
        translated_definition = translator.translate(definition, src='en', dest='ru').text
        return translated_word, translated_definition
    except Exception as e:
        print(f'Ошибка перевода: {e}')
        return word, definition

def word_game():
    print('Добро пожаловать в игру на угадывание слов!')
    while True:
        word_data = get_english_words()
        if not word_data:
            print('Не удалось получить слово. Попробуйте позже.')
            break

        english_word = word_data['english_word']
        word_definition = word_data['word_definition']

        russian_word, russian_definition = translate_to_russian(english_word, word_definition)

        print(f'Значение слова: {russian_definition}')
        user_input = input('Какое это слово (на русском языке)? ')

        if user_input.lower() == russian_word.lower():
            print('Всё верно!')
        else:
            print(f'Неверно! Загаданное слово: {russian_word} (английское слово: {english_word})')

        play_again = input('Хотите сыграть ещё раз? (y/n): ').strip().lower()
        if play_again != 'y':
            print('Спасибо за игру! До скорой встречи!')
            break

if __name__ == '__main__':
    word_game()