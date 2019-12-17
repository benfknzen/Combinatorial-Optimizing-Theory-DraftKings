# Combinatorial-Optimizing-Theory-DraftKings
Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
Rules of DraftKings MMA: https://www.draftkings.com/help/rules/mma (find raw data that can be filtered under these rules of scoring)
Authors: Benjamin Zeng]

***Non coding part***

1. User downloads csv file off Draftkings and puts into appropriate folder
2. Update fighter_data.csv
3. Run this program
4. Upload csv back into Draftkings
5. Loop back to 1 till filthy rich


***main.py***

Execution

Implements all the code and returns a list with combination of lineups

Call csv_append.py in order to append fighter_data.csv with draftkings_mma_(date).csv
Filter data set with filter_data_set.py in optimal ways
Use fighter_data to write back into draftkings_mma_(date).csv



***csv_append.py***

Function

Appends two csv files together under naming unique identifier keys. Used to extend the parameters or dimensions of the keys so that csvscrape.py can import it into one dataset to be optimized. File fighterdata.csv  to be appended onto draftkings_mma_(date).csv



***fighter_data.csv***

Updated database to pull fighter information from
Some important dimensions, parameters, stats to consider are in
https://docs.google.com/spreadsheets/d/1oeB7p6j9w8a1rqpLD82Efzvy4raiLNkDvDxtYkHseoY/edit#gid=491163749
(reach, height, weight, age, etc)



***csv_scrape.py***

Function

User manually downloads csv draftkings_mma_(date).csv off their website and this will scrape and create objects of the relevant classes and puts them into a dataset python can filter.




***Fighter.py***

Class

Subset class of Player. Imports Player



***Player.py***

Class

Combinatorially adds more dimensions to our picks. To be used in conjunction with more definitive classes. Contains generic identification and attributes that all subclasses should contain



***filter_dataset.py***

Function

Manipulates data specific to our application. A more complex Pandas library.

Within this function there will be a Smart_filter which is a weighted approach towards finding optimal solutions while taking n-dimensional data. A neural network approach would be worth pursuing.

*From Probability based elimination: When filtering on probability based elimination it is important to focus gathering and using data relative to the rules of the game.  Then creating a strong data organizer and optimizer based off of this raw data, rather than secondary or n-th order data.


Thoughts 3.4.2019 Updated:

I have the sorting working for AvgPointsPerGame for each line up in descending order so priority lineup entry is possible

Default stat AvgPointsPerGame is a lagging indicator because it also accounts for fights where fighters lost, these numbers skew the potential future data. ---Instead the estimated PointsPerNextGame is defined as if the player wins. A linear regression model made from stats of previous WINS of both: the fighter we care to predict stats, and opponents of this fighter will be used for prediction for PointsPerNextGame analysis.
The relevant data taken should be relative to other opposing team's stats.

In MMA this would only be one opponent

In the game of basketball this synergistic approach accounts for all the players each our main Hero prediction and the team's actual teammates for the match.
The relevant data used to take into account should be relative to the contest rules
