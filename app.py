import speedtest;

MEGABIT = 1048576;

speedTestHandler = speedtest.Speedtest();

print( speedTestHandler.download() / MEGABIT      );
print( speedTestHandler.get_best_server()["name"] );

