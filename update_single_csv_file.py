from writecsv import *	
from sys import argv

source = './source/'
destination = './destination/'
# print(argv)
update_single_csv_file(source, argv[1], argv[2])
move_single_csv_file(source, destination, argv[1])
print('Writing complete')