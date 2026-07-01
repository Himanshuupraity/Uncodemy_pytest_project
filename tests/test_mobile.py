import pytest

from pages.mobile import mobile


@pytest.mark.smoke
def test_mobile_click(page):
    a = mobile(page)
    a.mobile_option_click()


