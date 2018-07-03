from writecsv import *	

source = './source/'
destination = './destination/'
loop_and_update_all_csv_files(source)
move_all_csv_files(source, destination)
print('Writing complete')