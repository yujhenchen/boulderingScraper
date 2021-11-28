from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Athlete:
	def __init__(self, name, pic, country):
		self.name = name.strip() 
		self.pic = pic
		self.country = country.strip()

	def __str__(self):
		return self.name

class Athletes:
	def __init__(self):
		self.url = 'https://www.ifsc-climbing.org/index.php/athletes'

	def fetchAthletes(self):
		driver = webdriver.Chrome()

		driver.get(self.url)
		wait = WebDriverWait(driver, 5)

		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.category')))

		categories = driver.find_elements(By.CSS_SELECTOR, '.category')

		
		athleteDict = {}
		for category in categories:
			catName = category.find_element(By.CSS_SELECTOR, '.category-name').get_attribute('innerHTML')
			athleteDict[catName] = []
			athletes = category.find_elements(By.CSS_SELECTOR, '.athlete')
			for athlete in athletes:
				athleteName = athlete.find_element(By.CSS_SELECTOR, '.name').get_attribute('innerHTML')
				athletePic = athlete.find_element(By.CSS_SELECTOR, '.athlete-img').get_attribute('src')
				athleteIso = athlete.find_element(By.CSS_SELECTOR, '.iso').get_attribute('innerHTML')
				athObj = Athlete(athleteName, athletePic, athleteIso)
				athleteDict[catName].append(athObj)
		
		return athleteDict
		