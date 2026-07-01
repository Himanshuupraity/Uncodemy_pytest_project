class ai:
    def __init__(self, page):
        self.page = page
        self.technologies_tab = page.locator('(//a[text()="Technologies"])[1]')
        self.artificial_int_tab = page.locator('//strong[text()="Artificial Intelligence"]')


    def ai_option_click(self):
        self.technologies_tab.hover()
        self.artificial_int_tab.click()
        self.page.go_back()