# FIXME add needed imports

def load_covid_data(filepath):
    import json
    return json,loads(open(filepath).read())

def cases_per_population_by_age(input_data):
    x=input_data['metadata']['age_binning']['population']
    y = input_data['region']['population']['age']
    z = input_data['evolution'].keys()
    l = input_data['metadata']['age_binning']['hospitalizations']

    if l == []:
        a = 'Error: No regions provided'
    elif list(set(x).intersection(set(l))) == []:
        a = 'Error: cannot rebin'
    elif all(y) == False:
        a = 'Error: no population provided'
    else:
        a = {}
        b = []

        for m in range(len(x)):
            a.update({x[m]:[]})
        for n in range(len(x)):
            b.append([])
        
        if len(x) > len(l):
            for k in range(len(l)):
                if x[k] != l[k]:
                    y[k] = [y[k][p]+y[k+1][p] for p in range(len(y[k]))]
            for i in range(len(x)):
                for j in range(len(z)):
                    c = input_data['evolution'][list(z)[j]]['epidemiology']['confirmed']['total']['age']
                    b[i].append(c[i]/y[i])
                    a[x[i]].append((list(z)[j],b[i][j]))
        elif len(x) < len(l):
            for i in range(len(x)):
                for j in range(len(z)):
                    c = input_data['evolution'][list(z)[j]]['epidemiology']['confirmed']['total']['age']
                    for q in range(len(l)):
                        if c[q] == None:
                            c[q] = 0
                    if x[i] != l[i]:
                        c[i] = c[i] + c[i+1]
                    b[i].append(c[i]/y[i])
                    a[x[i]].append((list(z)[j],b[i][j]))
        else:
            for i in range(len(x)):
                for j in range(len(z)):
                    c = input_data['evolution'][list(z)[j]]['epidemiology']['confirmed']['total']['age']
                    b[i].append(c[i]/y[i])
                    a[x[i]].append((list(z)[j],b[i][j]))
    return a

def hospital_vs_confirmed(input_data):
    x = input_data['metadata']['age_binning']['population'] #年龄段
    y = input_data['region']['population']['age'] #各年龄段总人数
    z = input_data['evolution'].keys() #年份
    f = []
    g = list(z)
    h = []
    o = []
    
    for i in range(len(z)):
        d = input_data['evolution'][list(z)[i]]['hospitalizations']['hospitalized']['new']['all']
        e = input_data['evolution'][list(z)[i]]['epidemiology']['confirmed']['new']['all']
        if e == 0 or e == None or d == None:
            f.append(None)
        else:
            f.append(d/e)
    
    for j in range(len(z)):
        if f[j] != None:
            h.append(f[j])
            o.append(g[j])
    
    r = (o,h)   
    return r

def generate_data_plot_confirmed(input_data, sex=False, max_age=[], status='total'):
    from datetime import datetime
    f=[]
    g=[]
    h=[]
    result=[]
    x = input_data['metadata']['age_binning']['population'] #年龄段
    y = input_data['region']['population']['age'] #各年龄段总人数
    z = input_data['evolution'].keys() #年份
    l = input_data['metadata']['age_binning']['hospitalizations'] #住院年龄段
    
    for i in range(len(max_ages)):
        h.append([])

    if sex == True:
        for i in range(len(z)):
            f.append(input_data['evolution'][list(z)[i]]['epidemiology']['confirmed'][status]['male'])
            g.append(input_data['evolution'][list(z)[i]]['epidemiology']['confirmed'][status]['female'])
    
        data_time = [datetime.strptime(d, '%Y-%m-%d').date() for d in list(z)]
        result = [data_time,f,data_time,g]
    
    elif max_ages != []:
        for m in range(len(z)):
            for i in range(len(max_ages)):
                for j in range(len(x)):
                    if max_ages[i] <= abs(eval(x[0]))*(j+1):
                        n = input_data['evolution'][list(z)[m]]['epidemiology']['confirmed'][status]['age']
                        
                        for q in range(len(l)):
                            if n[q] == None:
                                n[q] = 0
                        
                        h[i].append(sum(n[0:j+1]))
                        break
        for k in range(len(max_ages)):
            if h[k] == []:
                 for m in range(len(z)):
                    n = input_data['evolution'][list(z)[m]]['epidemiology']['confirmed'][status]['age']
                    h[k].append(sum(n))
        
        data_time = [datetime.strptime(d, '%Y-%m-%d').date() for d in list(z)]
    else:
        result = 'Error: No age regions provided'
    
    for i in range(len(max_ages)):
        result.append(data_time)
        result.append(h[i])
     
    return result

def create_confirmed_plot(input_data, sex=False, max_ages=[], status='total', save=False):
    from matplotlib import pyplot as plt
    x = input_data['metadata']['age_binning']['population'] #年龄段
    y = input_data['region']['population']['age'] #各年龄段总人数
    z = input_data['evolution'].keys() #年份
    
    # FIXME check that only sex or age is specified.
    fig = plt.figure(figsize=(10, 10))
    
    if sex == True:
        type = 'sex'
        a = generate_data_plot_confirmed(input_data, sex, max_ages, status)
        
        if status == 'total':
            plt.plot(a[0],a[1],color='green',label=status + ' male', linestyle='-')
            plt.plot(a[2],a[3],color='purple',label=status + ' female', linestyle='-')
        else:
            plt.plot(a[0],a[1],color='green',label=status + ' male', linestyle='--')
            plt.plot(a[2],a[3],color='purple',label=status + ' female', linestyle='--')    
    
    if sex != True and sex != False: #有待测试
        return "Input is error"
        
    if max_ages != []:
        type = 'age'
        a = generate_data_plot_confirmed(input_data, sex, max_ages, status)
        
        if status == 'total':
            for i in range(0,2*len(max_ages),2):
                if max_ages[int(i/2)] <= 25:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='green', linestyle='-')
                elif 25 < max_ages[int(i/2)] <= 50:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='orange', linestyle='-')
                elif 50 < max_ages[int(i/2)] <= 75:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='purple', linestyle='-')
                else:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='pink', linestyle='-')
        else:
            for i in range(0,2*len(max_ages),2):
                if max_ages[int(i/2)] <= 25:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='green', linestyle='--')
                elif 25 < max_ages[int(i/2)] <= 50:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='orange', linestyle='--')
                elif 50 < max_ages[int(i/2)] <= 75:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='purple', linestyle='--')
                else:
                    plt.plot(a[i],a[i+1],label=status + ' younger than ' + str(max_ages[int(i/2)]), color='pink', linestyle='--')  
    
    region = input_data['region']['name']
    fig.autofmt_xdate()  # To show dates nicely
    plt.title('Confirmed cases in ' + region) #???
    plt.xlabel('data')
    plt.ylabel('cases')
    plt.legend()
    
    if save == True:
        plt.savefig(region + '_evolution_cases_' + type + '.png') #???

    plt.show()

def compute_running_average(data, window):
    raise NotImplementedError

def simple_derivative(data):
    raise NotImplementedError

def count_high_rain_low_tests_days(input_data):
    raise NotImplementedError
