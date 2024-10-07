from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


credentials = 'udes-1097495880'


def login(credentials):
    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # Navigate to the Cambridge login page
    browser.get('https://www.cambridgeone.org/login?rurl=/dashboard/learner/dashboard')

    # Wait for the username input field to be visible
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'gigya-loginID-56269462240752180'))
    )

    # Enter username
    username_field = browser.find_element(By.ID, 'gigya-loginID-56269462240752180')
    username_field.clear()
    username_field.send_keys(credentials)

    # Enter password
    password_field = browser.find_element(By.ID, 'gigya-password-56383998600152700')
    password_field.clear()
    password_field.send_keys(credentials)

    # Find the button using XPath
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Log in']"))
    )

    # Use JavaScript to click the button
    browser.execute_script("arguments[0].click();", button)

    return browser


def check_assignments(browser):

    span_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '(')]"))
        )
    # Get the text of the span element
    span_text = span_element.text.strip()
    # Extract the number from the text
    number = int(span_text.replace('(', '').replace(')', '').strip())
    # Check if the number is equal to 2
    if number > 0:
        print("The number is 2, performing the action...")
        # Place your action here, e.g., clicking a button or logging in
    else:
        print(f"The number is {number}, no action performed.")
    # Keep the browser open for debugging or testing
    input("Press Enter to close the browser...")


if __name__ == '__main__':
    
    browser = login(credentials)
    check_assignments(browser)
