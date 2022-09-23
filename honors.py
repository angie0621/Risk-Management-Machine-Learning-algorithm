import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime
forexc = pd.read_csv('Foreign Exchange Software.csv')
forexc['Due date'] = forexc['Due date'].apply(pd.to_datetime, errors = 'coerce')
forexc['Custom field (Start date)'] = forexc['Custom field (Start date)'].apply(pd.to_datetime, errors = 'coerce')
forexc['diff_dates'] = forexc['Due date'] - forexc['Custom field (Start date)']
forexc['diff_dates'] = forexc['diff_dates']/np.timedelta64(1,'D')

forexc['diff_time_spent'] = forexc['Original estimate'] - forexc['Time Spent']
for x in range(1500):
	forex = forexc.copy()
	forex['Random_Assignee'] = np.random.choice(forex['Assignee'], size = 20, replace = True, p = [.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,])
	forex['percent_random'] = np.random.uniform(0, 2, forex.shape[0])
	forex['percent_sign'] = forex['percent_random'].apply(lambda x: 2 if x > 0.2 else -2)
	forex['percentage'] = forex['percent_sign'] * forex['percent_random']
	forex['Transform_to_diff_date'] = forex['diff_dates'] * ( 1 + forex['percentage'] )
	forex['Transform_to_diff_date'] = forex['Transform_to_diff_date'].apply(np.ceil)
#creating random due dates

	forex['Randomize_due_date'] = forex['Due date'] + pd.to_timedelta(forex['Transform_to_diff_date'], unit = 'd')
	forex.drop(columns=['Due date', 'Transform_to_diff_date'], inplace = True)
	forex['Due date'] = forex['Randomize_due_date']
	forex.drop(columns=['Randomize_due_date'], inplace = True)
	forex['Label'] = forex['percent_sign'].apply(lambda x: 1 if x == -2 else 0 )

	forex['percent_random_time_spent'] = np.random.uniform(0,2,forex.shape[0])
	forex['percent_sign_time_spent'] = forex['percent_random_time_spent'].apply(lambda x: 2 if x > 0.2 else -2)
	forex['percentage_time_spent'] =  forex['percent_sign_time_spent'] *forex['percent_random_time_spent']
	forex['Random_time_spent'] = forex['diff_time_spent'] * (1 + forex['percentage_time_spent'])
	forex['Time Spent'] = forex['Random_time_spent']
	forex['diff_time_spent'] = forex['Original estimate'] - forex['Time Spent']

	forex['Label'] = forex['percent_sign_time_spent'].apply(lambda x: 1 if x == -2 else 0 )
	forex.to_csv('./Storing_csv_files_3/{}.csv'.format(x))
