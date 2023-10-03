# Problem Set 3



This problem set has four components that must be submitted to Canvas:


**All components of this problem set are due on Canvas by Tuesday, October 10, by 11:59pm Boston time.**

---

### Getting started
Remember: one of the goals in this class is to become proficient in using a text editor, navigating a linux file system with unix commands, and running programs from a command line. I'd like you to do this assignment on cslab, and the easiest way to get all the files from here up to your account on cslab is to use git. 

1. Create an account on GitHub if you don't already have one: https://github.com/signup
2. Log into cslab.
3. Type the following command to "clone" this respository to your home directory on cslab.

```
git clone https://github.com/CSCI-2349-F23/ps3.git
```

4. Type `ls` and you'll see that you now have a directory in your home directory called `ps3`.

(For future problem sets, you'll just put a different URL after `git clone`. When viewing the repo in your web browser, click the green `Code` button in the upper right corner. This will display the URL, which you can copy and paste.)

5. If you `ls ps3`, you'll see that there are a few files and a `data` directory. In that directory are four subdirectories: `txt`, `csv`, `html`, and `xml`, each of which has a few files. You'll be using these files as input in the different parts of this problem set.

### Part 1: Bash scripting

1. Write a single line with multiple commands in unix that will do the following for the file `data/csv/movies.csv`: extract the 1st, 2nd, and 8th fields, upcase everything, pick out the lines that contain the phrase "OF THE", then sort alphabetically. You should have 29 lines, where the first 3 and last 3 lines are as shown below.

```
BATTLE OF THE YEAR,SONY,2013
BEASTS OF THE SOUTHERN WILD,FOX SEARCHLIGHT,2012
CLASH OF THE TITANS,WARNER BROS,2010
...
TRANSFORMERS: REVENGE OF THE FALLEN,PARAMOUNT,2009
UNDERWORLD: RISE OF THE LYCANS,SONY,2009
WRATH OF THE TITANS,WARNER BROS,2012
```

2. Create a bash script called `part1.sh`. Make sure the bash script has the important first line at the top. **Then paste in the command you wrote for #1 above.** Then run it from the terminal with `bash part1.sh` and make sure that it does the right thing.

3. Write a single line in unix that does the above for both csv files, then extracts just the first field (the movie or book title), then prints out how many time each movie or book title appears in both files, then sorts that by the number of times. **Add this line of code to `part.sh`.**

You should get 141 lines, and you should find exactly one book from the list that was made into a movie of the same name on this list.   These are the first and last three lines of my output:

```
      1 1811 DICTIONARY OF THE VULGAR TONGUE
      1 A DISCOURSE UPON THE ORIGIN AND THE FOUNDATION OF THE INEQUALITY AMONG MANKIND
      1 A GENERAL HISTORY OF THE PYRATES:: FROM THEIR FIRST RISE AND SETTLEMENT IN THE ISLAND OF PROVIDENCE TO THE PRESENT TIME
      ...
      1 UNDERWORLD: RISE OF THE LYCANS
      1 WRATH OF THE TITANS
      2 THE HOUND OF THE BASKERVILLES
```

4. Finally, at the end of `part1.sh`, use a `for` loop to go through each csv file, and for each file write out the output of the command you wrote for #1 to a new file whose name is the same as the input file but replacing `.csv` with `-caps-ofthe.csv`. For example, the output you got for #1 above applied to `movies.csv` be redirected to a file called `movies-caps-ofthe.csv`.



Sources for these csv files:
* https://corgis-edu.github.io/corgis/csv/classics/
* https://github.com/reisanar/datasets/blob/master/HollywoodMovies.csv


### Part 2: Try it in Python



### Part 3: HTML


### Part 4: XML


### Part 5: Combining Python with bash
