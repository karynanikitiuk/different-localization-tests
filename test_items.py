import time

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        "Basket button isn't shown!"
