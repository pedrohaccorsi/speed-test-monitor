import speedtest;

class Internet():

    MEGABIT = 1048576;
 
    def getDownloadSpeedInMegabits(self):
        try:
            return (speedtest.Speedtest().download() / Internet.MEGABIT) 
        except:
            return 0

    def getBestServer(self):
        try:
            return speedtest.Speedtest().get_best_server()["name"] 
        except:
            return 'not connectd'
