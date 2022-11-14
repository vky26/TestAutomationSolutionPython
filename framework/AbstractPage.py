from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class AbstractPage:

    def webClickElement(self,context,locator):
        try:
            element = WebDriverWait(context.browser, 30).until(
                EC.visibility_of_element_located(locator)
            ).click();
        except Exception:
            raise Exception('Error on clicking Element')


    def webSendKeys(self,context,locator,value):
        try:
            element = WebDriverWait(context.browser, 30).until(
                EC.visibility_of_element_located(locator)
            ).send_keys(value);
        except Exception:
            raise Exception('Error on sendkeys to the Element')


    def switchToIFrame(self,context, frameName):
        context.browser.switch_to.frame(frameName);

    def scrollDownPage(self,context):
        context.browser.execute_script("window.scrollBy(0,1400)");

    def jsClick(self,context,locator):
        context.browser.execute_script("arguments[0].click();", locator)

    def webClearFields(self,context,locator):
        try:
            element = WebDriverWait(context.browser, 30).until(
                EC.visibility_of_element_located(locator)
            ).clear();
        except Exception:
            raise Exception('Error on clearing text from the Element')


    def webIsElementDisplayed(self,context, locator):
        try:
            element = WebDriverWait(context.browser, 30).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception:
            return False;
        return True;

    def selectDropDownByName(self,context,locator,dropDownValue):
        try:
            element = WebDriverWait(context.browser, 30).until(
                EC.visibility_of_element_located(locator)
            )
            select = Select(element)
            # select by select_by_visible_text() method
            select.select_by_visible_text(dropDownValue)
        except Exception:
            raise Exception('Not able to locate drop down element')

    def capture_screenshot(context, title='captured_screenshot'):
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f'{title}', attachment_type=allure.attachment_type.PNG
        )