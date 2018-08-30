import pandas
import sys
import matplotlib.pyplot as plt
import glob

def parse_arguments():
	'''
	Parses the command line argumetns and returns the appropriate list
	 of files
	
	Input:
	-------

	Returns:
	--------
		file_list : list of filenames (strings)
	'''
	arguments = sys.argv
	if len(arguments)==1:
		print('Usage: python gdp_plots <filename(s)> \n \
		or use -a for all gdp data in directory')
		exit()
	if arguments[1]=='-a':
		file_list = glob.glob('*gdp*.csv')
		if len(file_list)==0:
			print('no files in cwd')
			exit()
	else:
		file_list = sys.argv[1:]
	return file_list

def create_plots(file_list):
	'''
	creates plot of gdp data
	
	Inputs:
	------
		file_list
	Returns:
	-------
		Nothing -> sends plots to screen output
	'''
	for filename in file_list:
		data = pandas.read_csv(filename, index_col = 'country').T
		ax = data.plot(title=filename)
		ax.set_xlabel('Year')
		ax.set_ylabel('GDP per capita')
		ax.set_xticks(range(len(data.index)))
		ax.set_xticklabels(data.index, rotation=45)
		plt.show()

def main():
	file_list = parse_arguments()
	create_plots(file_list)
	
main()
