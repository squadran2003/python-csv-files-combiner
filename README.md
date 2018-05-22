# python-csv-files-combiner
script that combines multiple csv file into one

## Overview
The script uses the pandas library converting each csv file into a data frame and then concatenation each frame. 

## Dependencies
1) Python3
2) Pandas

## Installation
1)	To install python3 on windows :  https://www.python.org/downloads/windows/ and choose the latest release for python3. Once you install python, check that pip is also installed. You can type pip --version into the command line which will show you the version. If you get any other output, it means pip is not installed.

2) Intall pandas
```  pip install pandas ```

## Running the file
1)	Place the file combiner.py in the same directory as you csv files you want to combine
2)	Navigate to that directory via the command line. Note( You cannot use UNC paths in the command line) to overcome this use the command pushd, see below
3)	Type the command: python combiner.py . You can also supply a filename to the script. For example:  python combiner.py .  smart_220518.csv. Note ‘.’ Represents the current directory.
4)	Once done, type the command popd, this will get you back to your current directory.
