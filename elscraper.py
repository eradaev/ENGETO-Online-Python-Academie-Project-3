"""
projekt_3.py: treti projekt do Engeto Online Python Akademie

author: Evgeniy Radaev
email: eradaev@gmail.com
discord: Eugene_2022#3697
"""

import os
import sys
import csv
import requests
from bs4 import BeautifulSoup

url = "https://volby.cz/pls/ps2017nss/"

def main():
    os.system("clear")
    if len(sys.argv) != 3:
        print(f"Script '{sys.argv[0]}' requires two arguments to run. Please refer to readme.md file.")
        quit()
    elif not sys.argv[1].startswith('https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj'):
        print("Error! You have entered incorrect url. Please try again.")
        quit()
    else:
        print('Processing request...')


    link = get_url()
    filename = output_filename()

    f = open(filename + ".csv", mode="w")
    f_writer = csv.writer(f, delimiter=";")

    header = False
    data = requests.get(link)
    soup = BeautifulSoup(data.text, "html.parser")
    regions = soup.find_all("td", {"class": "cislo"})

    for line in regions:
        region_data = []
        region_data = get_id_name(line, region_data)
        region_soup = get_soup(url, line)

        region_results = region_soup.find(id="ps311_t1")
        region_data = get_voters(region_results, region_data)

        parties = region_soup.find(id="inner").find_all("tr")

        region_data = get_party_votes(parties, region_data)

        if not header:
            column_names = ["Kod obce", "Nazev obce", "Volici v seznamu", "Vydane obalky", "Platne hlasy"]
            for new_line in parties:
                if not new_line.find("th"):
                    column_names.append(new_line.find_all("td")[1].string)
            f_writer.writerow(column_names)
            header = True

        f_writer.writerow(region_data)

    f.close()
    print("Completed!")
    print(f"Output file {filename}.csv has been generated.")

def get_url():
    link = str(sys.argv[1])
    return link

def output_filename():
    name = sys.argv[2]
    if ".csv" not in name:
        return name
    else:
        print("Output filename should be without .csv extension!")
        quit()

def get_id_name(line, list):
    list.append(line.find("a").string)
    list.append(line.parent.find_all()[2].string)
    return list

def get_soup(URL, line):
    region_url = requests.get(URL + line.find("a").attrs["href"])
    return BeautifulSoup(region_url.text, "html.parser")

def get_voters(region_results, list):
    list.append(region_results.find("td", {"class": "cislo", "headers": "sa2"}).string)
    list.append(region_results.find("td", {"class": "cislo", "headers": "sa3"}).string)
    list.append(region_results.find("td", {"class": "cislo", "headers": "sa6"}).string)
    return list

def get_party_votes(parties, list):
    for line in parties:
        if not line.find("th"):
            list.append(line.find_all("td", {"class": "cislo"})[1].string)
    return list

if __name__ == '__main__':
    sys.exit(main())
