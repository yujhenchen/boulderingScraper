from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ifsc.pages.pagebase import PageBase

from ifsc.utils.waits import Waits

class Competitions(PageBase):

	def __init__(self):
		super().__init__()
		self.url = 'https://www.ifsc-climbing.org/index.php/world-competition'
		self.driver.get(self.url)
		self.wait = Waits(self.driver, 10)

	# external method
	def fetchCompetitions(self):
		
		self.switchToCalendarFrame()	

		eventTitles = self.getEventTitles()

		self.openYearSelectMenu()

		self.selectYear(option=0) # 0 is first option (newest year)
		
		eventTitles += self.getEventTitles()

		return eventTitles


	#internal methods
	def switchToCalendarFrame(self):
		self.wait.waitForElement((By.CSS_SELECTOR, '#calendar'))
		self.driver.switch_to.frame('calendar')

	def getEventTitles(self):
		self.wait.waitForElement((By.CSS_SELECTOR, '.competition'))
		events = self.driver.find_elements(By.CSS_SELECTOR, '.competition .title a')
		eventTitles = []
		for event in events:
			eventTitles.append(event.get_attribute('innerHTML'))
		return eventTitles
	
	def openYearSelectMenu(self):
		yearSelect = self.driver.find_element(By.ID, 'yearSelect')
		yearSelect.click()
	
	def selectYear(self, option):
		self.wait.waitForElement((By.XPATH, "//select[@id='yearSelect']/option[@value='" + str(option) + "']"))
		newestYear = self.driver.find_element(By.XPATH, "//select[@id='yearSelect']/option[@value='" + str(option) + "']")
		newestYear.click()



	