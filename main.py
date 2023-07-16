from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import string
import threading

def create_account(email, password):
    driver = webdriver.Firefox()
    driver.get("https://www.spotify.com/in-en/signup")
    random_length = random.randint(7, 8)
    emailletter = ''.join(random.choices(string.ascii_letters, k=random_length))
    email_input = driver.find_element(By.CSS_SELECTOR, "#email")
    email_input.send_keys(emailletter + "@me.tv")

    rand_len = random.randint(6, 7)
    passa = ''.join(random.choices(string.ascii_letters, k=rand_len))
    password_input = driver.find_element(By.CSS_SELECTOR, "#password")
    password_input.send_keys(passa + "200$")

    random_length = random.randint(6, 8)
    random_username = ''.join(random.choices(string.ascii_letters, k=random_length))
    username_input = driver.find_element(By.CSS_SELECTOR, "#displayname")
    username_input.send_keys(random_username)

    month_select = Select(driver.find_element(By.NAME, 'month'))
    month_select.select_by_index(5)

    day_input = driver.find_element(By.CSS_SELECTOR, "#day")
    day_input.send_keys(23)

    gender_label = driver.find_element(By.CSS_SELECTOR, "div.Radio-sc-tr5kfi-0:nth-child(1) > label:nth-child(2) > span:nth-child(2)")
    gender_label.click()

    year_input = driver.find_element(By.CSS_SELECTOR, "#year")
    year_input.send_keys("2000")

    finish_button = driver.find_element(By.CSS_SELECTOR, ".dqLIWu")
    finish_button.click()

    driver.quit()


threads = []
num_threads = int(input("Enter the number of threads to use: "))

while True:
    email_length = random.randint(5, 10)
    password_length = random.randint(8, 12)

    email = ''.join(random.choices(string.ascii_lowercase, k=email_length))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

    thread = threading.Thread(target=create_account, args=(email, password))
    threads.append(thread)
    thread.start()

    if input("Press 'q' to quit, or any other key to continue: ") == "q":
        break

for thread in threads:
    thread.join()


with open("acc.txt", "w") as file:
    for thread in threads:
        thread.join()
        email, password = thread._args
        file.write(f"{email}:{password}\n")
