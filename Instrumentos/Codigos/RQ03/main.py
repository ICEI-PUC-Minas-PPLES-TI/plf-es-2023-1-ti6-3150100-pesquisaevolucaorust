import requests
import json
import time

import datetime


url = 'https://api.stackexchange.com/2.3/questions'




def get_stackData(year):

    
    inicio = int(datetime.datetime(year, 1, 1).timestamp())
    fim = int(datetime.datetime(year, 12, 31).timestamp())

    params = {
    'key' :'1HsxJIJmPA)Y4sxXoaP01A((',
    'page': 1,
    'pagesize': 100,
    'order': 'desc',
    'sort': 'creation',
    'site': 'stackoverflow',
    'fromdate': inicio,
    'todate': fim
}

    questions = []
    i=0
    
    for page in range(1, 1001):
        retry = True
        while retry: 
            params['page'] = page
            response = requests.get(url, params=params)
            if response.status_code == 200:
                retry = False
                questions += response.json()['items']
                i+= 1
                print(i)
                if(i%100== 0):
                    print(i/1000,"% das perguntas obtidas")
            else:
                print("Timeout 10 min")
                time.sleep(360)
       
    filename = str(year) + "_100K_questions.json" 
    with open(filename, "w") as f:
        json.dump(questions, f, indent=4)

if __name__ == '__main__':
    get_stackData(2022)