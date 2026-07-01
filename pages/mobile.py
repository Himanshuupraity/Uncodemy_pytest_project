class mobile:
    def __init__(self, page):
        self.page = page
        self.technologies_tab = page.locator('(//a[text()="Technologies"])[1]')
        self.mobile_dev_tab = page.locator('//strong[text()="Mobile App Development"]')
        self.mobile_react_native = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.mobile_xamarin = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.mobile_flutter = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.mobile_swift = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.mobile_enterprise = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.mobile_kotlin = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.mobile_ionic = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.mobile_appointment_booking = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobile_list = [self.mobile_react_native,self.mobile_xamarin,self.mobile_flutter,self.mobile_swift,self.mobile_enterprise,self.mobile_kotlin,self.mobile_ionic,self.mobile_appointment_booking]
    
    def mobile_option_click(self):
        for o in self.mobile_list:
            self.technologies_tab.hover()
            self.mobile_dev_tab.hover()
            o.click()
            self.page.go_back()
