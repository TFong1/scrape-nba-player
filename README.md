# Scrape NBA Player

This project will scrape some data from [basketball-reference.com](https://www.basketball-reference.com).

Basketball Reference is a website that contains statistics from anything basketball related.  They have data on players, past and present, that play in the National Basketball Association (NBA), WNBA, NBA's G League, as well as International players, such as the EuroLeague, China's CBA, and Australia's NBL.

We are going to focus scraping data from NBA players who are currently active in the league. We'll grab the player's historical regular season data and save the data to a comma-separated values file (CSV).

## Application Programming Interfaces (API) Used in this Project

For this project, we are using [Scrapy](https://scrapy.org) with [Python](https://www.python.org). Please refer to these sites to receive guidance installing Scrapy and Python.

## Execute Scrapy Spider

To execute the Scrapy spider, change directory to the current_nba_players/current_nba_players/spiders and run the following command:

    scrapy runspider current-nba-players.py -O output.csv:csv

## Discussion

For a more detailed explanation of this code, head on over to my [Medium](https://medium.com/@tony.n.fong/scraping-nba-player-statistics-using-scrapy-ac01e91cfe43) page.
