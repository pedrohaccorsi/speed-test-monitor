import datetime;

class Calendar():

    def getToday(self):
        return datetime.datetime.now().strftime("%Y-%m-%d");

    def getNow(self):
        return datetime.datetime.now().strftime("%H:%M");

    