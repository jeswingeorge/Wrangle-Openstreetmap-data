# Wrangle-Openstreetmap-data
Project work as part of Udacity Data Analyst nanodegree course

Softwares used : Python v2.7 and sqlite3

In this project data wrangling on OSM file of New-Delhi, India is done. The OSM file is downloaded from the following links :
* https://www.openstreetmap.org/node/16173236
* https://mapzen.com/data/metro-extracts/metro/new-delhi_india/

The downloaded file will be in compressed state, it is extracted to get a OSM file of larger size. The OSM file hence downloaded 
__new-delhi_india.osm__ will be quiet large size and is difficult to read using a text editor. So the file size is reduced to make it 
readable and get an idea of the data to be wrangled.

This repository consists of the following files : 

- __1.Project_report.md__ : This is the final report of the work done on this project.

 __2.Final_code.ipynb__ : This file contains the codes for gathering and extracting the data from the OSM file. The data is then cleaned 
as per the programmer's requirements. Also the cleaned data is stored in CSV files.

- __2.csvs_to_database.ipynb__ : Using the code in this file, each of the CSV files is exported as tables to be stored in a database. Using 
these database we perform the sql queries.

- __3.link.txt__ : Contains the links to to the map position.

- __sample_delhi.osm__ : This smaller file can aid the programmer in understanding the data involved and the basic structure of the code.
The programmer can start working on these smaller samples of OSM files and then proceed to work on the larger OSM file.

- __5.References.txt__ : Contains a list of Web sites, forums, blog posts, etc referred to in this submission 





 


