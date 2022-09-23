import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime
forexc = pd.read_csv('Foreign Exchange software.csv')
forexc['Due date'] = forexc['Due date'].apply(pd.to_datetime, errors = 'coerce')
forexc['Custom field (Start date)'] = forexc['Custom field (Start date)'].apply(pd.to_datetime, errors = 'coerce')
forexc['diff_dates'] = forexc['Due date'] - forexc['Custom field (Start date)']
forexc['diff_dates'] = forexc['diff_dates']/np.timedelta64(1,'D')
for x in range(1000):
	forex = forexc.copy()
	percent_random = random.uniform(0, 2)
	if (random.uniform(0,2) > 1.0): 
		percent_sign = 2
	else:
		percent_sign =  -2

	percentage = percent_sign * percent_random
	forex['Transform_to_diff_date'] = forex['diff_dates'] * ( 1 + percentage )
	forex['Transform_to_diff_date'] = forex['Transform_to_diff_date'].apply(np.ceil)
#creating random due dates

	forex['Randomize_due_date'] = forex['Due date'] + pd.to_timedelta(forex['Transform_to_diff_date'], unit = 'd')
	forex.drop(columns=['Due date', 'diff_dates','Transform_to_diff_date'], inplace = True)
	forex['Due_date'] = forex['Randomize_due_date']
	forex.drop(columns=['Randomize_due_date'], inplace = True)
	if(percent_sign == -2):
		directory_name = './Due_date_bad_examples2/file{}.csv'.format(x)
		forex.to_csv(directory_name, index=False)
	else:
		directory_name = './Due_date_good_examples2/file{}.csv'.format(x)
		forex.to_csv(directory_name, index=False)