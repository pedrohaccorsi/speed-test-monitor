class Snapshot():

    def __init__(self, download_speed, server, date, hour):
        self.download_speed = download_speed;
        self.server = server;
        self.date = date;
        self.hour = hour;

    def toJSON(self):
        return {
            "download_speed" : self.download_speed,
            "server"         : self.server,
            "date"           : self.date,
            "hour"           : self.hour
        }

    def getDownloadSpeed(self):
        return self.download_speed;

    def getServer(self):
        return self.server;

    def getDate(self):
        return self.date;

    def getHour(self):
        return self.hour;