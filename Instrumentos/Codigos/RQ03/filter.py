import os
import json
import math
import datetime
import statistics
import matplotlib.pyplot as plt


def calc_quant(year):

    filename = str(year) + '_100K_questions.json'

    with open(filename, 'r') as file:
        data = file.read()
    
    objects = json.loads(data)

    sum_total = 0
    javascript = 0
    Go = 0
    Python = 0
    Java = 0
    other = 0
    RUST = 0

    for questions in objects: 
        sum_total += 1   
        if 'javascript' in questions['tags']:
            javascript += 1
        elif 'go' in questions['tags']:
            Go += 1
        elif 'python' in questions['tags']:
            Python += 1
        elif 'java' in questions['tags']:
            Java += 1
        elif 'rust' in questions['tags']:
            RUST += 1
        else: 
            other += 1

    
    data = {
        "Count_javascript" : javascript,
        "Count_go" : Go,
        "Count_Python" : Python,
        "Count_Java" : Java,
        "Count_RUST" : RUST,
        "Count_other": other,
        "Sum_total": sum_total
    }

    rust_perc = (data['Count_RUST']* 100)/data['Sum_total']
    print("Porcentagem de perguntas Rust = " , rust_perc ,"% - Valor total:", (1790000*rust_perc)/100)

    python_perc = (data['Count_Python']* 100)/data['Sum_total']
    print("Porcentagem de perguntas Python = " , python_perc ,"% - Valor total:", (1790000*python_perc)/100)

    Go_perc = (data['Count_go']* 100)/data['Sum_total']
    print("Porcentagem de perguntas go = " , Go_perc ,"% - Valor total:", (1790000*Go_perc)/100)

    javascript_perc = (data['Count_javascript']* 100)/data['Sum_total']
    print("Porcentagem de perguntas javascript = " , javascript_perc ,"% - Valor total:", (1790000*javascript_perc)/100)

    java_perc = (data['Count_Java']* 100)/data['Sum_total']
    print("Porcentagem de perguntas Java = " , java_perc ,"% - Valor total:", (1790000*java_perc)/100)

    other_perc = (data['Count_other']* 100)/data['Sum_total']
    print("Porcentagem de perguntas other = " , other_perc ,"% - Valor total:", (1790000*other_perc)/100)

    labels = ['RUST',   'Java', 'Python', 'GO','Outras', 'Javascript',]
    sizes = [rust_perc,java_perc, python_perc, Go_perc, other_perc,  javascript_perc,]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.3f%%')
    ax.axis('equal')

    plt.show()


def calc_frequency(year):
    calc_visibility("rust",year)
    calc_visibility("javascript",year)
    calc_visibility("go",year)
    calc_visibility("python",year)
    calc_visibility("java",year)

def calc_visibility(name,year):
            
            filename = str(year) + '/' + name + '_' + str(year) +'_questions.json'
            with open(filename, 'r') as file:
                    data = file.read()
        
            objects = json.loads(data)
            list_date_dif = []
            date_dif = 0
            int = 0
            date = datetime.datetime(2022, 4, 2, 23, 28, 29)
            reversed_data = list(reversed(objects))
            z_score_data = []
            for questions in reversed_data:
                    if int == 0 :
                        list_date_dif.append(date_dif)
                        date = datetime.datetime.utcfromtimestamp(questions['creation_date'])
                        int +=1
                    else: 
                        new_date = datetime.datetime.utcfromtimestamp(questions['creation_date'])
                        date_dif = (new_date - date).seconds
                        date = new_date
                        list_date_dif.append(date_dif/60)
                
            mean = statistics.mean(list_date_dif)
            stdev = statistics.stdev(list_date_dif)
            variance = statistics.variance(list_date_dif)

            for data in list_date_dif:
                z_score = (data - mean) / stdev
                z_score_data.append(z_score)
            
            count = 0
            for number in z_score_data:
                if number < -0.25:
                    count += 1

            percentage = count / len(z_score_data) * 100

            print(name, "media", mean)
            print(name, "variancia" ,variance)
            print(name ,"percentual frequencia", f"{percentage:.2f}% foram criadas frequentemente")

def calc_answer(year):
    filename = str(year) + '_100K_questions.json'

    with open(filename, 'r') as file:
        data = file.read()
    
        objects = json.loads(data)
    

    total = len(objects)
    rust_answer = 0
    rust_total = 0


    javascript_answer = 0
    javascript_total = 0

    python_answer = 0
    python_total = 0

    java_answer = 0
    java_total = 0

    go_answer = 0
    go_total = 0


    other_answer = 0
    others_total = 0
    for questions in objects:
        if 'rust' in questions['tags']:
            rust_total +=1
            if questions['is_answered'] is True:
                rust_answer += 1
        elif 'javascript' in questions['tags']:
            javascript_total +=1
            if questions['is_answered'] is True:
                javascript_answer += 1

        elif 'python' in questions['tags']:
            python_total +=1
            if questions['is_answered'] is True:
                python_answer += 1
        elif 'java' in questions['tags']:
            java_total +=1
            if questions['is_answered'] is True:
                java_answer += 1
        
        elif 'go' in questions['tags']:
            go_total +=1
            if questions['is_answered'] is True:
                go_answer += 1

        else:
            others_total +=1
            if questions['is_answered'] is True:
                other_answer +=1

    perc_rust = (rust_answer*100)/rust_total
    perc_javascript = (javascript_answer*100)/javascript_total
    perc_python = (python_answer*100)/python_total
    perc_java = (java_answer*100)/java_total
    perc_go = (go_answer*100)/go_total
    perc_normal = (other_answer*100)/others_total

    labels = ['RUST',  'GO',  'Python', 'Javascript', 'Outras', 'Java']
    sizes = [perc_rust, perc_go, perc_python, perc_javascript,  perc_normal, perc_java,]

    fig, ax = plt.subplots()
    ax.barh(labels, sizes)
    

    ax.set_xlabel('Percentuais')
    ax.set_ylabel('Linguagens')
    ax.set_title('Percentual de perguntas respondidas')

    plt.show()


    print("Porcentagem de questions respondidas de RUST ",perc_rust,"%")
    print("Porcentagem de questions respondidas de javascript ",perc_javascript,"%")
    print("Porcentagem de questions respondidas de python ",perc_python,"%")
    print("Porcentagem de questions respondidas de java ",perc_java,"%")
    print("Porcentagem de questions respondidas de go ",perc_go,"%")




    print("Porcentagem de questions respondidas de outras linguagens ",perc_normal,"%")


def get_data(type,year):

    filename = str(year) + '_100K_questions.json'

    with open(filename, 'r') as file:
        data = file.read()
    
        objects = json.loads(data)
        
    list = []
    for questions in objects:
        if type in questions['tags']:
            list.append(questions)
    
    filename = type + '_' + str(year) +"_questions.json"
    with open(filename, "w") as f:
        json.dump(list, f, indent=4)
        
def get_all_data(year):       
    get_data("rust",year)
    get_data("javascript",year)
    get_data("go",year)
    get_data("python",year)
    get_data("java",year)

def generate_pie_chart():

    labels = ['RUST',   'Java', 'Python', 'GO', 'Javascript',]
    sizes = [38.08, 36.95, 37.68, 37.46,  38.17,]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.2f%%')
    ax.axis('equal')

    plt.show()

def generate_sidebar():

    labels = ['java','Outras', 'javascript', 'python','go','rust']
    sizes = [39.01, 39.56, 42.08, 44.95 ,  50.0, 63.45]

    fig, ax = plt.subplots()
    ax.barh(labels, sizes)

    for i, v in enumerate(sizes):
        ax.text(v + 0.5, i, str(v), color='black', fontweight='bold')

    ax.set_xlabel('Percentuais (%)')
    ax.set_ylabel('Linguagens')
    ax.set_title('Percentual de perguntas respondidas')
    ax.set_xlim(right=max(sizes)+8)
    plt.show()


def generate_bar():

    categorias = ['Rust','Python', 'go', 'javascript','Java','other']
    valores = [0.64,15.46,0.52 , 10.29, 4.78 , 68.28]

    # Criação do gráfico de barras
    plt.bar(categorias, valores)

    for i, valor in enumerate(valores):
        plt.text(i, valor, str(valor), ha='center', va='bottom')


    # Personalização do gráfico
    plt.xlabel('Categorias')
    plt.ylabel('Valores %')
    plt.title('Gráfico de Barras')
    plt.grid(True)

    # Exibição do gráfico
    plt.show()
   

if __name__ == '__main__':
    # get_all_data(2022)
    # print("----------------------------------------------------------------------")
    #calc_frequency(2019)
    # print("----------------------------------------------------------------------")
    #calc_answer(2022)
    # print("----------------------------------------------------------------------")
    #calc_quant(2022)
    # generate_pie_chart()
    #generate_sidebar()
    generate_bar()
 
 
