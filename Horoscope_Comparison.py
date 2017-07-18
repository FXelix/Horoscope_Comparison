
"""
This script is about learning requests and BeautifulSoup to scrape websites.
This script is about your daily horoscope from 3 different websites:
1. https://www.astrology.com/
2. https://www.horoscope.com/us/index.aspx
3. "https://www.tarot.com/daily-horoscope/"

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
        self.tarot = "https://www.tarot.com/daily-horoscope/"

        # matching Star signs to URL snippets
        self.star_sign = {"aries": {"astrology": "horoscope/daily/aries.html",
                                    "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=1",
                                    "tarot": "aries",
                                    },
                          "taurus": {"astrology": "horoscope/daily/taurus.html",
                                     "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=2",
                                     "tarot": "taurus",
                                     },
                          "gemini": {"astrology": "horoscope/daily/gemini.html",
                                     "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=3",
                                     "tarot": "gemini",
                                     },
                          "cancer": {"astrology": "horoscope/daily/cancer.html",
                                     "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=4",
                                     "tarot": "cancer",
                                     },
                          "leo":    {"astrology": "horoscope/daily/leo.html",
                                     "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=5",
                                     "tarot": "leo",
                                     },
                          "virgo":  {"astrology": "horoscope/daily/virgo.html",
                                     "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=6",
                                     "tarot": "",
                                     },
                          "libra":  {"astrology": "horoscope/daily/libra.html",
                                     "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=7",
                                     "tarot": "libra",
                                     },
                          "scorpio": {"astrology": "horoscope/daily/scorpio.html",
                                      "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=8",
                                      "tarot": "scorpio",
                                      },
                          "sagittarius": {"astrology": "horoscope/daily/sagittarius.html",
                                          "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=9",
                                          "tarot": "sagittarius",
                                          },
                          "capricorn": {"astrology": "horoscope/daily/capricorn.html",
                                        "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=10",
                                        "tarot": "capricorn",
                                        },
                          "aquarius": {"astrology": "horoscope/daily/aquarius.html",
                                       "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=11",
                                       "tarot": "aquarius",
                                       },
                          "pisces": {"astrology": "horoscope/daily/pisces.html",
                                     "horoscope": "horoscopes/general/horoscope-general-daily-today.aspx?sign=12",
                                     "tarot": "pisces",
                                     },
                          }

        self.sign_input = ""

    def user_input(self):
        while True:
            try:
                user_sign = input("Enter your star sign: ")
                if user_sign.lower() not in self.star_sign:
                    raise ValueError
            except ValueError:
                print("Enter a valid star sign.")
                continue
            else:
                self.sign_input = user_sign
                break

    def get_content(self):
        # download the website
        astrology_page = requests.get(self.astrology + self.star_sign[self.sign_input]["astrology"])
        horoscope_page = requests.get(self.horoscope + self.star_sign[self.sign_input]["horoscope"])
        tarot_page = requests.get(self.tarot + self.star_sign[self.sign_input]["tarot"])

        try:
            # check if website is reachable
            astrology_page.raise_for_status()
            horoscope_page.raise_for_status()
            tarot_page.raise_for_status()
        except Exception as exc:
            print("An Error occured: {}".format(exc))

        # parse HTML with bs4
        astrology_soup = bs4.BeautifulSoup(astrology_page.text, "html.parser")
        horoscope_soup = bs4.BeautifulSoup(horoscope_page.text, "html.parser")
        tarot_soup = bs4.BeautifulSoup(tarot_page.text, "html.parser")

        #selecht specific text element
        astrology_text = astrology_soup.select(".page-horoscope-text")
        horoscope_text = horoscope_soup.select(".horoscope-content p")
        tarot_text = tarot_soup.select(".js-today_interp_copy")

        # print the found Horoscopes
        print("Astrology.com: \n",
              astrology_text[0].getText(), "\n")

        print("Horoscope.com: \n",
              horoscope_text[0].getText(), "\n")

        print("Tarot.com: \n",
              tarot_text[0].getText(), "\n")


def main():
    x = HoroscopeComparison()
    x.user_input()
    x.get_content()

if __name__ == "__main__":
    main()
