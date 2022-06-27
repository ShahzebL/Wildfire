import numpy as np
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url = "https://sedac.ciesin.columbia.edu/mapping/popest/pes-v3/"

driver = webdriver.Chrome()
driver.get(url)
button = driver.find_element_by_class_name('leaflet-control-command leaflet-control')
print(button.text)


driver.close()



#tap an element

