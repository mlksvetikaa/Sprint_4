from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_TEXT = [By.XPATH, "//*[contains(@class, 'Home_Header')]"]  # Заголовок на главной странице
    HEADER_ORDER_BUTTON = [By.XPATH, ".//*[@class='Button_Button__ra12g']"] # Кнопка "Заказать" в шапке
    LOCATOR_FAQ = [By.XPATH, ".//div[text()='Вопросы о важном']"]  # Раздел "Вопросы о важном"
    LOCATOR_QUESTIONS = [By.XPATH, "//*[contains(@class, 'accordion__item')]"]  # Вопросы
    LOCATOR_ANSWER = (By.XPATH, "//*[contains(@class, 'accordion__panel') and not(@hidden)]")  # Отображаемый ответ
    COOKIES_BUTTON = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF' and text()='да все привыкли']"]  # Кнопка "Да все привыкли"
    ORDER_BUTTON_MAIN_PAGE = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"]  # Кнопка "Заказать" на странице
    YANDEX_LOGO = [By.XPATH, "//*[@alt='Yandex']"]  # Лого "Яндекс"
    SCOOTER_LOGO = [By.XPATH, "//*[@alt='Scooter']"]  # Лого "Самокат"