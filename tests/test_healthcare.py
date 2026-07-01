import pytest

from pages.healthcare import healthcare
@pytest.mark.smoke
def test_healthcare(page):
    a=healthcare(page)
    a.healthcare_option_click()
