

The program scrapes the data and metadata from the wiki page where the starting link is 'http://en.wikipedia.org/wiki/Big_data' and 10 random wiki pages are selected 
from the pages and those are followed to scrape the data and metadata out of it and stored in text document(.txt) files, and the page which being scraped is mentioned
on the top of the .txt file, the file is saved with the same name as the wiki page being scraped. If the data is needed in some other format it can be produced in 
other formats as well, according to the requirement.

The program is designed for python 2.7.9 and the librabries used are 'requests' and 'lxml'. 'requests' is used to make the HTTP connection and fetch data from the 
server while lxml is used to give a tree like structure to the webpage so that relevant can be extracted using xpath. Both the exyternal libraries are included in 
the zipped file and under the library folder.

The connection may cause the program the end abrubtly but that is just due to the internet connection. If such a problem arises then re-execute the program and it 
will execute normally.

The formattting can also be performed of the data but that can be made according to the requirement.