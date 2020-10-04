import xlsxwriter
from Snapshot import *;

class Excel():

    def __init__(self, file_name):
        self.workbook  = xlsxwriter.Workbook(file_name+'.xlsx')
        self.worksheet = self.workbook.add_worksheet()

    def createChart(self, snapshots):
        headings = ['Date', 'Hour', 'Server', 'Speed(Mbits)']
        data     = [ [], [], [], [] ]

        for snapshot in snapshots:
            data[0].append(snapshot.getDate())
            data[1].append(snapshot.getHour())
            data[2].append(snapshot.getServer())
            data[3].append(snapshot.getDownloadSpeed())

        chart1 = self.workbook.add_chart({'type': 'line'})
        chart1.set_size({'width': 80*len(data[0]), 'height': 300})

        self.worksheet.write_row('A1', headings)
        self.worksheet.write_column('A2', data[0])
        self.worksheet.write_column('B2', data[1])
        self.worksheet.write_column('C2', data[2])
        self.worksheet.write_column('D2', data[3])

        chart1.add_series({
            'name':       'Speed(Mbits)',
            'categories': f'=Sheet1!$B$2:$C${len(data[2])+1}',
            'values':     f'=Sheet1!$D$2:$D${len(data[3])+1}',
            'trendline': {'type': 'moving_average', 'period': 2}
        })

        chart1.set_title ({'name': 'Speedtest'})
        chart1.set_x_axis({'name': 'server locale/timestamp'})
        chart1.set_y_axis({'name': 'speed (Mbits)'})
        chart1.set_style(10)

        self.worksheet.insert_chart('E2', chart1, {'x_offset': 25, 'y_offset': 10})
        self.workbook.close()