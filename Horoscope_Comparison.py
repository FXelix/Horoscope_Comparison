
"""
This script is about learning requests and BeautifulSoup to scrape websites.
This script is about your daily horoscope from 3 different websites:
1. https://www.astrology.com/
2. https://www.horoscope.com/us/index.aspx
3. http://astrostyle.com/daily-horoscopes/

I dont't believe in astrology nor do I affiliate with those website. This script just compares their
statements about your specific daily horoscope.
"""


import requests
import bs4


class HoroscopeComparison:
    # base URLs
    def __init__(self):
        self.astrology = "https://www.astrology.com/"
        self.horoscope = "https://www.horoscope.com/us/"
        self.astrostyle = "http://astrostyle.com/daily-horoscopes/"

        self.star_sign = {"Aries": {"astrology": "horoscope/daily/aries.html",
                                    "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=1",
                                    "astrostyle": "aries-daily-horoscope/"}
                          }

    def user_input(self):
        while True:
            try:
                user_sign = input("Enter your star sign: ")
                if user_sign not in self.star_sign:
                    raise ValueError
            except ValueError:
                print("Enter a valid star sign.")
                continue
            else:
                return user_sign

    def get_content(self):
        astrology_page = requests.get(self.astrology + self.star_sign[self.user_input()]["astrology"])
        horoscope_page = requests.get(self.horoscope + self.star_sign[self.user_input()]["horoscope"])
        astrostyle_page = requests.get(self.astrostyle + self.star_sign[self.user_input()]["astrostyle"])

        try:
            astrology_page.raise_for_status()
            horoscope_page.raise_for_status()
            astrostyle_page.raise_for_status()
        except Exception as exc:
            print("An Error occured: {}".format(exc))

        astrology_soup = bs4.BeautifulSoup(astrology_page.text, "html.parser")
        horoscope_soup = bs4.BeautifulSoup(horoscope_page.text, "html.parser")
        astrostyle_soup = bs4.BeautifulSoup(astrology_page.text, "html.parser")

        astrology_text = astrology_soup.select(".page-horoscope-text")
        horoscope_text = horoscope_soup.select(".horoscope-content p")
        astrostyle_text = astrostyle_soup.select(".weekday_div p")



#  TODO: Select today's horoscope-text with BeautifulSoup

#  TODO: Display content to user
