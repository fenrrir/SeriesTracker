#!/usr/bin/env python


import sys
from urllib import urlopen


BASE_URL = 'http://www.tvrage.com'
BASE_SEARCH_URL = 'http://www.tvrage.com/search.php?search='
EPISODES_URL = '/episode_list/all'


try:
    from lxml.html import parse
    USING_LXML = True
except ImportError:
    from bs4 import BeautifulSoup
    USING_LXML = False


class HTMLParser(object):


    def parse_series(self, series_div):
        '''
        Parse a bs tag containing a div to get series' title, last episode name and
        air date, episode list url, genre and status.

        Example div
        <div class=" clearfix" id="show_search">
            <dl>
                <dt>
                    <h2>
                    <a href="/Smash">Smash</a> #first a is title
                    <img src="http://images.tvrage.com/flags/us.gif"/>
                    </h2>
                </dt>
                <dd class="img">
                    <a href="/Smash">
                        <img src="http://images.tvrage.com/shows/29/thumb125-28337.jpg" width="75"/>
                    </a>
                </dd>
                <dd> #second dd is last episode air date
                    <strong>Latest Episode:</strong>
                    May/14/2012 
                    <a href="/Smash/episodes/1065174545">Bombshell</a> #third a is name
                </dd>
                <dd> #third dd is genre and status
                    <strong>Genre:</strong>
                    Music |
                    <strong>Status:</strong>
                    Returning Series 
                </dd>
           </dl>
        </div>
        '''
        raise TypeError()

    def get_synopsis(self, episode_url):
        raise TypeError()

    def parse_episode(self, episode_tr):
        '''
        Parse a bs tag containing a tr to get an episode's title, air date, season,
        episode number, and synopsis.

        Example tr
        <tr bgcolor="#FFFFFF" id="brow">
            <td align="center" width="45">
                1
            </td>
            <td align="center" width="40">
                <a href="/Supernatural/episodes/166205" title="Supernatural season 1 episode 1">
                    1x01
                </a>
            </td>
            <td align="center" width="80">
                13/Sep/2005
            </td>
            <td style="padding-left: 6px;">
                <a href="/Supernatural/episodes/166205/?trailer=1#trailer">
                    <img border="0" height="13" src="/_layout_v3/misc/film.gif" title="View Trailer"/>
                </a>
                <a href="/Supernatural/episodes/166205">
                    Pilot
                </a>
            </td>
            <td align="center">
                <a href="/Supernatural/episodes/166205/gallery">
                    0
                </a>
            </td>
            <td align="center">
                9.5
            </td>
        </tr>
        '''
        raise TypeError()

    def search_series(self, url):
        raise TypeError()


    def get_episodes(series_tuple):
        raise TypeError()


class LxmlHTMLParser(HTMLParser):

    def parse_series(self, series_div):
        anchors = series_div.cssselect('a')
        dd = series_div.cssselect('dd')
        title = anchors[0].text_content()
        episodes_url = BASE_URL + anchors[0].get('href') + EPISODES_URL
        if len(anchors) == 3:
            last_air_date = dd[1].text_content().split(' ')[2]
            last_episode = anchors[2].text_content()
            return title, episodes_url, last_air_date, last_episode
        else:
            return title, episodes_url

    def get_synopsis(self, episode_url):
        doc = parse(urlopen(episode_url)).getroot()
        synopsis = doc.cssselect('div .show_synopsis')[0].text_content()
        synopsis = synopsis.split('\n')[1]
        return synopsis

    def parse_episode(self, episode_tr):
        anchors = episode_tr.cssselect('a')
        number = anchors[0].text_content()
        name = episode_tr.cssselect('td a')[-1].text_content()
        season = number.split('x')[0]
        air_date = episode_tr.cssselect('td')[2].text_content()
        episode_url = BASE_URL + anchors[-1].get('href')
        synopsis = episode_url
        return number, name, season, air_date, synopsis

    def search_series(self, url):
        doc = parse(urlopen(url)).getroot()
        series_list = doc.cssselect('div #show_search')
        return series_list


    def get_episodes(self, url):
        doc = parse(urlopen(url)).getroot()
        episodes_table = doc.cssselect('div #brow')
        return episodes_table


class BeautifulSoupHTMLParser(object):

    def parse_series(self, series_div):
        title = series_div.find_all('a')[0].string
        episodes_url = BASE_URL + series_div.find_all('a')[0]['href'] + EPISODES_URL
        if len(series_div.find_all('a')) == 3:
            last_air_date = series_div.find_all('dd')[1].contents[2]
            last_episode = series_div.find_all('a')[2].string
            return title, episodes_url, last_air_date, last_episode
        else:
            return title, episodes_url


    def get_synopsis(self, episode_url):
        html = urlopen(episode_url).read()
        soup = BeautifulSoup(html)
        synopsis = soup.find_all('div', 'show_synopsis')[0].contents[0]
        return synopsis


    def parse_episode(self, episode_tr):
        anchors = episode_tr.find_all('a')
        td = episode_tr.find_all('td')
        number = anchors[0].string
        name = td[3].find_all('a')[-1].string
        season = number.split('x')[0]
        air_date = td[2].string
        episode_url = BASE_URL + anchors[-1]['href']
        synopsis = episode_url
        return number, name, season, air_date, synopsis


    def search_series(self, url):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        series_list = soup.find_all(id='show_search')
        return series_list


    def get_episodes(self, url):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        episodes_table = soup.find_all(id='brow')
        return episodes_table



if USING_LXML:
    DefaultParser = LxmlHTMLParser
else:
    DefaultParser = BeautifulSoupHTMLParser


class SeriesManager(object):

    def __init__(self, html_parser):
        self.html_parser = html_parser

    def get_synopsis(self, episode_url):
        return self.html_parser.get_synopsis(episode_url).lstrip()

    def parse_episode(self, episode_tr):
        number, name, season, air_date, synopsis =\
                self.html_parser.parse_episode(episode_tr)
        if len(season) != 1:
            return None
        else:
            return number, name, season, air_date, synopsis

    def search_series(self, series_name):
        series_name = series_name.replace(' ','+')
        url = BASE_SEARCH_URL + series_name

        series_list = self.html_parser.search_series(url)

        results = []
        for item in series_list:
            results.append(self.html_parser.parse_series(item))
        return results


    def get_episodes(self, series_tuple):
        url = series_tuple[1]

        episodes_table = self.html_parser.get_episodes(url)

        episode_list = []
        for item in episodes_table:
            episode = self.parse_episode(item)
            if episode != None:
                yield episode



class SerieNotFound(Exception):
    pass


class Serie(object):


    def __init__(self, name, manager=None, data=None):
        self.name = name

        if not manager:
            manager = SeriesManager( DefaultParser() )

        self.manager = manager

        if not data:
            try:
                self.data = self.manager.search_series(self.name)[0]
                self.name = self.data[0]
            except IndexError:
                raise SerieNotFound()
        else:
            self.data = data

    
    @property
    def episodes(self):
        def iterator():
            episodes = self.manager.get_episodes(self.data)
            for episode_data in episodes:
                yield Episode(episode_data, self.manager)

        return iterator()


    @property
    def episodes_as_list(self):
        return list(self.episodes)


    def __str__(self):
        return "<Serie {}>".format(self.name)

    __repr__ = __str__


class Episode(object):

    def __init__(self, episode_data, manager):
        self.episode_data = episode_data
        self.manager = manager
        self._synopsis_unread = False
        self.number, self.name, self.season, \
            self.air_date, self._synopsis_url = episode_data
        self.season = int(self.season)

    @property
    def synopsis(self):
        if not self._synopsis_unread:
            self._synopsis = self.manager.get_synopsis( self._synopsis_url )
            self._synopsis_unread = True
        return self._synopsis

    def __str__(self):
        return "<Episode {} - {}>".format(self.number, self.name)

    __repr__ = __str__




def get_serie(name):
    manager = SeriesManager( DefaultParser() )
    data = manager.search_series(name)[0]
    s_name = data[0]
    if s_name != name:
        raise SerieNotFound()
    else:
        return Serie(s_name, manager)


def search_serie(name):
    manager = SeriesManager( DefaultParser() )
    data = manager.search_series(name)
    return [ Serie(d[0], manager, d) for  d in data ]



def main():
    for episode in search_serie(sys.argv[1])[0].episodes:
        print episode

if __name__ == '__main__':
    main()
