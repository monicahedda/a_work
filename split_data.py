import csv
import os


def read_file_by_line(file_name, size, dir_name):
	in_file = open(file_name, 'r')
        in_reader = csv.reader(in_file) 

	i = 0

	create_directory(dir_name) #create directory for smaller files

	file_name = file_name.replace('.csv', '')
	out_file_name = dir_name + '/' + file_name + str(i) + '.csv'

	is_full = False
	
	for row in in_reader:
	    is_full = check_file_size(out_file_name, size)
	    if not is_full:
	        is_full = write_line_to_file(row, out_file_name)
	    else:
		i = i + 1
		out_file_name = dir_name + '/' + file_name + str(i) + '.csv'
		write_line_to_file(row, out_file_name)

	print 'Created ', i , ' smaller files.'


def create_directory(dir_name):
	try:
    	    os.makedirs(dir_name)
	except OSError:
    	    pass


def write_line_to_file(row, out_file_name):
	out_file = open(out_file_name, 'a')
	n_writer = csv.writer(out_file)
	n_writer.writerow(row)
	out_file.close()


def check_file_size(out_file_name, size):
	if os.path.isfile(out_file_name):
        	file_info = os.stat(out_file_name)
		size_in_MB = convert_bytes(file_info.st_size, 'MB')
		#print 'size_in_MB=',size_in_MB
        	if size_in_MB >= size:
            	    return True
        	else:
            	    return False
	else:
		return False 


def convert_bytes(num, type):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['KB', 'MB', 'GB', 'TB']:
	if x == type:
            num = num/1024.0
	    return num
	else:
	    num = num/1024.0

def main():
	read_file_by_line('CUSTOMER.csv', 16, 'CUSTOMER') # enter filename, size in MB here, 
	#print convert_bytes(10000000, 'MB') 

if __name__ == '__main__':
    main()
