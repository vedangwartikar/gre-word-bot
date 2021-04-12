# To the Moon...

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from yahoofinancials import YahooFinancials
from forex_python.converter import CurrencyRates
import pandas as pd

def doge(update: Update, context: CallbackContext) -> None:
    yahoo_financials = YahooFinancials('DOGE-USD')
    doge_price = yahoo_financials.get_current_price()

    c = CurrencyRates()
    inr_rate = c.get_rate('USD', 'INR')

    doge_price_inr = round(doge_price * inr_rate, 4)
    print(doge_price_inr)
    update.message.reply_text(f'DOGE: {doge_price_inr} INR')

def vet(update: Update, context: CallbackContext) -> None:
    yahoo_financials = YahooFinancials('VET-USD')
    vet_price = yahoo_financials.get_current_price()

    c = CurrencyRates()
    inr_rate = c.get_rate('USD', 'INR')

    vet_price_inr = round(vet_price * inr_rate, 4)
    print(vet_price_inr)
    update.message.reply_text(f'VET: {vet_price_inr} INR')

def verge(update: Update, context: CallbackContext) -> None:
    yahoo_financials = YahooFinancials('XVG-USD')
    verge_price = yahoo_financials.get_current_price()

    c = CurrencyRates()
    inr_rate = c.get_rate('USD', 'INR')

    verge_price_inr = round(verge_price * inr_rate, 4)
    print(verge_price_inr)
    update.message.reply_text(f'VERGE: {verge_price_inr} INR')

def bat(update: Update, context: CallbackContext) -> None:
    yahoo_financials = YahooFinancials('BAT-USD')
    bat_price = yahoo_financials.get_current_price()

    c = CurrencyRates()
    inr_rate = c.get_rate('USD', 'INR')

    bat_price_inr = round(bat_price * inr_rate, 4)
    print(bat_price_inr)
    update.message.reply_text(f'BAT: {bat_price_inr} INR')

def eth(update: Update, context: CallbackContext) -> None:
    yahoo_financials = YahooFinancials('ETH-USD')
    eth_price = yahoo_financials.get_current_price()

    c = CurrencyRates()
    inr_rate = c.get_rate('USD', 'INR')

    eth_price_inr = round(eth_price * inr_rate, 4)
    print(eth_price_inr)
    update.message.reply_text(f'ETH: {eth_price_inr} INR')

def iost(update: Update, context: CallbackContext) -> None:
    yahoo_financials = YahooFinancials('IOST-USD')
    iost_price = yahoo_financials.get_current_price()

    c = CurrencyRates()
    inr_rate = c.get_rate('USD', 'INR')

    iost_price_inr = round(iost_price * inr_rate, 4)
    print(iost_price_inr)
    update.message.reply_text(f'ETH: {iost_price_inr} INR')

def bnb(update: Update, context: CallbackContext) -> None:
    yahoo_financials = YahooFinancials('BNB-USD')
    bnb_price = yahoo_financials.get_current_price()

    c = CurrencyRates()
    inr_rate = c.get_rate('USD', 'INR')

    bnb_price_inr = round(bnb_price * inr_rate, 4)
    print(bnb_price_inr)
    update.message.reply_text(f'ETH: {bnb_price_inr} INR')

def nice(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('6*9+6+9=69')

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

updater = Updater('1598163939:AAHf-__oR8j20yTBnjPkI_DNvJGd3Ww996M')

updater.dispatcher.add_handler(CommandHandler('doge', doge))
updater.dispatcher.add_handler(CommandHandler('vet', vet))
updater.dispatcher.add_handler(CommandHandler('verge', verge))
updater.dispatcher.add_handler(CommandHandler('nice', nice))
updater.dispatcher.add_handler(CommandHandler('eth', eth))
updater.dispatcher.add_handler(CommandHandler('iost', iost))
updater.dispatcher.add_handler(CommandHandler('bnb', bnb))
updater.dispatcher.add_handler(CommandHandler('word', word))

updater.start_polling()
updater.idle()
