from selenium import webdriver  #(import webdriver)
from selenium.webdriver.chrome.service import Service  #:1(import chrome webdriver)

Service = Service(
    "C:\\Users\\nisha\\Desktop\\chromedriver\\chromedriver.exe")  #:2(import the path of chormedriver where we have store it)


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars") #(this code will add an arguments to disable the infobars from the website)
    options.add_argument("satart-maximized") #(this argument will maximized the browser when it is launched)
    options.add_argument("disable-dev-shm-usage")  # (disable the dev/shm which helps to reduce memory consumption)
    options.add_argument("--no-sandbox")  #(this argument wii disable the sandbox mode of chrome)
    options.add_experimental_option("excludeSwitches", ["enable-automaton"]) #(it is used to by pass detection mechanism
                                                                         # that website used to identify automated browse session
    options.add_argument(
        "disable_blink_Features=AutomationControlled")  # (this disable blink features controlled by automation)
    driver = webdriver.Chrome(options=options)  #(this line of code is creating
                                                # a Selenium WebDriver object for interacting with
                                                # the Chrome web browser, using custom options provided in the options variable.)
    driver.get("https://automated.pythonanywhere.com/")  #(Link of the website from where we want to scrabe the data)
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())
