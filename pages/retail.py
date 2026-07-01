class retail:
    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.vertical_retail = page.locator('(//strong[text()="Retail and Ecommerce"])')
        self.retail_ecommerce_website = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.retail_ecommerce_app = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retail_list=[self.retail_ecommerce_website, self.retail_ecommerce_app]
    
    def retail_option_click(self):
        for j in self.retail_list:
            self.vertical.hover()
            self.vertical_retail.hover()
            j.click()
            self.page.go_back()