# SMB Credit Score Calculator
This repository contains a set of scripts that can be used for roughly evaluating the creditworthiness of a small business. To run the script:

`python main.py`

##Screenshots
Running the script will take you through a series of prompts for information about the business in question:

![intro](http://i.imgur.com/SIrZm0E.png)

It will prompt using drop-down menus as well, as seen below:

![drop-down](http://i.imgur.com/nfBaejF.png)

After a few questions, it will spit out a rough approximation of a business' creditworthiness on a scale of 0-1:

![final output](http://i.imgur.com/0PRT1rb.png)

##How it works
The program works by taking a weighted average of 5 factors that can be indicators of good credit:

1. **Company Yelp score** - a score based on the number and quality of Yelp reviews a company receives
2. **Industry score** - a score based on the volatility of the company's industry
3. **Size score** - a score based on the size of the company
4. **Owner score** - a score based on the creditworthiness of the company owner (just a placeholder for now)
5. **URL score** - a score based on the trustworthiness of the company's website (just a placeholder for now)

For more details as to how these scores are calculated, see the relevant source code (there's a separate file for each scoring procedure).

##Navigating the source
The two most important files are the following:

1. **user_inputs.py** - contains the scripts for prompting and validating all user input.
2. **score_aggregator.py** - calls each of the individual scoring routines and aggregates them into one score.

The file **main.py** simply calls **user_inputs.py**, which gathers all data about the company and returns a company object (the company class can be found in the **company_info.py** file). Then, **score_aggregator.py** is used to calculate and print a score for the company.
