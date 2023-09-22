from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#ваши емаил и пароль от спотифай
email = 'YourEmail'
password = 'YourPassword'


#прокси индия любой
proxy_ip_port = 'YourIp:YourPort'
proxy_login = 'YourProxyLogin'
proxy_password = 'YourProxyPassword'

def change_region(spotify_login, spotify_password, proxy_ip_port, proxy_login, proxy_password):

	proxy_options = {
	    "proxy": {
	        "https": f"http://{proxy_login}:{proxy_password}@{proxy_ip_port}"
	    }
	}
	options = webdriver.ChromeOptions()
	#options.add_argument('headless')

	driver = webdriver.Chrome( seleniumwire_options=proxy_options)

	driver.get("https://www.spotify.com/md-ru/account/")

	time.sleep(3)


	input_login = driver.find_element(By.XPATH ,'//input[@id="login-username"]')
	input_password = driver.find_element(By.XPATH ,'//input[@id="login-password"]')
	login_button = driver.find_element(By.ID, "login-button")

	input_login.send_keys(spotify_login)
	time.sleep(1)
	input_password.send_keys(spotify_password)
	time.sleep(2)
	login_button.click()
	time.sleep(5)

	change_profile = driver.find_element(By.XPATH, "(//DIV[@role='button'])[2]")
	change_profile.click()
	time.sleep(5)

	choose_country = driver.find_element(By.XPATH, "//SELECT[@id='country']")
	select = Select(choose_country)
	choose_country.click()
	time.sleep(5)
	try:
		select.select_by_visible_text('Индия')
	except:
		try:
			select.select_by_visible_text('India')
		except:
			try:
				select.select_by_value('In')
			except:
				select.select_by_value('Ин')

	time.sleep(7)
	final_button = driver.find_element(By.XPATH, "//form/div/button/span")

	final_button.click()

	time.sleep(10)
	driver.quit()





change_region(email, password, proxy_ip_port, proxy_login, proxy_password)
