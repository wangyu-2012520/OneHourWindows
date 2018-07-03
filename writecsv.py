import csv
from datetime import datetime, timedelta
import os
import shutil

def read_windows(filename, input_limit = 0):
	#define local variables
	is_update_needed = 0
	updateData = [["WindowId", "Day", "Session", "Method", "Start Date", "End Date", "Fulfilment Centre", "Fulfilment Type", "Start Time", "End Time", "Web Cutoff Day", "Web Cutoff Time", "Pickup Day", "Pickup Time", "Region", "Limit", "IsDelete"]]

	with open(filename) as csvFile:
		reader = csv.DictReader(csvFile)
		for row in reader:
			WindowId = row['WindowId']
			Day = row['Day']
			Session = row['Session'] 
			Method = row['Method']
			Start_Date = row['Start Date']
			End_Date = row['End Date']
			Fulfilment_Centre = row['Fulfilment Centre']
			Fulfilment_Type = row['Fulfilment Type']
			Start_Time = row['Start Time']
			End_Time = row['End Time']
			Web_Cutoff_Day = row['Web Cutoff Day']
			Web_Cutoff_Time = row['Web Cutoff Time']
			Pickup_Day = row['Pickup Day']
			Pickup_Time = row['Pickup Time']
			Region = row['Region']
			IsDelete = row['IsDelete']

			if input_limit == 0:
				Limit = row['Limit']
			else:
				Limit = input_limit

			# convert Start_Time, End_Time, Pickup_Time from string to datetime
			Start_Time = datetime.strptime(Start_Time, '%H:%M')
			End_Time = datetime.strptime(End_Time, '%H:%M')
			Pickup_Time = datetime.strptime(Pickup_Time, '%H:%M')

			# calculate hours difference
			hours_difference = abs(Start_Time - End_Time).total_seconds() / 3600.0
			is_default_window = 0

			while hours_difference > 0:

				# add one hour window to start time as end time (this step is necessary to have correct date-time type in csv file)
				End_Time = Start_Time + timedelta(hours=1)

				# convert start time, end time to string
				Start_Time = format(Start_Time, '%H:%M')
				End_Time = format(End_Time, '%H:%M')
				Pickup_Time = format(Pickup_Time, '%H:%M')

				# default windows will keep the windowsID; new windows will have windowID as 0
				if is_default_window == 0:
					updateData.append([WindowId, Day, Session, Method, Start_Date, End_Date, Fulfilment_Centre, Fulfilment_Type, Start_Time, End_Time, Web_Cutoff_Day, Web_Cutoff_Time, Pickup_Day, Pickup_Time, Region, Limit, IsDelete])
				else:
					updateData.append(['0', Day, Session, Method, Start_Date, End_Date, Fulfilment_Centre, Fulfilment_Type, Start_Time, End_Time, Web_Cutoff_Day, Web_Cutoff_Time, Pickup_Day, Pickup_Time, Region, Limit, IsDelete])

				# convert Start_Time from string to datetime & add Pickup_Time to extra 1 minute
				Start_Time = datetime.strptime(End_Time, '%H:%M')
				Pickup_Time = datetime.strptime(Pickup_Time, '%H:%M')
				Pickup_Time = Pickup_Time + timedelta(minutes=1)

				# update variables
				is_update_needed = 1
				is_default_window = 1
				hours_difference = hours_difference - 1
			
		print(updateData)
	return updateData, is_update_needed

def update_windows(filename, inputData, is_update_needed):
	if is_update_needed == 1:
		csvFile = open(filename, 'w')
		with csvFile:
			writer = csv.writer(csvFile)
			writer.writerows(inputData)


def update_single_csv_file(directory, filename, limit = 40):
	if filename.endswith(".csv"): 
		# print(os.path.join(directory, filename))
		updateData, is_update_needed = read_windows(directory + filename, limit)
		update_windows(directory + filename, updateData, is_update_needed)	

def move_single_csv_file(source, destination, filename):
	if filename.endswith(".csv"): 
		shutil.move(source + filename, destination)



def loop_and_update_all_csv_files(directory):
	for filename in os.listdir(directory):
		if filename.endswith(".csv"): 
			# print(os.path.join(directory, filename))
			updateData, is_update_needed = read_windows(directory + filename)
			update_windows(directory + filename, updateData, is_update_needed)
		else:
			continue

def move_all_csv_files(source, destination):
	for filename in os.listdir(source):
		if filename.endswith(".csv"): 
			shutil.move(source + filename, destination)
		else:
			continue