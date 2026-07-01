import pytest

from pages.social_link import social


@pytest.mark.smoke

def test_social(page):
    a=social(page)
    a.social_click()