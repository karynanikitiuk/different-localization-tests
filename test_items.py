link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        "Basket button isn't shown!"
