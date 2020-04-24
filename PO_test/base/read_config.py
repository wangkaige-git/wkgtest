#coding=utf-8
import configparser
import os

class ReadConfig():

    def __init__(self,con_filename='LocalElement.ini'):
        """
        con_filename：配置文件的文件名
        """
        configdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.configpath = configdir+'\\data\\'+con_filename



    def get_config_value(self,section,params):
        config = configparser.ConfigParser()
        config.read(self.configpath)
        return config.get(section,params)


    def get_section_key(self,section,params):
        config = configparser.ConfigParser()
        config.read(self.configpath)
        config_value = config.get(section,params)
        return config_value.split('>')[0]

    def get_section_value(self,section,params):
        config = configparser.ConfigParser()
        config.read(self.configpath)
        config_value = config.get(section,params)
        return config_value.split('>')[1]



if __name__ == "__main__":
    print (ReadConfig().configpath)


