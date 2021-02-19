#gre_word_bot

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import pandas as pd

def word(update: Update, context: CallbackContext) -> None:
    words = pd.read_csv('words.csv')
    random_row = words.sample()
    # print(random_row['word'], random_row['definition'], random_row['part of speech'], random_row['example'])
    index = str(int(random_row.index.values[0]))
    word = random_row['word'].values[0]
    definition = random_row['definition'].values[0]
    part_of_speech = random_row['part of speech'].values[0]
    example = random_row['example'].values[0]

    # print('#' + index + '\n' + word + ' (' + part_of_speech + '): ' + definition + '\n' + example)
    update.message.reply_text('<i>#' + index + '</i>\n\n<strong>' + word + '</strong> (' + part_of_speech + '): ' + definition + '\n\n' + example, parse_mode='HTML')

updater = Updater('1675796212:AAHNxw79wXKq_WEvar7nKgJ2fiEXggkj2RI')

updater.dispatcher.add_handler(CommandHandler('word', word))

updater.start_polling()
updater.idle()
