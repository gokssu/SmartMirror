
from __future__ import print_function
import time
import feedparser

try:
    from Tkinter import *
    import Tkinter as tk
except ImportError:
    from tkinter import *
    import tkinter as tk
import requests
import pprint

from PIL import Image, ImageTk

time_format = 24  # 12 or 24
date_format = "%b %d, %Y"
news_country_code = 'TR:tr'
weather_api_token = 'APIKEY'
weather_city_id = '826716'
weather_unit = 'metric'

xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18
xsmall_text_size = 14
text_font = "Calibri"
text_color = "white"
background_color = 'black'
icon_lookup = {
    '01d': "assets/01d.png",
    '01n': "assets/01n.png",
    '02d': "assets/02d.png",
    '02n': "assets/02n.png",
    '03d': "assets/03d.png",
    '03n': "assets/03n.png",
    '04d': "assets/04d.png",
    '04n': "assets/04n.png",
    '09d': "assets/09d.png",
    '09n': "assets/09n.png",
    '10d': "assets/10d.png",
    '10n': "assets/10n.png",
    '11d': "assets/11d.png",
    '11n': "assets/11n.png",
    '13d': "assets/13d.png",
    '13n': "assets/13n.png",
    '50d': "assets/50d.png",
    '50n': "assets/50n.png",
}


class Start(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg=background_color)
        self.starttitle = 'Hi,Have a Nice Day !'
        self.startLbl = Label(self, text=self.starttitle, font=(text_font, medium_text_size), fg=text_color,
                              bg=background_color)
        self.startLbl.pack(side=TOP, anchor=NW)
        self.startLbl = Frame(self, bg=background_color)


class Clock(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg=background_color)
        self.time1 = ''
        self.timeLbl = Label(self, font=(text_font, xlarge_text_size), fg=text_color, bg=background_color)
        self.timeLbl.pack(side=TOP, anchor=W)
        self.day_of_week1 = ''
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=(text_font, medium_text_size), fg=text_color,
                              bg=background_color)
        self.dayOWLbl.pack(side=TOP, anchor=W)
        self.date1 = ''
        self.dateLbl = Label(self, text=self.date1, font=(text_font, medium_text_size), fg=text_color,
                             bg=background_color)
        self.dateLbl.pack(side=TOP, anchor=W)
        self.tick()

    def tick(self):
        if time_format == 12:
            time2 = time.strftime('%I:%M %p')  # hour in 12h format
        else:
            time2 = time.strftime('%H:%M')  # hour in 24h format

        day_of_week2 = time.strftime('%A')
        date2 = time.strftime(date_format)

        if time2 != self.time1:
            self.time1 = time2
            self.timeLbl.config(text=time2)
        if day_of_week2 != self.day_of_week1:
            self.day_of_week1 = day_of_week2
            self.dayOWLbl.config(text=day_of_week2)
        if date2 != self.date1:
            self.date1 = date2
            self.dateLbl.config(text=date2)
        self.timeLbl.after(200, self.tick)


class News(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg=background_color)
        self.title = ' ▤ News in Turkey ▤ '
        self.newsLbl = Label(self, text=self.title, font=(text_font, medium_text_size), fg=text_color,
                             bg=background_color)
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg=background_color)
        self.headlinesContainer.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        try:
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            if news_country_code is None:
                headlines_url = "https://news.google.com/rss?hl=tr&gl=TR&ceid=TR:tr"
            else:
                headlines_url = "https://news.google.com/rss?hl=tr&gl=TR&ceid=TR:tr" + news_country_code

            feed = feedparser.parse(headlines_url)

            for post in feed.entries[0:7]:
                headline = NewsHeadline(self.headlinesContainer, post.title)
                headline.pack(side=TOP, anchor=W)
        except:
            print("Error: Cannot get news.")

        self.after(600000, self.get_headlines)


class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg=background_color)
        image = Image.open("assets/Newspaper.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg=background_color, image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)

        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=(text_font, small_text_size), fg=text_color,
                                  bg=background_color)
        self.eventNameLbl.pack(side=LEFT, anchor=N)


class FullscreenWindow:

    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background=background_color)
        self.topFrame = Frame(self.tk, background=background_color)
        self.bottomFrame = Frame(self.tk, background=background_color)
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = True
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.config(cursor='none')
        # clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=LEFT, anchor=N, padx=0, pady=0)
        # weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=RIGHT, anchor=N, padx=0, pady=0)
        # news
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=0, pady=0)
        # start
        self.start = Start(self.topFrame)
        self.start.pack(side=RIGHT, anchor=CENTER, padx=70, pady=200)


    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"


class Weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg=background_color)
        self.temperature = ''
        self.currently = ''
        self.icon = ''
        self.name = ''
        self.degreeFrm = Frame(self, bg=background_color)
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.temperatureLbl = Label(self.degreeFrm, font=(text_font, large_text_size), fg=text_color,
                                    bg=background_color)
        self.temperatureLbl.pack(side=LEFT, anchor=E)
        self.iconLbl = Label(self, bg=background_color)
        self.iconLbl.pack(side=RIGHT, anchor=E, padx=20)
        self.currentlyLbl = Label(self, font=(text_font, medium_text_size), fg=text_color, bg=background_color)
        self.currentlyLbl.pack(side=RIGHT, anchor=E)
        self.get_weather()

    def get_weather(self):
        try:
            resp = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?q=Eskişehir,turkey' + weather_city_id
                + '&units='
                + weather_unit
                + '&appid='
                + weather_api_token)

            temp = resp.json()
            pprint.PrettyPrinter(indent=4).pprint(temp)
            self.degree_sign = u"\N{DEGREE SIGN}" + 'C-' + temp['name']
            temperature = temp['main']['temp_min'], self.degree_sign
            current = temp['weather'][0]['description']
            icon = temp['weather'][0]['icon']

            icon2 = icon_lookup[icon]
            print(icon2)
            image = Image.open(icon2)
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.iconLbl.config(image=photo)
            self.iconLbl.image = photo
            self.temperatureLbl.config(text=temperature)
            self.currentlyLbl.config(text=current)

        except:
            print("No internet, cannot get weather.")

        self.after(600000, self.get_weather)


if __name__ == '__main__':
    mirror = FullscreenWindow()
    mirror.tk.title("SmartMirror")
    mirror.tk.attributes("-fullscreen", True)

    mirror.tk.mainloop()
