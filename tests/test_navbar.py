import pytest

from pages.navbar import navbar

@pytest.mark.smoke
def test_navbar(page):
    a=navbar(page)
    a.navbar_click()