import pytest


from pages.contact_form import c_form

@pytest.mark.smoke
def test_contat(page):
    a= c_form(page)
    a.form_option_fill()