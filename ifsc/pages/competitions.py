from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Competitions:
	def __init__(self):
		self.url = 'https://www.ifsc-climbing.org/index.php/world-competition'

	def fetchCompetitions(self):
		driver = webdriver.Chrome()

		driver.get(self.url)
		wait = WebDriverWait(driver, 5)
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#calendar')))
		driver.switch_to.frame('calendar')
		
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.competition')))
		events = driver.find_elements(By.CSS_SELECTOR, '.competition .title a')
		eventTitles = []
		for event in events:
			eventTitles.append(event.get_attribute('innerHTML'))
		
		yearSelect = driver.find_element(By.ID, 'yearSelect')
		yearSelect.click()
		
		wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='yearSelect']/option[@value='0']")))

		newestYear = driver.find_element(By.XPATH, "//select[@id='yearSelect']/option[@value='0']")
		newestYear.click()

		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.competition .title a'), '2022'))
		events = driver.find_elements(By.CSS_SELECTOR, '.competition .title a')
		for event in events:
			eventTitles.append(event.get_attribute('innerHTML'))

		
		return eventTitles
