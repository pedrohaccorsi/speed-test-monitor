from time import sleep;
from Internet import *;
from Calendar import *;
from Snapshot import *;

internet = Internet();
calendar = Calendar();

snapshots = [];

for i in range (0,50):
    snapshots.append(
        Snapshot(
            internet.getDownloadSpeedInMegabits(),
            internet.getBestServer(),
            calendar.getToday(),
            calendar.getNow()
        )
    )


import xlsxwriter

workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Date', 'Hour', 'Server', 'Speed(Mbits)']
dates    = []
hours    = []
servers  = []
speeds   = []

for snapshot in snapshots:
    dates.append(snapshot.getDate())
    hours.append(snapshot.getHour())
    servers.append(snapshot.getServer())
    speeds.append(snapshot.getDownloadSpeed())

data = [ dates, hours, servers, speeds ]

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])
worksheet.write_column('D2', data[3])

# Create a new chart object. In this case an embedded chart.
chart1 = workbook.add_chart({'type': 'line'})

max = 0
for speed in data[3]:
    if speed > max:
        speed = max

gap    = int(max / 10)
values = []

for speed in range(0, max):
    values.append(speed)
    speed = (speed + gap) if speed + gap <= max else max



# Configure the first series.
chart1.add_series({
    'name':       'Speed(Mbits)',
    'categories': '=Sheet1!$A$2:$C$999',
    'values':     values
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Results of sample analysis'})
chart1.set_x_axis({'name': 'server locale/timestamp'})
chart1.set_y_axis({'name': 'speed (Mbits)'})

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(10)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('E2', chart1, {'x_offset': 25, 'y_offset': 10})

workbook.close()