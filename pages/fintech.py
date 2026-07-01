class fintech:
    def __init__(self, page):
        self.page=page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.vertical_fintech = page.locator('(//strong[text()="Fintech"])')
        self.fintech_pos_software = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.fintech_crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintech_list=[self.fintech_pos_software, self.fintech_crypto]
    
    def fintech_option_click(self):
        for l in self.fintech_list:
            self.vertical.hover()
            self.vertical_fintech.hover()
            l.click()
            self.page.go_back()