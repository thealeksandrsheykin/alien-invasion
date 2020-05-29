#-*-coding: utf-8-*-
#!/usr/bin/env python3

class Settings():
    '''
    A class to store all settings for Alien Invasion.
    '''
    def __init__(self):
        '''Initialize the game's settings.'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230,230,230)

        #Ship settings
        self.ship_speed_factor = 1.5
