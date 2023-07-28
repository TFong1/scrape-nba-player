# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PerGameSeason(scrapy.Item):
    name: str = scrapy.Field()
    season: str = scrapy.Field()
    age: str = scrapy.Field()
    team: str = scrapy.Field()
    league: str = scrapy.Field()
    position: str = scrapy.Field()
    games_played: str = scrapy.Field()
    games_started: str = scrapy.Field()
    minutes_played_per_game: str = scrapy.Field()
    field_goals_per_game: str = scrapy.Field()
    field_goals_attempted_per_game: str = scrapy.Field()
    field_goal_percentage: str = scrapy.Field()
    three_point_field_goals_per_game: str = scrapy.Field()
    three_point_field_goals_attempts_per_game: str = scrapy.Field()
    three_point_field_goal_percentage: str = scrapy.Field()
    two_point_field_goals_per_game: str = scrapy.Field()
    two_point_field_goal_attempts_per_game: str = scrapy.Field()
    two_point_field_goal_percentage: str = scrapy.Field()
    effective_field_goal_percentage: str = scrapy.Field()
    free_throws_per_game: str = scrapy.Field()
    free_throw_attempts_per_game: str = scrapy.Field()
    free_throw_percentage: str = scrapy.Field()
    offensive_rebounds_per_game: str = scrapy.Field()
    defensive_rebounds_per_game: str = scrapy.Field()
    total_rebounds_per_game: str = scrapy.Field()
    assists_per_game: str = scrapy.Field()
    steals_per_game: str = scrapy.Field()
    blocks_per_game: str = scrapy.Field()
    turnovers_per_game: str = scrapy.Field()
    personal_fouls_per_game: str = scrapy.Field()
    points_per_game: str = scrapy.Field()
