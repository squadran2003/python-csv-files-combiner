import sys
import os
import pandas as pd

	
	
print("Please Wait ........")
#path comes from system argument in the cmd line
path = sys.argv[1]
filename = None
try:
	filename = sys.argv[2]
except IndexError:
	filename = 'COMBINED_FILES.csv'

# filter out only csv files
filenames = [f for f in os.listdir(path) if f.endswith('csv')]



data_frame = pd.DataFrame([])
frames = []

for file in filenames:
	named_file = pd.read_csv(file, encoding = "ISO-8859-1")
	df = pd.DataFrame(named_file)
	# adding the filename to a field filename
	df['filename']= file
	frames.append(df)
	results = pd.concat(frames)


results.to_csv(filename,index=False)
print("Complete ......")






