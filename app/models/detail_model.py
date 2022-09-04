class DetailModel(dict):
    @property
    def name(self):
        return self.__dict__["Name"]

    @name.setter
    def name(self,name_param):
        self.__dict__["Name"] = name_param

    @property
    def surname(self):
        return self.__dict__["Surname"]

    @surname.setter
    def surname(self, surname_param):
        self.__dict__["Surname"] = surname_param

    @property
    def identityNumber(self):
        return self.__dict__["IdentityNumber"]

    @identityNumber.setter
    def identityNumber(self, identityNumber_param):
        self.__dict__["IdentityNumber"] = identityNumber_param

    @property
    def email(self):
        return self.__dict__["Email"]

    @email.setter
    def email(self, email_param):
        self.__dict__["Email"] = email_param

    @property
    def phoneNumber(self):
        return self.__dict__["PhoneNumber"]

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber_param):
        self.__dict__["PhoneNumber"] = phoneNumber_param

    @property
    def applicationDate(self):
        return self.__dict__["ApplicationDate"]

    @applicationDate.setter
    def applicationDate(self, applicationDate_param):
        self.__dict__["ApplicationDate"] = applicationDate_param

    @property
    def howToApply(self):
        return self.__dict__["HowToApply"]

    @howToApply.setter
    def howToApply(self, howToApply_param):
        self.__dict__["HowToApply"] = howToApply_param

    @property
    def freetext(self):
        return self.__dict__["Freetext"]

    @freetext.setter
    def freetext(self, freetext_param):
        self.__dict__["Freetext"] = freetext_param