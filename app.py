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
    update.message.reply_text(f'DGGE: {doge_price_inr} INR')


updater = Updater('1598163939:AAHf-__oR8j20yTBnjPkI_DNvJGd3Ww996M')

updater.dispatcher.add_handler(CommandHandler('doge', doge))

updater.start_polling()
updater.idle()