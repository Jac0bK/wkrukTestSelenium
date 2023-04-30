import unittest

import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from time import sleep

#Dane testowe

fake = Faker(['pl_PL'])
firstname = fake.first_name()
lastname = fake.last_name()
phoneNo = fake.phone_number()
email = fake.email()
street = fake.street_name()
buildingNo = fake.building_number()
postcode = fake.postcode()
cityname = fake.city()
password = fake.password()
password_check = fake.password()

password_error_info = "Podane hasła nie są identyczne."

#//ul[@class="errors_for_field"]//li

class RegistrationTests(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne:
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait_10_seconds = WebDriverWait(self.driver, 10)
        self.driver.get("https://wkruk.pl/")
        cookies = self.driver.find_element(By.ID, "cookiescript_accept")
        cookies.click()
        # Kliknij "Zarejestruj"
        sleep(2)
        self.wait_10_seconds.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[2]/a[1]'))).click()
        register = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/form/p/a').click()
        sleep(5)

    def testWrongPassword(self):
        firstname_input = self.driver.find_element(By.ID, "customer_first_name")
        firstname_input.send_keys(firstname)
        lastname_input = self.driver.find_element(By.ID, "customer_last_name")
        lastname_input.send_keys(lastname)
        phone_number_input =self.driver.find_element(By.ID, "customer_telephone")
        phone_number_input.send_keys(phoneNo)
        street_name_input = self.driver.find_element(By.ID, "customer_delivery_street_name")
        street_name_input.send_keys(street)
        buildingNo_input = self.driver.find_element(By.ID, "customer_delivery_building_number")
        buildingNo_input.send_keys(buildingNo)
        postcode_input = self.driver.find_element(By.ID, "customer_delivery_postal_code")
        postcode_input.send_keys(postcode)
        city_input = self.driver.find_element(By.ID, "customer_delivery_city")
        city_input.send_keys(cityname)
        email_input = self.driver.find_element(By.ID, "customer_email")
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, "customer_password")
        password_input.send_keys(password)
        sleep(10)
        password_input = self.driver.find_element(By.ID, "customer_password_confirmation")
        password_input.send_keys(password_check)

        accept_policy = self.driver.find_element(By.XPATH, '//*[@for="customer_agreed"]').click()
        sleep(5)

        accept_RODO = self.driver.find_element(By.XPATH, '//*[@for="customer_agreed_long"]').click()
        sleep(5)

        register_btn = self.driver.find_element(By.XPATH, '//button[@class="btn"][@type="submit"]').click()

        sleep(10)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()