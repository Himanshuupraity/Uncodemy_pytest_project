


import pytest

from pages.custom import custom

@pytest.mark.smoke
def test_custom_click(page):
    a = custom(page)
    a.custom_option_click()