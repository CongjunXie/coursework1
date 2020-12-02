from process_covid import load_covid_data
from process_covid import cases_per_population_by_age
from process_covid import hospital_vs_confirmed
from process_covid import generate_data_plot_confirmed
from process_covid import create_confirmed_plot
from process_covid import compute_running_average
from process_covid import simple_derivative
from process_covid import count_high_rain_low_tests_days

#def tset_load_covid_data: #throws a meaningful error if the structure of the file doesn’t match with what’s expected.
    
#def test_hospital_vs_confirmed: #produces the expected output even when some values are missing
    
def test_generate_data_plot_confirm(): #throws a meaningful error when an input argument is not correct(e.g., sex=4)
    assert generate_data_plot_confirmed(data_er, sex=4) == 'Input sex is error'
    assert generate_data_plot_confirmed(data_er, max_ages=4) == 'Input max_age is error'

def test_compute_running_average(): #works as expected with different window sizes (with even and oddsizes)
    assert compute_running_average([1,2,3,4,5,6,7,8,9,10],7) == [None,None,None,4,5,6,7,None,None,None]
    assert compute_running_average([1,3,5,7,9,11,13],5) == [None,None,5,7,9,None,None]
    assert compute_running_average([1.5,2.6,3.4,4.9,5.1],3) == [None,2.5,3.6333333333333333,4.466666666666667,None]