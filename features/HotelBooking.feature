Feature: Hotel Booking Scenario

@hotelBooking
Scenario: Book a deluxe room in hotel
	Given I check the availability of a deluxe room
	When I book the room
    Then I verify the booking