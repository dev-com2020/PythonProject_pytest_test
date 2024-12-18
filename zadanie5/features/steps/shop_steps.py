from behave import *

SHOP_URL = "https://magento.softwaretestingboard.com/"

@given("ładujemy adres strony")
def step_impl(context):
    context.page.goto(SHOP_URL)
    print("Strona ładuje się...")

@when('Szukam "{product}"')
def step_impl(context, product):
    search_box = context.page.wait_for_selector("input[name='q']")
    search_box.fill(product)
    search_box.press("Enter")
    print(f"Wyszukano: {product}")

@then("Powinna wyświetlić się strona z koszulkami")
def step_impl(context):
    context.page.wait_for_selector("h1.page-title")
    search_result_text = context.page.locator("h1.page-title").text_content()
    assert "shirt" in search_result_text, "Nie znaleziono"
    print("Wyniki poprawne")

@then('strona powinna wyświetlić {exp_title}')
def step_impl(context, exp_title):
    actual_title = context.page.title()
    assert actual_title == exp_title, "nie znaleziono"

