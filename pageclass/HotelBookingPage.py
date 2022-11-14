import time
import json
from selenium.webdriver.common.by import By
from framework.AbstractPage import AbstractPage
from framework.Utils import Utils
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By



class HotelBookingPage():

    arrivalDate = (By.ID, 'date-start')
    numberOfNights =  (By.ID, 'to-place')
    numberOfAdults =  (By.NAME,'wbe_product[adult_count]')
    numberOfChildren =  (By.NAME,'wbe_product[children_count]')
    bookNowButton = (By.NAME, 'commit')
    deluxeApartmentCategory = (By.XPATH, '//h2[contains(text(),"Deluxe Appartment")]')
    deluxeApartmentRoom = (By.XPATH, '(//h2[contains(text(),"Deluxe Appartment")]/following::table//tr[last()])//td[last()]/span')
    addOn1 = (By.XPATH, '(//input[@type="number"])[1]')
    addOn2 = (By.XPATH, '(//input[@type="number"])[2]')
    addSelectedAddOns = (By.XPATH, '(//input[@type="submit"])[1]')
    emailId = (By.XPATH, '//input[@title="E-mail"]')
    lastName = (By.XPATH, '//input[@title="Last name"]')
    firstName = (By.XPATH, '//input[@title="First name"]')
    phoneNumber = (By.XPATH, '//input[@title="Phone"]')
    creditCardRadioButton = (By.XPATH, '//input[@title="Credit Card"]')
    agreePolicyRadioButton = (By.XPATH, '//input[@title="I agree with the hotel and guarantee policy"]')
    createBookingButton = (By.XPATH, '//input[@value="Create Booking"]')
    cardNumber = (By.ID, 'cardNumber')
    billingAddressLine = (By.ID, 'credit_card_collect_purchase_address')
    zip = (By.ID, 'credit_card_collect_purchase_zip')
    city = (By.ID, 'credit_card_collect_purchase_city')
    state = (By.ID, 'credit_card_collect_purchase_state')
    payButton = (By.XPATH, '//button[@type="submit"]')
    successMessage = (By.XPATH, '//h1[text()="Thank you for your booking!"]')
    dropDownBrand = (By.XPATH, '//select[@name="credit_card_collect_purchase[brand]"]')
    expiryMonth = (By.XPATH, '//select[@name="credit_card_collect_purchase[expire_month]"]')
    expiryYear = (By.XPATH, '//select[@name="credit_card_collect_purchase[expire_year]"]')
    country = (By.XPATH, '//select[@name="credit_card_collect_purchase[country]"]')


    page = AbstractPage()
    utility = Utils()

    def checkRoomAvailibility(self,context):

        context.browser.get(self.utility.readJSONDataValue(context,'defaultproperties','hotelBookingURL'));
        context.browser.maximize_window();
        end_date = self.utility.getRandomDate(context);
        self.page.webSendKeys(context,self.arrivalDate,end_date)
        self.page.webClickElement(context, self.numberOfNights);
        self.page.webClearFields(context,self.numberOfNights);
        self.page.webSendKeys(context,self.numberOfNights, self.utility.readJSONDataValue(context,'defaultproperties','numberOfNights'));
        self.page.webClearFields(context,self.numberOfAdults);
        self.page.webSendKeys(context,self.numberOfAdults,self.utility.readJSONDataValue(context,'defaultproperties','numberOfAdults'));
        self.page.webSendKeys(context,self.numberOfChildren, self.utility.readJSONDataValue(context,'defaultproperties','numberOfChildren'));
        self.page.webClickElement(context,self.bookNowButton);
        self.page.switchToIFrame(context,"clock_pms_iframe_1");
        self.page.scrollDownPage(context);
        self.page.webClickElement(context, self.deluxeApartmentRoom);

    def bookARoom(self, context):
        print('**Select Add On**');
        self.page.webSendKeys(context,self.addOn1, "1");
        self.page.webSendKeys(context,self.addOn2, "1");
        self.page.webClickElement(context,self.addSelectedAddOns);

        print('**Provide Details**');
        self.page.webSendKeys(context,self.emailId, self.utility.readJSONDataValue(context,'defaultproperties','emailId'));
        self.page.webSendKeys(context,self.lastName, self.utility.readJSONDataValue(context,'defaultproperties','firstName'));
        self.page.webSendKeys(context,self.firstName, self.utility.readJSONDataValue(context,'defaultproperties','numberOfChildren'));
        self.page.webSendKeys(context,self.phoneNumber, self.utility.readJSONDataValue(context,'defaultproperties','phoneNumber'));
        self.page.webClickElement(context,self.creditCardRadioButton);
        self.page.webClickElement(context,self.agreePolicyRadioButton);
        self.page.webClickElement(context,self.createBookingButton);

        print('**Provide Card Details**');
        self.page.webSendKeys(context, self.cardNumber, self.utility.readJSONDataValue(context,'creditCardDetails','number'));
        self.page.selectDropDownByName(context, self.dropDownBrand, self.utility.readJSONDataValue(context,'creditCardDetails','brand'));
        self.page.selectDropDownByName(context, self.expiryMonth, self.utility.readJSONDataValue(context,'creditCardDetails','expiryMonth'));
        self.page.selectDropDownByName(context, self.expiryYear, self.utility.readJSONDataValue(context,'creditCardDetails','expiryYear'));

        print('**Provide Billing Address**');
        self.page.webSendKeys(context, self.billingAddressLine, self.utility.readJSONDataValue(context,'billingAddressDetails','addLine'));
        self.page.webSendKeys(context, self.zip, self.utility.readJSONDataValue(context,'billingAddressDetails','zip'));
        self.page.webSendKeys(context, self.city, self.utility.readJSONDataValue(context,'billingAddressDetails','city'));
        self.page.webSendKeys(context, self.state, self.utility.readJSONDataValue(context,'billingAddressDetails','state'));
        self.page.selectDropDownByName(context, self.country, self.utility.readJSONDataValue(context,'billingAddressDetails','country'));
        self.page.webClickElement(context, self.payButton);

    def verifyRoomBooking(self, context):
        if(self.page.webIsElementDisplayed(context, self.successMessage)):
            assert True == True
        else:
            print('**Booking Failed**');
            assert True == False
