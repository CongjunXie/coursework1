def load_covid_data(filepath):
    import json
    data = json.loads(open(filepath).read())
    date = data['evolution'].keys()
    
    class SchemeError(Exception):
        pass

    if sorted(list(data.keys())) != sorted(['metadata', 'region', 'evolution']):
        raise SchemeError('Scheme is not valid')
    elif sorted(list(data['metadata'].keys())) != sorted(['time-range', 'age_binning']):
        raise SchemeError('Scheme is not valid')
    elif sorted(list(data['metadata']['time-range'].keys())) != sorted(['start_date', 'stop_date']):
        raise SchemeError('Scheme is not valid')
    elif sorted(list(data['metadata']['age_binning'].keys())) != sorted(['hospitalizations', 'population']):
        raise SchemeError('Scheme is not valid')
    elif sorted(list(data['region'].keys())) != sorted(['name', 'key', 'latitude', 'longitude', 'elevation', 'area', 'population', 'open_street_maps', 'noaa_station', 'noaa_distance']):
        raise SchemeError('Scheme is not valid')
    elif sorted(list(data['region']['area'].keys())) != sorted(['total', 'rural', 'urban']):
        raise SchemeError('Scheme is not valid')
    elif sorted(list(data['region']['population'].keys())) != sorted(['total', 'male', 'female', 'age', 'rural', 'urban']):
        raise SchemeError('Scheme is not valid')
    else:
        pass
    
    for i in range(len(date)):
        if sorted(list(data['evolution'][list(date)[i]].keys())) != sorted(['hospitalizations', 'epidemiology', 'weather', 'government_response']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations'].keys())) != sorted(['hospitalized', 'intensive_care', 'ventilator']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['hospitalized'].keys())) != sorted(['new', 'total', 'current']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['hospitalized']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['hospitalized']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['hospitalized']['current'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['intensive_care'].keys())) != sorted(['new', 'total', 'current']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['intensive_care']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['intensive_care']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['intensive_care']['current'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['ventilator'].keys())) != sorted(['new', 'total', 'current']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['ventilator']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['ventilator']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['hospitalizations']['ventilator']['current'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology'].keys())) != sorted(['confirmed', 'deceased', 'recovered', 'tested']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['confirmed'].keys())) != sorted(['new', 'total']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['confirmed']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['confirmed']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['deceased'].keys())) != sorted(['new', 'total']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['deceased']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['deceased']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['recovered'].keys())) != sorted(['new', 'total']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['recovered']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['recovered']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['tested'].keys())) != sorted(['new', 'total']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['tested']['new'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['epidemiology']['tested']['total'].keys())) != sorted(['all', 'male', 'female', 'age']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['weather'].keys())) != sorted(['temperature', 'rainfall', 'snowfall', 'dew_point', 'relative_humidity']):
            raise SchemeError('Scheme is not valid')
        elif sorted(list(data['evolution'][list(date)[i]]['weather']['temperature'].keys())) != sorted(['average', 'min', 'max']):
            raise SchemeError('Scheme is not valid')
        else:
            return data   

def cases_per_population_by_age(input_data):
    age_binning_p = input_data['metadata']['age_binning']['population']
    age_population = input_data['region']['population']['age']
    date = input_data['evolution'].keys()
    age_binning_h = input_data['metadata']['age_binning']['hospitalizations']

    class rangeError(Exception):
        pass

    if age_binning_h == []:
        raise rangeError('No age_binning provided')
    elif list(set(age_binning_p).intersection(set(age_binning_h))) == []:
        raise rangeError('Can not be rebin')
    elif all(age_population) == False:
        raise rangeError('No age_population provided')
    else:
        a = {}
        b = []

        for m in range(len(age_binning_p)):
            a.update({age_binning_p[m]:[]})
            b.append([])
        
        if len(age_binning_p) > len(age_binning_h):
            for k in range(len(age_binning_h)):
                if age_binning_p[k] != age_binning_h[k]:
                    age_population[k] = [age_population[k][p]+age_population[k+1][p] for p in range(len(age_population[k]))]

            for i in range(len(age_binning_p)):
                for j in range(len(date)):
                    c = input_data['evolution'][list(date)[j]]['epidemiology']['confirmed']['total']['age']
                    b[i].append(c[i]/age_population[i])
                    a[age_binning_p[i]].append((list(date)[j],b[i][j]))

        elif len(age_binning_p) < len(age_binning_h):
            for i in range(len(age_binning_p)):
                for j in range(len(date)):
                    c = input_data['evolution'][list(date)[j]]['epidemiology']['confirmed']['total']['age']

                    for q in range(len(age_binning_h)):
                        if c[q] == None:
                            c[q] = 0
                                
                    if age_binning_p[i] != age_binning_h[i]:
                        c[i] = c[i] + c[i+1]
                    b[i].append(c[i]/age_population[i])
                    a[age_binning_p[i]].append((list(date)[j],b[i][j]))
        else:
            for i in range(len(age_binning_p)):
                for j in range(len(date)):
                    c = input_data['evolution'][list(date)[j]]['epidemiology']['confirmed']['total']['age']
                    b[i].append(c[i]/age_population[i])
                    a[age_binning_p[i]].append((list(date)[j],b[i][j]))
    return a

def hospital_vs_confirmed(input_data):
    date = input_data['evolution'].keys()
    g = list(date)
    f = []
    h = []
    o = []
    
    for i in range(len(date)):
        d = input_data['evolution'][list(date)[i]]['hospitalizations']['hospitalized']['new']['all']
        e = input_data['evolution'][list(date)[i]]['epidemiology']['confirmed']['new']['all']
        if e == 0 or e == None or d == None:
            f.append(None)
        else:
            f.append(d/e)
    
    for j in range(len(date)):
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
    age_binning_p = input_data['metadata']['age_binning']['population']
    date = input_data['evolution'].keys()
    age_binning_h = input_data['metadata']['age_binning']['hospitalizations']

    class InputError(Exception):
        pass

    if sex == True:
        for i in range(len(date)):
            f.append(input_data['evolution'][list(date)[i]]['epidemiology']['confirmed'][status]['male'])
            g.append(input_data['evolution'][list(date)[i]]['epidemiology']['confirmed'][status]['female'])
    
        data_time = [datetime.strptime(d, '%Y-%m-%d').date() for d in list(date)]
        result = [data_time,f,data_time,g]

        result=[]
        result.append({'date':data_time,'value':f})
        result.append({'date':data_time,'value':g})

    elif sex != False:
        raise InputError('Input sex is not valid')
    
    elif type(max_age).__name__ == 'list' and len(max_age) >= 1:
        for i in range(len(max_age)):
            h.append([])

        for m in range(len(date)):
            for i in range(len(max_age)):
                for j in range(len(age_binning_p)):
                    if max_age[i] <= abs(eval(age_binning_p[0]))*(j+1):
                        n = input_data['evolution'][list(date)[m]]['epidemiology']['confirmed'][status]['age']
                        
                        for q in range(len(age_binning_h)):
                            if n[q] == None:
                                n[q] = 0
                        
                        h[i].append(sum(n[0:j+1]))
                        break

        for k in range(len(max_age)):
            if h[k] == []:
                 for m in range(len(date)):
                    n = input_data['evolution'][list(date)[m]]['epidemiology']['confirmed'][status]['age']
                    h[k].append(sum(n))
        
        data_time = [datetime.strptime(d, '%Y-%m-%d').date() for d in list(date)]

        result=[]
        for i in range(len(max_age)):
            result.append({'date':data_time,'value':h[i]})
            
    else:
        raise InputError('Input max_age is not valid')
     
    return result

def create_confirmed_plot(input_data, sex=False, max_ages=[], status='total', save=False):
    from matplotlib import pyplot as plt
        
    class InputError(Exception):
        pass

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
        raise InputError('Input sex is not valid')
        
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
        raise InputError('Input max_ages is not valid')
    
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
    
    class InputError(Exception):
        pass

    if window%2 == 0:
        raise InputError('Input window is even, cannot be used to compute')
    else:
        for i in range(len(data)):
            f.append([])
    
        for i in range(0,b):
            d.append(None)
        
        for i in range(b,c+1):
            e = data[i-a+1:i+a]
            o = sum(p is None for p in e)
        
            if window-o == 0:
                d.append(None)
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
    date = input_data['evolution'].keys()

    class InputError(Exception):
        pass

    if window%2 == 0:
        raise InputError('Input window is even, cannot be used to compute')
    else:
        for i in range(len(date)):
            a.append(input_data['evolution'][list(date)[i]]['weather']['rainfall'])
            b.append(input_data['evolution'][list(date)[i]]['epidemiology']['tested']['new']['all'])
     
        a1 = a # weather don't need to be averaged
        b1 = compute_running_average(b, window)
    
        a2 = simple_derivative(a1)
        b2 = simple_derivative(b1) 

        for i in range(0,e):
            c.append(False)
        for i in range(e,len(date)-e+1):
            if a2[i] > 0:
                c.append(True)
            else:
                c.append(False)
    
        c1 = sum(c)
        
        if c1 == 0:
            ratio = 0
        else:
            
            for i in range(0,e):
                d.append(False)
    
            for i in range(e,len(date)-e+1):
                if a2[i] > 0 and b2[i] < 0:
                    d.append(True)
                else:
                    d.append(False)
        
            for i in range(len(date)-e+1,len(date)):
                d.append(False)
    
            d1 = sum(d)
    
            ratio = d1/c1
        
    return ratio
