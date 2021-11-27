from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class Competitions:
	def __init__(self):
		self.url = 'https://www.ifsc-climbing.org/index.php/world-competition'

	def fetchCompetitions(self):
		driver = webdriver.Chrome()

		driver.get(self.url)
		wait = WebDriverWait(driver, 5)
		wait.until(presence_of_element_located((By.CSS_SELECTOR, '#calendar')))
		driver.switch_to.frame('calendar')
		
		wait.until(presence_of_element_located((By.CSS_SELECTOR, '.competition')))
		events = driver.find_elements(By.CSS_SELECTOR, '.competition .title a')

		eventTitles = []
		for event in events:
			eventTitles.append(event.get_attribute('innerHTML'))
		return eventTitles	
