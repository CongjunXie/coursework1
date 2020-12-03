def load_covid_data(filepath):
    import json
    data = json.loads(open(filepath).read())
    z = data['evolution'].keys() #years

    if sorted(list(data.keys())) != sorted(['metadata', 'region', 'evolution']):
        return 'Error1'
    elif sorted(list(data['metadata'].keys())) != sorted(['time-range', 'age_binning']):
        return 'Error2'
    elif sorted(list(data['metadata']['time-range'].keys())) != sorted(['start_date', 'stop_date']):
        return 'Error3'
    elif sorted(list(data['metadata']['age_binning'].keys())) != sorted(['hospitalizations', 'population']):
        return 'Error'
    elif sorted(list(data['region'].keys())) != sorted(['name', 'key', 'latitude', 'longitude', 'elevation', 'area', 'population', 'open_street_maps', 'noaa_station', 'noaa_distance']):
        return 'Error'
    elif sorted(list(data['region']['area'].keys())) != sorted(['total', 'rural', 'urban']):
        return 'Error'
    elif sorted(list(data['region']['population'].keys())) != sorted(['total', 'male', 'female', 'age', 'rural', 'urban']):
        return 'Error'
    else:
        pass
    
    for i in range(len(z)):
        if sorted(list(data['evolution'][list(z)[i]].keys())) != sorted(['hospitalizations', 'epidemiology', 'weather', 'government_response']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations'].keys())) != sorted(['hospitalized', 'intensive_care', 'ventilator']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['hospitalized'].keys())) != sorted(['new', 'total', 'current']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['hospitalized']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['hospitalized']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['hospitalized']['current'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['intensive_care'].keys())) != sorted(['new', 'total', 'current']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['intensive_care']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['intensive_care']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['intensive_care']['current'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['ventilator'].keys())) != sorted(['new', 'total', 'current']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['ventilator']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['ventilator']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['hospitalizations']['ventilator']['current'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology'].keys())) != sorted(['confirmed', 'deceased', 'recovered', 'tested']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['confirmed'].keys())) != sorted(['new', 'total']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['confirmed']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['confirmed']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['deceased'].keys())) != sorted(['new', 'total']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['deceased']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['deceased']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['recovered'].keys())) != sorted(['new', 'total']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['recovered']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['recovered']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['tested'].keys())) != sorted(['new', 'total']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['tested']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['epidemiology']['tested']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['weather'].keys())) != sorted(['temperature', 'rainfall', 'snowfall', 'dew_point', 'relative_humidity']):
            return 'Error'
        elif sorted(list(data['evolution'][list(z)[i]]['weather']['temperature'].keys())) != sorted(['average', 'min', 'max']):
            return 'Error'
        else:
            return data   

def cases_per_population_by_age(input_data):
    class SchemeError(Exception):
        pass
    
    if input_data == 'Error':
        raise SchemeError
    else:
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
    z = input_data['evolution'].keys()
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
    x = input_data['metadata']['age_binning']['population']
    y = input_data['region']['population']['age']
    z = input_data['evolution'].keys()
    l = input_data['metadata']['age_binning']['hospitalizations']

    if sex == True:
        for i in range(len(z)):
            f.append(input_data['evolution'][list(z)[i]]['epidemiology']['confirmed'][status]['male'])
            g.append(input_data['evolution'][list(z)[i]]['epidemiology']['confirmed'][status]['female'])
    
        data_time = [datetime.strptime(d, '%Y-%m-%d').date() for d in list(z)]
        result = [data_time,f,data_time,g]

        result=[]
        result.append({'date':data_time,'value':f})
        result.append({'date':data_time,'value':g})

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

        result=[]
        for i in range(len(max_ages)):
            result.append({'date':data_time,'value':h[i]})
            
    else:
        result = 'Input max_age is error'
     
    return result

def create_confirmed_plot(input_data, sex=False, max_ages=[], status='total', save=False):
    from matplotlib import pyplot as plt
    x = input_data['metadata']['age_binning']['population']
    y = input_data['region']['population']['age']
    z = input_data['evolution'].keys()
    
    fig = plt.figure(figsize=(10, 10))
    
    if sex == True:
        r = 'sex'
        a = generate_data_plot_confirmed(input_data, sex, max_ages, status)
        
        if status == 'total':
            plt.plot('date','value',data=a[0],color='green',label=status + ' male', linestyle='-')
            plt.plot('date','value',data=a[1],color='purple',label=status + ' female', linestyle='-')
        else:
            plt.plot('date','value',data=a[0],color='green',label=status + ' male', linestyle='--')
            plt.plot('date','value',data=a[1],color='purple',label=status + ' female', linestyle='--')   
    
    elif sex != True and sex != False:
        return "Input sex is error"
        
    elif type(max_ages).__name__ == 'list' and len(max_ages) >= 1:
        r = 'age'
        a = generate_data_plot_confirmed(input_data, sex, max_ages, status)
        
        if status == 'total':
            for i in range(0,len(max_ages)):
                if max_ages[i] <= 25:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='green', linestyle='-')
                elif 25 < max_ages[i] <= 50:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='orange', linestyle='-')
                elif 50 < max_ages[i] <= 75:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='purple', linestyle='-')
                else:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='pink', linestyle='-')
        else:
            for i in range(0,len(max_ages)):
                if max_ages[i] <= 25:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='green', linestyle='--')
                elif 25 < max_ages[i] <= 50:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='orange', linestyle='--')
                elif 50 < max_ages[i] <= 75:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='purple', linestyle='--')
                else:
                    plt.plot('date','value',data=a[i],label=status + ' younger than ' + str(max_ages[i]), color='pink', linestyle='--')
    else:
        return "Input age_max is error"
    
    region = input_data['region']['name']
    fig.autofmt_xdate()  # To show dates nicely
    plt.title('Confirmed cases in ' + region)
    plt.xlabel('data')
    plt.ylabel('cases')
    plt.legend()
    
    if save == True:
        plt.savefig(region + '_evolution_cases_' + r + '.png')

    plt.show()

def compute_running_average(data, window):
    # data is a list and window is odd
    a = int((window+1)/2)
    b = a-1
    c = len(data)-a 
    d = []
    f = []
    
    if window%2 == 0:
        d = 'Input window is even, cannot be used to compute'
    else:
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

def count_high_rain_low_tests_days(input_data,window=7):
    a = []
    b = []
    c = []
    d = []
    e = int((window+1)/2)
    
    x = input_data['metadata']['age_binning']['population']
    y = input_data['region']['population']['age']
    z = input_data['evolution'].keys()
    
    if window%2 == 0:
        ratio = 'Input window is even, cannot be used to compute'
    else:
        for i in range(len(z)):
            a.append(input_data['evolution'][list(z)[i]]['weather']['rainfall'])
            b.append(input_data['evolution'][list(z)[i]]['epidemiology']['tested']['new']['all'])
     
        a1 = compute_running_average(a, window)
        b1 = compute_running_average(b, window)
    
        a2 = simple_derivative(a1)
        b2 = simple_derivative(b1) 
    
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
