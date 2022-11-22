ElectionsScraper scrapes data from public server volby.cz and saves them into newly made .csv file

The code is capable of scraping regional data of 2017 Czech legislative elections, chosen by iser from the following link: 

    https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

    Specifically, the code scrapes the following data for every municipality in selected district: 
    
    Code of the municipality (kód obce)
    Name of the municipality (název obce)
    Number of voters (voliči v seznamu)
    Number of issued envelopes (vydané obálky)
    Number of legal votes (platné hlasy)
    List of candidate parties (kandidující strany)
   
All collected data are written into newly created .csv file.

Usage:

The script runs from command line.

 ~% python elscraper.py 'url_addres_of_the_district' csv_filename

, where:  
        python is the program executing script, 
        
        elscraper.py is name of the script,
        
        first argument is url address of scraped district. It can be accessed  by opening the link mentioned above: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ and clicking on any X symbol in column named "Výběr obce". 
     
    	second argument is name of future .csv file to be made. It is recommended to name it after okres(district) name for convenience.
    	
Usage example:

user@MacBook ~% python elscraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6205' olomouc
    	
An example file named "olomouc.csv" generated from the command above is enclosed.

