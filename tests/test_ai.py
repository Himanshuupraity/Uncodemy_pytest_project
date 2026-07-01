import pytest


from pages.ai import ai

@pytest.mark.smoke
def test_ai_click(page):
    a = ai(page)
    a.ai_option_click()