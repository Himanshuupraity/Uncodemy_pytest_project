import pytest

from pages.fintech import fintech

@pytest.mark.smoke
def test_fintech_click(page):
    a = fintech(page)
    a.fintech_option_click()