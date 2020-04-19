#coding=utf-8
import configparser

class ReadConfig():

    def __init__(self,con_filename):
        """
        con_filename：配置文件的文件名
        """
        configdir = 'E:\\auto_test\\PO_test\\data'
        self.configpath = configdir+'\\'+con_filename



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



configfile = ReadConfig('LocalElement.ini')
