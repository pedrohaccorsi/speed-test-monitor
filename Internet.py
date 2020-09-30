import speedtest;

class Internet():

    MEGABIT = 1048576;

    def __init__(self):
        try:
            self.speedTestHandler = speedtest.Speedtest();
        except:
            return

    def getDownloadSpeedInMegabits(self):
        return (self.speedTestHandler.download() / Internet.MEGABIT) if (self.speedTestHandler is not None) else 0

    def getBestServer(self):
        return self.speedTestHandler.get_best_server()["name"] if (self.speedTestHandler is not None) else ""
