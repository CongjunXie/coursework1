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
    
#def test_hospital_vs_confirmed: #produces the expected output even when some values are missing
    
def test_generate_data_plot_confirm(): #throws a meaningful error when an input argument is not correct(e.g., sex=4)
    assert generate_data_plot_confirmed(data_er, sex=4) == 'Input sex is error'
    assert generate_data_plot_confirmed(data_er, max_ages=4) == 'Input max_age is error'

#def test_compute_running_average #works as expected with different window sizes (with even and oddsizes)