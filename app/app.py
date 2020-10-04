from time import sleep;
from Internet import *;
from Calendar import *;
from Snapshot import *;
from Excel    import *;

internet  = Internet();
calendar  = Calendar();
snapshots = [];

for i in range (0,200):
    sleep(60 * 5)
    snapshots.append(
        Snapshot(
            internet.getDownloadSpeedInMegabits(),
            internet.getBestServer(),
            calendar.getToday(),
            calendar.getNow()
        )
    ) 

Excel('speedtest-results').createChart(snapshots)

print("done!")