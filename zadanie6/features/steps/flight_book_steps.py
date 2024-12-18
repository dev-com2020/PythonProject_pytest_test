from behave import given, when, then
from booking_service import BookingService, Passenger

@given('Pasażer "{name}" ma {age:d} lat')
def step_impl(context, name, age):
    context.passenger = Passenger(name, age)

@given('Lot "{flight}" jest dostępny')
def step_impl(context, flight):
    context.flight = flight
    context.booking_service = BookingService()

@when('Pasażer rezerwuje lot "{flight}"')
def step_impl(context, flight):
    context.result = context.booking_service.book_flight(context.passenger, flight)

@when('Pasażer próbuje zarezerwować lot "{flight}"')
def step_impl(context, flight):
    try:
        context.result = context.booking_service.book_flight(context.passenger, flight)
    except ValueError as e:
        context.error_message = str(e)

@then('Rezerwacja jest potwierdzona')
def step_impl(context):
    assert context.result == "Rezerwacja potwierdzona", \
                    "Oczekiwano potwierdzenia rezerwacji."

@then('Rezerwacja jest odrzucona z powodu wieku')
def step_impl(context):
    assert context.error_message == "Pasażer jest niepełnoletni", \
                    "Oczekiwano odrzucenia rezerwacji z powodu wieku."