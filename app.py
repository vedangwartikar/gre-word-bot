# To the Moon..

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from yahoofinancials import YahooFinancials
from forex_python.converter import CurrencyRates

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

updater = Updater('1598163939:AAHf-__oR8j20yTBnjPkI_DNvJGd3Ww996M')

updater.dispatcher.add_handler(CommandHandler('doge', doge))
updater.dispatcher.add_handler(CommandHandler('vet', vet))
updater.dispatcher.add_handler(CommandHandler('verge', verge))

updater.start_polling()
updater.idle()
