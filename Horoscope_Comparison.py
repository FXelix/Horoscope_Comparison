
"""
This script is about learning requests and BeautifulSoup to scrape websites.
This script is about your daily horoscope from 3 different websites:
1. https://www.astrology.com/
2. https://www.horoscope.com/us/index.aspx
3. http://astrostyle.com/daily-horoscopes/

I dont't believe in astrology nor do I affiliate with those website. This script just compares their
statements about your specific daily horoscope.
"""


class HoroscopeComparison:
    # base URLs
    astrology = "https://www.astrology.com/"
    horoscope = "https://www.horoscope.com/us/"
    astrostyle = "http://astrostyle.com/daily-horoscopes/"

    star_sign = {"Aries": {"astrology": "",
                           "horoscope": "",
                           "astrostyle": ""}
                 }

    def user_input(self):
        while True:
            try:
                user_sign = input("Enter your star sign: ")
                if user_sign not in HoroscopeComparison.star_sign:
                    raise ValueError
            except Exception as exc:
                print("Enter a valid star sign.")
                continue
            else:
                return user_sign

#  TODO: Ask for valid star sign

#  TODO: Scrape websites with requests

#  TODO: Select today's horoscope-text with BeautifulSoup

#  TODO: Display content to user
