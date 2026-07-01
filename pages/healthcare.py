class healthcare:
    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.vertical_healthcare = page.locator('(//strong[text()="Healthcare"])')
        self.healthcare_diet_nutrition = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthcare_health_tracking = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthcare_list = [self.healthcare_diet_nutrition, self.healthcare_health_tracking]

    def healthcare_option_click(self):
        for k in self.healthcare_list:
            self.vertical.hover()
            self.vertical_healthcare.hover()
            k.click()
            self.page.go_back()