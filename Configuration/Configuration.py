import os,  stat
import shlex, subprocess
import sys, getopt
import logging
import glob
from os.path import basename , dirname
#import CppHeaderParser
import shutil
import datetime
import configparser
import xml.etree.ElementTree as ET



def ReadIni(IniFileName):
	returnValue = {}
	config = configparser.ConfigParser()
	config.read(IniFileName)
	SectionList = config.sections()	
	for section in SectionList:
		for x in config[section]:
			returnValue[x] = config[section][x]
	return (returnValue)
	
def ReadXml(XmlFileName, tag):
	returnValue = {}
	tree = ET.parse(XmlFileName)
	root = tree.getroot()
	for Cfg in root.findall(tag):
		#print(Cfg.get('name'))
		returnValue[Cfg.get('name')] = Cfg.find('value').text
		#returnValue[Cfg.get('name')] = Cfg.text
		
	return returnValue

		
def main():
	ret = ReadXml("Conf.xml", "Configuration")
	print(ret)
	ret = ReadIni("Conf.ini")
	print(ret)
	
main()