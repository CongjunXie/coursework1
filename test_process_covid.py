from process_covid import load_covid_data
from process_covid import cases_per_population_by_age
from process_covid import hospital_vs_confirmed
from process_covid import generate_data_plot_confirmed
from process_covid import create_confirmed_plot
from process_covid import compute_running_average
from process_covid import simple_derivative
from process_covid import count_high_rain_low_tests_days

from pathlib import Path
data_directory = Path("covid_data")
data_file = "ER-Mi-EV_2020-03-16_2020-04-24.json"
data_er = load_covid_data(data_directory / data_file)

#def tset_load_covid_data: #throws a meaningful error if the structure of the file doesn’t match with what’s expected.

def test_cases_per_population_by_age_cannot_rebin(): #negative test
    input_data = {'metadata':
    {'age_binning':
        {'population':['0-9', '10-19', '20-29', '30-39', '40-49', '50-'],
        'hospitalizations':['0-19', '20-39', '40-']}},
    'region':{'population':{'age':1000}},
    'evolution':{'2020-8-15':100,'2020-8-16':100}}

    assert cases_per_population_by_age(input_data) == 'Error'

def test_cases_per_population_by_age_rebin_1():
    input_data = {'metadata':
    {'age_binning':
        {'population':['0-9', '10-19', '20-29', '30-39', '40-49', '50-'],
        'hospitalizations':['0-19', '20-39', '40-']}},
    'region':{'population':{'age':[1,2,3,4,5,6]}},
    'evolution':{'2020-8-15':{'epidemiology':{'confirmed':{'total':{'age':[1,2,3]}}}},
                  '2020-8-16':{'epidemiology':{'confirmed':{'total':{'age':[4,5,6]}}}},
                 '2020-8-17':{'epidemiology':{'confirmed':{'total':{'age':[7,8,9]}}}}}}

    assert list(cases_per_population_by_age(input_data).keys()) == ['0-19', '20-39', '40-']

def test_cases_per_population_by_age_rebin_2():
    input_data = {'metadata':
    {'age_binning':
        {'population':['0-19', '20-39', '40-'],
        'hospitalizations':['0-9', '10-19', '20-29', '30-39', '40-49', '50-']}},
    'region':{'population':{'age':[1,2,3]}},
    'evolution':{'2020-8-15':{'epidemiology':{'confirmed':{'total':{'age':[1,2,3,4,5,6]}}}},
                  '2020-8-16':{'epidemiology':{'confirmed':{'total':{'age':[2,4,6,8,10,12]}}}},
                 '2020-8-17':{'epidemiology':{'confirmed':{'total':{'age':[3,2,5,8,1,6]}}}}}}
    
    assert list(cases_per_population_by_age(input_data).keys()) == ['0-19', '20-39', '40-']

def test_hospital_vs_confirmed(): #create a set of data myself and change the variables
    input_data = {'evolution':
    {'2020-03-16':
        {'hospitalizations':{'hospitalized':{'new':{'all':10}}},
        'epidemiology':{'confirmed':{'new':{'all':5}}}},
    '2020-03-17':
        {'hospitalizations':{'hospitalized':{'new':{'all':20}}},
        'epidemiology':{'confirmed':{'new':{'all':20}}}},
    '2020-03-18':
        {'hospitalizations':{'hospitalized':{'new':{'all':None}}},
        'epidemiology':{'confirmed':{'new':{'all':7}}}},
    '2020-03-19':
        {'hospitalizations':{'hospitalized':{'new':{'all':13}}},
        'epidemiology':{'confirmed':{'new':{'all':None}}}},   
    '2020-03-20':
        {'hospitalizations':{'hospitalized':{'new':{'all':12}}},
        'epidemiology':{'confirmed':{'new':{'all':0}}}}}}

    assert hospital_vs_confirmed(input_data) == (['2020-03-16','2020-03-17'],[2,1])

    input_data = {'evolution':
    {'2020-03-16':
        {'hospitalizations':{'hospitalized':{'new':{'all':None}}},
        'epidemiology':{'confirmed':{'new':{'all':None}}}},
    '2020-03-17':
        {'hospitalizations':{'hospitalized':{'new':{'all':20}}},
        'epidemiology':{'confirmed':{'new':{'all':20}}}},
    '2020-03-18':
        {'hospitalizations':{'hospitalized':{'new':{'all':3}}},
        'epidemiology':{'confirmed':{'new':{'all':7}}}},
    '2020-03-19':
        {'hospitalizations':{'hospitalized':{'new':{'all':13}}},
        'epidemiology':{'confirmed':{'new':{'all':None}}}},   
    '2020-03-20':
        {'hospitalizations':{'hospitalized':{'new':{'all':12}}},
        'epidemiology':{'confirmed':{'new':{'all':1}}}}}}
    assert hospital_vs_confirmed(input_data) == (['2020-03-17','2020-03-18','2020-03-20'],[1,3/7,12])
    
def test_incorrect_sex_generate_data_plot_confirm(): #throws a meaningful error when an input argument is not correct(e.g., sex=4)
    assert generate_data_plot_confirmed(data_er, sex=4) == 'Input sex is error'
    assert generate_data_plot_confirmed(data_er, sex='abc') == 'Input sex is error'
    assert generate_data_plot_confirmed(data_er, sex=(1,2,3)) == 'Input sex is error'

def test_incorrect_max_age_generate_data_plot_confirm():
    assert generate_data_plot_confirmed(data_er, max_ages=4) == 'Input max_age is error'
    assert generate_data_plot_confirmed(data_er, max_ages='abc') == 'Input max_age is error'
    assert generate_data_plot_confirmed(data_er, max_ages=(1,2,3)) == 'Input max_age is error'

def test_odd_compute_running_average(): #works as expected with different window sizes (with even and oddsizes)
    assert compute_running_average([1,2,3,4,5,6,7,8,9,10],7) == [None,None,None,4,5,6,7,None,None,None]
    assert compute_running_average([1,3,5,7,9,11,13],5) == [None,None,5,7,9,None,None]
    assert compute_running_average([1.5,2.6,3.4,4.9,5.1],3) == [None,2.5,3.6333333333333333,4.466666666666667,None]
    assert compute_running_average([0, 1, 5, 2, 2, 5],3) == [None, 2.0, 8/3, 3.0, 3.0, None]
    assert compute_running_average([2, None, 4],3) == [None,3,None]
    assert compute_running_average([0, 3, None, None, None, 6, 9], 3) == [None, 1.5, 3, None, 6, 7.5, None]

def test_even_compute_running_average():
    assert compute_running_average([1,2,3,4,5,6,7,8,9,10],8) == 'Input window is even, cannot be used to compute'
    assert compute_running_average([1,2,3,4,5,6,7,8],4) == 'Input window is even, cannot be used to compute'
    assert compute_running_average([1,2,3,4,5],2) == 'Input window is even, cannot be used to compute'

def test_simple_derivative():
    assert simple_derivative([1,2,3,4,5,6,7,8]) == [None,1,1,1,1,1,1,1]
    assert simple_derivative([None, 1, 2, None, 4]) == [None,None,1,None,None]