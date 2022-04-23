# Help Tom with his analysis of a recent local congressional election on behalf of the Colorado Board of Elections.

## Gather the following information:
- total number of votes in the election
- a list of all candidates who received votes in the election
- total number of votes per candidate
- total percentage of votes per candidate
- winner based on the popular vote

## Resources
Source: election_results.csv<br>
Output: election_analysis.txt<br>
Written in: <i>Python 3.10.2 via VSCode 1.66.2</i><br>

## Dependencies
In order to work with the supplied csv file we needed to import two modules. The <code>csv</code> module has a function called <code>reader</code> which will allow us to iterate over each row in the file and read each of those rows. The <code>os</code> module has a function called <code>path</code> that will allow us to both read from the locally stored csv file as well as write to a locally stored txt file for output.

