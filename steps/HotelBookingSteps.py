from behave import *
import time
from pageclass.HotelBookingPage import  HotelBookingPage

bookingPage = None
class HotelBookingSteps:
      @given('I check the availability of a deluxe room')
      def step(context):
            global bookingPage;
            bookingPage = HotelBookingPage();
            bookingPage.checkRoomAvailibility(context);


      @when('I book the room')
      def step(context):
            bookingPage.bookARoom(context);

      @then('I verify the booking')
      def step(context):
            bookingPage.verifyRoomBooking(context);