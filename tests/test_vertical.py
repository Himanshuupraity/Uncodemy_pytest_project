
import pytest

from pages.vertical import vertical

@pytest.mark.smoke
def test_tradingoption_click(page):
    p = vertical(page)
    p.trading_option_click()
