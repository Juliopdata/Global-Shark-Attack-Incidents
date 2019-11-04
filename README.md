# <p align="center"> Global-Shark-Attack-Incidents</p>


  <p align="center"> <img  src="https://github.com/Juliopdata/Global-Shark-Attack-Incidents/blob/master/SRC/JAWS-poster.jpg"></p>


<p align="center">Data complied by the global shark attacks file</p>


---

## Overview

The goal of this project is to combine everything I have learned about data wrangling, cleaning, and manipulation with Pandas so I can see how it all works together. For this project, I start with a messy data set Shark Attack. I need to import it, use my data wrangling skills to clean it up, prepare it to be analyzed, and then export it as a clean CSV data file.

## Hypothesis

**Are USA citizens the favourite food of de common shark?**

**Is there any country landlocked with sharks attacks?**

**It was more easy to die die a Dog attack than by Shark attack in 1989**

## Project structure

The project folder is structured in the following way:

* __main.ipynb__ : contains the notebook with the calculums and all the explanations about my research.

* __INPUT__ : Folder where the dataset should be placed in csv format.

* __OUTPUT__ : Folder that contains the cleaned datasets after clenaing an analysis.

* __SRC__: Folder that concains the file functions.py with all the auxiliar functios used in our project.

## Data import process

The first step in this project is to import the data from the provided .csv file to a pandas DataFrame.

In this case the .csv file provided is nos codified in utf-8, so it has been to import it with the parameter encode='iso-8859-1'.

## Cleaning and analyzing

1- Exploring the original dataset

2- Start the cleaning process using my data wrangling skills, includes:
    - Deleting not useful columns
    - Dealing with missing values 
    - Fixing the column names 
    - Importing functions to clean
    - Fixing columns values
    - Deleting rows with unknown values
    - Checking duplicates.
    

3- Exploring the clean dataset with graphics:
    - Countries of the attacks
    - Years
    - Sex of the victims
    - Casualties




## Conclusions

    - Usa is the country with more sharks attacks.
    - Florida is the area where there are more attacks.
    - The 2000 years are the years with most sharks attacks.
    - Uruguay with no Sea have at least One shark attack.
    - In 1989 same number of people die by Dogs and Sharks attacks.
    



## Useful Resources

* [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
* [Pandas Tutorials](https://pandas.pydata.org/pandas-docs/stable/tutorials.html)
* [StackOverflow Pandas Questions](https://stackoverflow.com/questions/tagged/pandas)
* [Awesome Public Data Sets](https://github.com/awesomedata/awesome-public-datasets)
* [Kaggle Data Sets](https://www.kaggle.com/datasets)



