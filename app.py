#gre_word_bot..

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import pandas as pd
import os
import random

def word(update: Update, context: CallbackContext) -> None:
    words = pd.read_csv('words.csv')
    random_row = words.sample()
    # print(random_row['word'], random_row['definition'], random_row['part of speech'], random_row['example'])
    index = str(int(random_row.index.values[0]))
    word = random_row['word'].values[0]
    definition = random_row['definition'].values[0]
    part_of_speech = random_row['part of speech'].values[0]
    example = random_row['example'].values[0]

    print(word)
    update.message.reply_text('<i>#' + index + '</i>\n\n<strong>' + word + '</strong> (' + part_of_speech + '): ' + definition + '\n\n' + example, parse_mode='HTML')

def formula(update: Update, context: CallbackContext) -> None:
    # path = 'quant'
    # photo = "{}/{}".format(path, random.choice((os.listdir(path))))
    try:
        photo_links = ['https://i.ibb.co/Wg8r9CH/circles.png', 'https://i.ibb.co/FhPGLy4/triangles.png', 'https://i.ibb.co/sQbH4gz/polygons.png', 'https://i.ibb.co/7nrv2wz/rectangles.png', 'https://i.ibb.co/fCSTfDZ/squares.png', 'https://i.ibb.co/XWDT0VR/trapezoids.png']
        photo = random.choice(photo_links)
        update.message.reply_photo(photo)
    except:
        pass

updater = Updater('2085897495:AAH0c9n65vmvFHa78rGaX_3IFEQ2Eb-Kwu4')

updater.dispatcher.add_handler(CommandHandler('word', word))
updater.dispatcher.add_handler(CommandHandler('formula', formula))

updater.start_polling()
updater.idle()
