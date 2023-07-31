
import string
import scrapy
from current_nba_players.PerGameSeason import PerGameSeason


class CurrentNBAPlayerSpider(scrapy.Spider):
    name = "current_nba_players"
    allowed_domains = ["www.basketball-reference.com"]
    start_urls = ["https://www.basketball-reference.com/players/"]

    def start_requests(self):
        last_name_initials = list(string.ascii_lowercase)
        base_player_url = "https://www.basketball-reference.com/players/"
        urls = [base_player_url + x + '/' for x in last_name_initials]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        base_url = 'https://www.basketball-reference.com'

        for active_player in response.xpath('//div[@id="div_players"]//th[@data-stat="player"]/strong'):
            url = base_url + active_player.xpath('a/@href').get()
            yield scrapy.Request(url=url, callback=self.parse_player_page)
        


    def parse_player_page(self, response):
        """
            This method parses each of the individual player's page
            i.e. https://www.basketball-reference.com/players/f/foxde01.html
        """

        name = response.xpath('//div[@id="info" and @class="players"]//div/h1/span/text()').get()

        for season in response.xpath('//div[@id="div_per_game"]/table[@id="per_game"]/tbody/tr[@class="full_table"]'):
            player = PerGameSeason()

            player["name"] = name

            # Need to loop through each season (each season is organized as a row)
            # foreach season in seasons ('//tbody/tr[@class="full_table"]')
            player["season"] = season.xpath('th[@data-stat="season"]/a/text()').get()
            player["age"] = season.xpath('td[@data-stat="age"]/text()').get()
            player["team"] = season.xpath('td[@data-stat="team_id"]/a/text()').get()
            player["league"] = season.xpath('td[@data-stat="lg_id"]/a/text()').get()
            player["position"] = season.xpath('td[@data-stat="pos"]/text()').get()
            player["games_played"] = season.xpath('td[@data-stat="g"]/text()').get()
            player["games_started"] = season.xpath('td[@data-stat="gs"]/text()').get()
            player["minutes_played_per_game"] = season.xpath('td[@data-stat="mp_per_g"]/text()').get()
            player["field_goals_per_game"] = season.xpath('td[@data-stat="fg_per_g"]/text()').get()
            player["field_goals_attempted_per_game"] = season.xpath('td[@data-stat="fga_per_g"]/text()').get()
            player["field_goal_percentage"] = season.xpath('td[@data-stat="fg_pct"]/text()').get()
            player["three_point_field_goals_per_game"] = season.xpath('td[@data-stat="fg3_per_g"]/text()').get()
            player["three_point_field_goals_attempts_per_game"] = season.xpath('td[@data-stat="fg3a_per_g"]/text()').get()
            player["three_point_field_goal_percentage"] = season.xpath('td[@data-stat="fg3_pct"]/text()').get()
            player["two_point_field_goals_per_game"] = season.xpath('td[@data-stat="fg2_per_g"]/text()').get()
            player["two_point_field_goal_attempts_per_game"] = season.xpath('td[@data-stat="fg2a_per_g"]/text()').get()
            player["two_point_field_goal_percentage"] = season.xpath('td[@data-stat="fg2_pct"]/text()').get()
            player["effective_field_goal_percentage"] = season.xpath('td[@data-stat="efg_pct"]/text()').get()
            player["free_throws_per_game"] = season.xpath('td[@data-stat="ft_per_g"]/text()').get()
            player["free_throw_attempts_per_game"] = season.xpath('td[@data-stat="fta_per_g"]/text()').get()
            player["free_throw_percentage"] = season.xpath('td[@data-stat="ft_pct"]/text()').get()
            player["offensive_rebounds_per_game"] = season.xpath('td[@data-stat="orb_per_g"]/text()').get()
            player["defensive_rebounds_per_game"] = season.xpath('td[@data-stat="drb_per_g"]/text()').get()
            player["total_rebounds_per_game"] = season.xpath('td[@data-stat="trb_per_g"]/text()').get()
            player["assists_per_game"] = season.xpath('td[@data-stat="ast_per_g"]/text()').get()
            player["steals_per_game"] = season.xpath('td[@data-stat="stl_per_g"]/text()').get()
            player["blocks_per_game"] = season.xpath('td[@data-stat="blk_per_g"]/text()').get()
            player["turnovers_per_game"] = season.xpath('td[@data-stat="tov_per_g"]/text()').get()
            player["personal_fouls_per_game"] = season.xpath('td[@data-stat="pf_per_g"]/text()').get()
            player["points_per_game"] = season.xpath('td[@data-stat="pts_per_g"]/text()').get()

            yield player

