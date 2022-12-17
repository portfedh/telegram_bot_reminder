import os
import telebot
import datetime as dt

TOKEN = os.environ.get("token_telegram_bs_re")
today = dt.datetime.now()


class lease():

    def __init__(self, property, rent, contract_start):
        self.property = property
        self.rent = f'${rent:,.2f}'
        self.contract_start = dt.datetime.strptime(contract_start, '%d/%m/%y')
        self.contract_end = self.contract_start + dt.timedelta(days = 365)
        self.days_until = self.contract_end - today

    def create_message(self):
        self.message = ('<strong>' + self.property + '</strong>' +
                        '\nRenta : ' + self.rent +
                        '\nInicio : ' + self.contract_start.strftime('%d-%b-%Y') +
                        '\nFinal : ' + self.contract_end.strftime('%d-%b-%Y') +
                        '<strong>' +
                        '\nDias restantes: ' + str(self.days_until.days) +
                        '</strong>')
        print(self.message)

    def send_telegram(self):
        self.bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
                
        self.bot.send_message(chat_id=1061946783, text=self.message) 

if __name__ == '__main__':
    x = lease('<b>ExampleProperty_1</b>', 10_000, '31/10/22')
    x.create_message()
    x.send_telegram()
                  