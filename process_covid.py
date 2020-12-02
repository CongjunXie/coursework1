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
    raise NotImplementedError

def generate_data_plot_confirmed(input_data, sex, max_age, status):
    """
    At most one of sex or max_age allowed at a time.
    sex: only 'male' or 'female'
    max_age: sums all bins below this value, including the one it is in.
    status: 'new' or 'total' (default: 'total')
    """
    raise NotImplementedError

def create_confirmed_plot(input_data, sex=False, max_ages=[], status=..., save=...):
    # FIXME check that only sex or age is specified.
    fig = plt.figure(figsize=(10, 10))
    # FIXME change logic so this runs only when the sex plot is required
    for sex in ['male', 'female']:
        # FIXME need to change `changeme` so it uses generate_data_plot_confirmed
        plt.plot('date', 'value', changeme)
    # FIXME change logic so this runs only when the age plot is required
    for age in max_ages:
        # FIXME need to change `changeme` so it uses generate_data_plot_confirmed
        plt.plot('date', 'value', changeme)
    fig.autofmt_xdate()  # To show dates nicely
    # TODO add title with "Confirmed cases in ..."
    # TODO Add x label to inform they are dates
    # TODO Add y label to inform they are number of cases
    # TODO Add legend
    # TODO Change logic to show or save it into a '{region_name}_evolution_cases_{type}.png'
    #      where type may be sex or age
    plt.show()

def compute_running_average(data, window):
    raise NotImplementedError

def simple_derivative(data):
    raise NotImplementedError

def count_high_rain_low_tests_days(input_data):
    raise NotImplementedError
