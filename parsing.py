import requests as rq
from bs4 import BeautifulSoup as bbs

import unicodedata


class Parsing:
    count = 1

    def __init__(self):
        self.all_movie_data = []

    @staticmethod
    def get_url_data(baseurl):
        # Hit on a given url and fetch data
        res = rq.get(baseurl)
        res_data = None
        if res:
            res_data = bbs(res.text, "html.parser")

        return res, res_data

    def parse_movie_list(self, baseurl="https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"):
        # Movie List,Link and additional info parsing
        try:
            _, res_data = self.get_url_data(baseurl)
        except:
            res_data = None
            print("Webpage did not responding")

        if res_data:
            table_data = res_data.find(
                "table", {"class": "wikitable sortable"})
            row_data = table_data.findAll("tr")[1:]

            primary_link = "https://en.wikipedia.org"
            if row_data:
                for i in row_data:
                    cell_data = i.findAll("td")
                    if cell_data:
                        try:
                            link = primary_link + cell_data[0].find("a")["href"]
                        except:
                            link = None
                        film, year, awards, nomination = [
                            j.text.strip() for j in cell_data]
                        temp = {"Link": link, "Film": film, "Year": year,
                                "Awards": awards, "Nomination": nomination}
                        if link:
                            temp = self.parse_movie(temp["Link"], temp)
                        else:
                            temp["Link"] = "Not available"

                        temp["_id"] = Parsing.count
                        self.all_movie_data.append(temp)
                        Parsing.count += 1

    def parse_movie(self, baseurl, temp=None):
        # Specific Movie detail info parsing
        if temp is None:
            temp = {}
        try:
            _, res_data = self.get_url_data(baseurl)
        except:
            res_data = None
            print("Webpage did not responding")

        if res_data:
            table_data = res_data.find("table", {"class": "infobox vevent"})
            if table_data:
                row_data = table_data.findAll("tr")
                if row_data:
                    for i in row_data:
                        key = i.find("th")
                        value = i.find("td")
                        if key:
                            if value:
                                key = key.text.strip()
                                value = value.text.strip().split("\n")
                                temp_val = []
                                for j in value:
                                    j = unicodedata.normalize(
                                        "NFKD", j.split("[")[0].strip())
                                    if j:
                                        temp_val.append(j)

                                not_allow = ''''/\."$*<>:|?'''
                                for i in not_allow:
                                    key = key.replace(i, "")
                                key = key.strip()

                                if key:
                                    temp[key] = ", ".join(temp_val)
        return temp

    def __getitem__(self, index):
        # Access data like dictionary. Such as obj[0]
        return self.all_movie_data[index]
