import pytest


from pages.blog_cat import blog_cat

@pytest.mark.smoke
def test_blog_click(page):
    a=blog_cat(page)
    a.blog_cat_option_click()