import requests


def train_search(fr, to, date, time):
    url = 'https://booking.uz.gov.ua/train_search/'
    r = requests.post(url,  data={'from': fr, 'to': to, 'date': date, 'time': time})
    return r.json()

if __name__ == '__main__':
    print(train_search(2200001, 2218000, '2019-07-11', '00:00'))
