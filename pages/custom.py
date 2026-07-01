class custom:
    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.vertical_custom = page.locator('(//a[@href="#"])[4]')
        self.custom_desktop_app = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.custom_hrm_development = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.custom_travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.custom_dating_app = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.custom_crm_usa = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.custom_crm_development = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.custom_erp_app = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.custom_e_learning = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.custom_real_estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.custom_list=[self.custom_desktop_app, self.custom_hrm_development, self.custom_travel, self.custom_dating_app, self.custom_crm_usa,self.custom_crm_development, self.custom_erp_app, self.custom_e_learning, self.custom_real_estate]
    
    def custom_option_click(self):
        for m in self.custom_list:
            self.vertical.hover()
            self.vertical_custom.hover()
            m.click()
            self.page.go_back()