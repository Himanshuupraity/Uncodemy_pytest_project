import pytest



from pages.ecom import ecom

@pytest.mark.smoke
def test_ecom_click(page):
    a = ecom(page)
    a.ecom_option_click()