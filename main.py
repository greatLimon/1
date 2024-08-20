from datetime import datetime  
from application.salary import calculate_salary
from application.db.people import get_employees

import numpy as np
from bashplotlib.histogram import plot_hist

def my_func():
    arr = np.random.normal(size=1000, loc=0, scale=1)
    plot_hist(arr, bincount=50)

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now())
    my_func()
