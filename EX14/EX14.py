"""
Module can be used to make data from table into a picture.

author: Jaanus
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def read_file(filename):
    """Read a csv file without headings and seperated by a semicolon from stat ee."""
    content = []
    with open(filename) as file:
        for line in file:
            content.append(line.strip().split(';'))
    return content


def get_series(series):
    """Return requested data list."""
    content = read_file('RV021sm.csv')
    data = []
    for i in range(len(content)):
        if series == 'Vanuserühmad kokku':
            data.append(int(content[i][2]) + int(content[i][3]) + int(content[i][4]))
        elif series == '15-19':
            data.append(int(content[i][2]))
        elif series == '20-24':
            data.append(int(content[i][3]))
        elif series == '25-29':
            data.append(int(content[i][4]))
    return data


def save_plot(series_axis1, series_axis2, filename):
    """Salvestab etteantud andmejadadest moodustatud graafiku faili, mille nimi on ette antud argumendis „filename“."""
    if len(series_axis1) == 0 or len(series_axis1) != len(series_axis2):
        return
    years = [year for year in range(1965, 1965 + len(series_axis1))]
    fig, ax1 = plt.subplots()
    ax1.plot(years, series_axis1, 'ro')
    ax1.set_xlabel('year')
    ax1.set_ylabel('vanuserühmas inimeste arv', color='r')
    ax2 = ax1.twinx()
    series2 = []
    if sum(series_axis1) >= sum(series_axis2):
        for i in range(len(series_axis1)):
            series2.append(series_axis2[i] / series_axis1[i] * 100)
            label = 'jada 2 suhe jadaga 1'
    else:
        for i in range(len(series_axis1)):
            series2.append(series_axis1[i] / series_axis2[i] * 100)
            label = 'jada 1 suhe jadaga 2'
    ax2.plot(years, series2, 'b')
    ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f%%'))
    ax2.set_ylabel('{0}'.format(label), color='b')
    # plt.show()
    plt.savefig(filename)

if __name__ == '__main__':
    s1 = get_series('Vanuserühmad kokku')
    s2 = get_series('15-19')
    save_plot(s1, s2, 'series_JK')
