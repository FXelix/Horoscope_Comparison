
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

        self.star_sign = {"Aries": {"astrology": "horoscope/daily/aries.html",
                                    "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=1",
                                    }
                          }

        self.sign_input = ""

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
                self.sign_input = user_sign
                break


    def get_content(self):
        astrology_page = requests.get(self.astrology + self.star_sign[self.sign_input]["astrology"])
        horoscope_page = requests.get(self.horoscope + self.star_sign[self.sign_input]["horoscope"])

        try:
            astrology_page.raise_for_status()
            horoscope_page.raise_for_status()
        except Exception as exc:
            print("An Error occured: {}".format(exc))

        astrology_soup = bs4.BeautifulSoup(astrology_page.text, "html.parser")
        horoscope_soup = bs4.BeautifulSoup(horoscope_page.text, "html.parser")

        astrology_text = astrology_soup.select(".page-horoscope-text")
        horoscope_text = horoscope_soup.select(".horoscope-content p")

        print(astrology_text[0].getText())
        print(horoscope_text[0].getText())

#  TODO: Print pretty content

#  TODO: Add all star signs

#  TODO: Add more websites
