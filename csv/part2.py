# import some helpful libraries
import sys
import glob
import re

# get the list of files ending in csv
csvfiles = glob.glob("*.csv")

# for each of those csv files
for inputfile in csvfiles:

    # create the name for the corresponding output file
    outputfile = re.sub(".csv", "-caps-ofthe.csv", inputfile)
    outputfile = "caps_files/" + outputfile

    # with your input file is open...
    with open(inputfile) as f:

        # with the output file is open...
        with open(outputfile, "w") as g:

            # write out the text of the input file in all caps
            # to the output file
            g.write(f.read().upper())

# The syntax I use above is different from what I used in class. 
# Using with open()  makes it so you don't have to close the 
# files with close() later on. 


