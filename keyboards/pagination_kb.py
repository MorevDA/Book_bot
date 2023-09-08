from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons: str): # InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    for button in buttons:
        print(button)
        if button in LEXICON:
            kb_builder.add(InlineKeyboardButton(text=LEXICON.get(button), callback_data=button))
        else:
            kb_builder.add(InlineKeyboardButton(text=button, callback_data=button))
    #kb_builder.row(*[InlineKeyboardButton(text=LEXICON.get(button) if button in LEXICON else button,
                                          #callback_data='xeq') for button in buttons])
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

if __name__ == '__main__':
    print(LEXICON.get('forward'))
