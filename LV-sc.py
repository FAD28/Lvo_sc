from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Lovoo User Scraping #https://de.lovoo.com/
# 1- Loginbutton.click()
# 2- send keys: Email-Adresse
# 3- send keys: PW
# 4- Loginbutton.click()
# 5- Matchbutton.click()   # Ab hier kommt ein loop
# 6- Profil.click()
# 7- Steckbrief.click() 
# 8- df.to_excel Data
# 9- driver.back
# 10- Match.button.click()
# 6- Profil.click()
# 7- Steckbrief.click()
# 8- df.to_excel Data
# 9- driver.back

class LovooScraping():

    def __init__(self):
        self.driver= webdriver.Chrome(executable_path='/User/Driver/chromedriver')
        self.df = pd.DataFrame()
        self.name_list = []
        self.wohnort_list = []
        self.interessiert_list = []
        self.aussehen_list = []
        self.raucher_list = []
        self.wohnsituation_list = []


    def compile_data(self):

        # Name
        name = self.driver.find_elements_by_css_selector('#profile-details > div > div.h5.relative.bg-gender.text-white.padding-lg.text-bold.no-space-after.no-space-before > span')
        self.name_list = [value.text for value in name]
        print(self.name_list)

        # Wohnort
        wohnort = self.driver.find_elements_by_css_selector('#profile-details > div > div.space-before-sm > div > div.tab-pane.active > div > div:nth-child(1) > div > dl > dd')
        self.wohnort_list = [value.text for value in wohnort]

        # Interessiert an
        interessiert = self.driver.find_elements_by_css_selector('#profile-details > div > div.space-before-sm > div > div.tab-pane.active > div > div:nth-child(3) > div > dl > dd')
        self.interessiert_list = [value.text for value in interessiert]

        # Aussehen
        aussehen = self.driver.find_elements_by_css_selector('#profile-details > div > div.space-before-sm > div > div.tab-pane.active > div > div:nth-child(5) > div > dl > dd')
        self.aussehen_list = [value.text for value in aussehen]

        # Raucher
        raucher = self.driver.find_elements_by_css_selector('#profile-details > div > div.space-before-sm > div > div.tab-pane.active > div > div:nth-child(7) > div > dl > dd')
        self.raucher_list = [value.text for value in raucher]

        # Wohnsituation
        wohnsituation = self.driver.find_elements_by_css_selector('#profile-details > div > div.space-before-sm > div > div.tab-pane.active > div > div:nth-child(9) > div > dl > dd')
        self.wohnsituation_list = [value.text for value in wohnsituation]

        # self.df.loc["name"] = self.name_list
        #
        # self.df.loc["Wohnort"] = self.wohnort_list
        #
        # self.df.loc["Aussehen"] = self.aussehen_list
        #
        # self.df.loc["Raucher"] = self.raucher_list
        #
        # self.df.loc["Wohnsituation"] = self.wohnsituation_list
        #
        for i in range(len(self.name_list)):
            try:
                self.df.loc[i, "name"] = self.name_list[i]

            except Exception as e:

                print('Name konnte nicht gefunden werden ')

            try:
                self.df.loc[i, "Wohnort"] = self.wohnort_list[i]

            except Exception as e:

                print('Wohnort konnte nicht gefunden werden ')
            try:
                self.df.loc[i, "Aussehen"] = self.aussehen_list[i]

            except Exception as e:

                print('Aussehen konnte nicht gefunden werden ')

            try:
                self.df.loc[i, "Raucher"] = self.raucher_list[i]

            except Exception as e:

                print('Raucher konnte nicht gefunden werden ')

            try:
                self.df.loc[i, "Wohnsituation"] = self.wohnsituation_list[i]

            except Exception as e:

                print('Wohnsituation konnte nicht gefunden werden ')

        print("Excel sheet created!")

writer = pd.ExcelWriter("Lovoo.xlsx")

###################################################################

driver = LovooScraping()  # // steht jetzt im for-loop

link = 'https://de.lovoo.com/'

driver.driver.get(link)

einloggen_button = driver.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/button[2]")
einloggen_button.click()

username = driver.driver.find_element_by_xpath("//*[@id='form']/div[1]/input")
password = driver.driver.find_element_by_xpath("//*[@id='form']/div[2]/div[1]/input")

username.send_keys("*username*")
time.sleep(5)
password.send_keys("*password*")
time.sleep(5)
driver.driver.find_element_by_xpath("//*[@id='form']/div[2]/div[2]/button").click()
# if einloggen_button.click()
time.sleep(5)

for i in range(2):
    driver.driver.find_element_by_xpath("//*[@id='topmenu']/div/nav/div/div[2]/div/ul[1]/li[2]/a").click()
    time.sleep(5)
    driver.driver.find_element_by_xpath("//*[@id='page-content']/match/div/div/div[1]/a/div").click()
    time.sleep(5)
    driver.driver.find_element_by_css_selector('#profile-details > div > div.space-before-sm > ul > li:nth-child(2) > a').click()
    time.sleep(5)
    driver.compile_data()
    driver.df.to_excel(writer, sheet_name='Lovoo')
    driver.driver.back()
    time.sleep(5)

writer.save()

driver.driver.close()
