import requests
import bs4
from datetime import datetime
from bs4 import BeautifulSoup
from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%d %H:%M'
UPDATE_DELAY = 1  # 60 * 60 * 12
GROUP = '341'
sched_page = ''
k = 0


class Subject:
    def __init__(self, cell_tag: bs4.element.Tag, subj_date):  # Initialize when created
        self.__cell = cell_tag

        metadata = cell.find(attrs={'class': 'rasp-table-inner-cell-hidden'})
        self.duration = ' '.join(metadata.contents[-1].split())
        subj = cell.find(attrs={'class': 'subject-m'})
        if not subj:
            subj = cell.find(attrs={'class': 'subject'})
        style = cell.find(attrs={'class': 'type'})
        self.title = subj.contents[0].strip()
        self.type = style.text.strip()
        self.date = subj_date

    def __str__(self):
        return f"{self.duration}: {self.title}{self.type}"


class colomns:
    def __init__(self):
        date = head.find(attrs={'class': 'rasp-table-inner-cell'}).text.strip()
        self.date = date


def my_filter(entry):
    if type(entry) == bs4.element.NavigableString:
        return not str.isspace(entry)
    return True


with open('rasp_page.html', 'r+', encoding="utf-8") as f:
    last_update_time = datetime.strptime(f.readline().strip(), DATETIME_FORMAT)
    offset = datetime.now() - last_update_time
    if offset.seconds >= UPDATE_DELAY:
        sched_page = requests.get('http://rasp.sstu.ru/group/{}'.format(GROUP)).text
        f.write(sched_page)
    else:
        sched_page = f.read()
    f.write("\n")

is_vacation = lambda x: len(list(filter(my_filter, x.find(attrs={'class': 'rasp-table-inner-cell'}).contents))) == 0

rasp = BeautifulSoup(sched_page, 'html.parser').find(attrs={'class': 'rasp-table'})
cols = rasp.find_all(attrs={'class': 'rasp-table-col'})

subjects = []

for col in cols:
    head = col.find(attrs={'class': 'rasp-table-row-header'})

    print('=======================')
    print(date)
    print('=======================')
    cells = col.find_all(attrs={'class': 'rasp-table-row'})
    inner = cells[2].find(attrs={'class': 'rasp-table-inner-cell'}).contents
    for cell in cells:
        if is_vacation(cell):
            continue
        subjects.append(Subject(cell, date))
        print(subjects[-1])
