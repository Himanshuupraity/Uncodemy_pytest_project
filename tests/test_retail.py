import pytest

from pages.retail import retail

@pytest.mark.smoke
def test_retailoption_click(page):
    a= retail(page)
    a.retail_option_click()