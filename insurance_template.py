import os
import telebot
import datetime as dt

TOKEN = os.environ.get("token_telegram_compass")
today = dt.datetime.now()


class insurance():

    def __init__(self, insurance_plan_name, start_date):
        self.insurance_plan_name = insurance_plan_name
        self.start_date = dt.datetime.strptime(start_date, '%d/%m/%y')
        self.end_date = self.start_date + dt.timedelta(days = 365)
        self.days_until = self.end_date - today
        self.create_message()
        self.send_telegram()

    def create_message(self):
        self.message = ('<strong>' + self.insurance_plan_name + '</strong>' +
                        '\nStart : ' + self.start_date.strftime('%d-%b-%Y') +
                        '\nEnd : ' + self.end_date.strftime('%d-%b-%Y') +
                        '<strong>' +
                        '\nDays remaining: ' + str(self.days_until.days) +
                        '</strong>')
        print(self.message)

    def send_telegram(self):
        self.bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
        self.bot.send_message(chat_id=1061946783, text=self.message) 

if __name__ == '__main__':
    x = insurance('BUPA_Insurance_1', '31/10/22')
                  