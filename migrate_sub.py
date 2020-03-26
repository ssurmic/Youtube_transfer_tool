'''

transfering tool for the subscriptions between yotube accounts

reqiurements:

module:

standard library: re, xml.dom, time, collection
extras: selenium


'''



from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xml.dom import minidom
import time
import re
def main():
    #create the instance of the driver
    driver = webdriver.chrome()
    sign_in_helper(driver)

def sign_in_helper(driver):
    pass