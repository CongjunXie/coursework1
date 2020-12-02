# FIXME add needed imports

def load_covid_data(filepath):
    import json
    return json.loads(open(filepath).read())

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

def generate_data_plot_confirmed(input_data, sex=False, max_ages=[], status='total'):
    from datetime import datetime
    f=[]
    g=[]
    h=[]
    result=[]
    x = input_data['metadata']['age_binning']['population'] #年龄段
    y = input_data['region']['population']['age'] #各年龄段总人数
    z = input_data['evolution'].keys() #年份
    l = input_data['metadata']['age_binning']['hospitalizations'] #住院年龄段

    if sex == True:
        for i in range(len(z)):
            f.append(input_data['evolution'][list(z)[i]]['epidemiology']['confirmed'][status]['male'])
            g.append(input_data['evolution'][list(z)[i]]['epidemiology']['confirmed'][status]['female'])
    
        data_time = [datetime.strptime(d, '%Y-%m-%d').date() for d in list(z)]
        result = [data_time,f,data_time,g]

        for i in range(len(max_ages)):
            result.append(data_time)
            result.append(h[i])

    elif sex != False:
        result = 'Input sex is error'
    
    elif type(max_ages).__name__ == 'list' and len(max_ages) >= 1:
        for i in range(len(max_ages)):
            h.append([])

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

        for i in range(len(max_ages)):
            result.append(data_time)
            result.append(h[i])
    else:
        result = 'Input max_age is error'
     
    return result

def create_confirmed_plot(input_data, sex=False, max_ages=[], status='total', save=False):
    from matplotlib import pyplot as plt
    x = input_data['metadata']['age_binning']['population'] #年龄段
    y = input_data['region']['population']['age'] #各年龄段总人数
    z = input_data['evolution'].keys() #年份
    
    # FIXME check that only sex or age is specified.
    fig = plt.figure(figsize=(10, 10))
    
    if sex == True:
        r = 'sex'
        a = generate_data_plot_confirmed(input_data, sex, max_ages, status)
        
        if status == 'total':
            plt.plot(a[0],a[1],color='green',label=status + ' male', linestyle='-')
            plt.plot(a[2],a[3],color='purple',label=status + ' female', linestyle='-')
        else:
            plt.plot(a[0],a[1],color='green',label=status + ' male', linestyle='--')
            plt.plot(a[2],a[3],color='purple',label=status + ' female', linestyle='--')    
    
    if sex != False: #有待测试
        return "Input sex is error"
        
    if type(max_ages).__name__ == 'list' and len(max_ages) >= 1:
        r = 'age'
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
    else:
        return "Input age_max is error"
    
    region = input_data['region']['name']
    fig.autofmt_xdate()  # To show dates nicely
    plt.title('Confirmed cases in ' + region) #???
    plt.xlabel('data')
    plt.ylabel('cases')
    plt.legend()
    
    if save == True:
        plt.savefig(region + '_evolution_cases_' + r + '.png') #???

    plt.show()

def compute_running_average(data, window):
    # data is a list and window is odd
    a = int((window+1)/2)
    b = a-1
    c = len(data)-a 
    d = []
    f = []
    
    for i in range(len(data)):
        f.append([])
    
    for i in range(0,b):
        d.append(None)
        
    for i in range(b,c+1):
        e = data[i-a+1:i+a]
        o = sum(p is None for p in e)
        
        if window-o == 0:
            d.append(0)
        else:
            for j in range(i-a+1,i+a):
                if data[j] == None:
                    f[i].append(0)
                else:
                    f[i].append(data[j])
                
            d.append(sum(f[i])/(window-o))
    
    for i in range(c+1,len(data)):
        d.append(None)
        
    return d

def simple_derivative(data):
    # data is a list
    a = []
    
    a.append(None)
    
    for i in range(1,len(data)):
        e = data[i-1:i+1]
        o = sum(p is None for p in e)
        
        if o > 0:
            a.append(None)
        else:
            a.append(data[i]-data[i-1])
    
    return a


def simple_derivative(data):
    # data is a list
    a = []
    
    a.append(None)
    
    for i in range(1,len(data)):
        e = data[i-1:i+1]
        o = sum(p is None for p in e)
        
        if o > 0:
            a.append(None)
        else:
            a.append(data[i]-data[i-1])
    
    return a


def count_high_rain_low_tests_days(input_data,window=7):
    a = [] #降水
    b = [] #检查人数
    c = []
    d = []
    #不用专门设置变量？？
    e = int((window+1)/2)
    
    x = input_data['metadata']['age_binning']['population'] #年龄段
    y = input_data['region']['population']['age'] #各年龄段总人数
    z = input_data['evolution'].keys() #年份
    
    for i in range(len(z)):
        a.append(input_data['evolution'][list(z)[i]]['weather']['rainfall'])
        b.append(input_data['evolution'][list(z)[i]]['epidemiology']['tested']['new']['all'])
     
    a1 = compute_running_average(a, window)
    b1 = compute_running_average(b, window)
    
    a2 = simple_derivative(a1)
    b2 = simple_derivative(b1) 
    
    # 降水上升
    for i in range(0,e):
        c.append(False)
    
    for i in range(e,len(z)-e+1):
        if a2[i] > 0:
            c.append(True)
        else:
            c.append(False)
        
    for i in range(len(z)-e+1,len(z)):
        c.append(False)
    
    c1 = sum(c)
        
    if c1 == 0:
        ratio = 0
    else:
        # test人数下降
        for i in range(0,e):
            d.append(False)
    
        for i in range(e,len(z)-e+1):
            if a2[i] > 0 and b2[i] < 0:
                d.append(True)
            else:
                d.append(False)
        
        for i in range(len(z)-e+1,len(z)):
            d.append(False)
    
        d1 = sum(d)
    
        ratio = d1/c1
        
    return ratio
