class GreenCardRegistration:
    ALLOWED_COUNTRIES = ["Ukraine", "Poland", "Germany", "USA"]
    MIN_PERSON_AGE = 18
    MAX_PERSON_AGE = 70

    def __init__(self, person_name, person_age, country):
        self.__person_name = person_name
        self.__person_age = person_age
        self.__country = country

    @property
    def person_name(self):
        return self.__person_name

    @person_name.setter
    def person_name(self, name):
        self.__person_name = name

    @property
    def person_age(self):
        return self.__person_age

    @person_age.setter
    def person_age(self, age):
        self.__person_age = age

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @staticmethod
    def is_name_valid(person_name):
        """Check validation of the person name

        Args:
            person_name (str): Valid person name

        Returns:
            bool: Check if all of the characters in string are letters and if the name length is more than 3 symbols
        """
        return person_name.isalpha() and len(person_name) >= 3

    @classmethod
    def is_eligible_for_registration(cls, person_age, country):
        """Check allowed conditions for registration

        Args:
            person_age (int): Age of person who wants to be registered
            country (str): Country of registration

        Returns:
            bool: Check if range of age and country are allowed for registration
        """
        return (cls.MIN_PERSON_AGE <= person_age <= cls.MAX_PERSON_AGE) and (country in cls.allowed_countries)

    def register_person(self):
        """ Register the person for the Green Card

        Returns:
            str: Result message about the registration status

        """

        if not GreenCardRegistration.is_name_valid(self.person_name):
            return "Invalid name: '{self.person_name}'. Please ensure your name contains only letters and is at least 3 characters long"

        if not GreenCardRegistration.is_eligible_for_registration(self.person_age, self.country):
            return (f"Registration failed for {self.person_name}. "
                    f"Eligibility criteria not met: Age must be between {
                        self.MIN_PERSON_AGE} and {self.MAX_PERSON_AGE}, "
                    f"and the country of registration must be one of the following: {', '.join(GreenCardRegistration.allowed_countries)}.")
        return f"Registration successful for {self.person_name}. Welcome to {self.country}!"


person = GreenCardRegistration(
    person_name='James', person_age=25, country='Ukraine')
# Registration successful for James. Welcome to Ukraine!
print(person.register_person())

person2 = GreenCardRegistration(
    person_name='Bob', person_age=45, country='France')
# Registration failed for Viktoria. Eligibility criteria not met: Age must be between 18 and 70, and the country of registration must be one of the following: Ukraine, Poland, Germany, USA.
print(person2.register_person())

person3 = GreenCardRegistration(
    person_name='Viktoria', person_age=75, country='Poland')
# Registration failed for Viktoria. Eligibility criteria not met: Age must be between 18 and 70, and the country of registration must be one of the following: Ukraine, Poland, Germany, USA.
print(person3.register_person())

person4 = GreenCardRegistration(
    person_name='_%', person_age=35, country='')
# Registration failed for Viktoria. Eligibility criteria not met: Age must be between 18 and 70, and the country of registration must be one of the following: Ukraine, Poland, Germany, USA.
print(person3.register_person())

person4 = GreenCardRegistration(
    person_name='', person_age=35, country='Poland')
# Registration failed for Viktoria. Eligibility criteria not met: Age must be between 18 and 70, and the country of registration must be one of the following: Ukraine, Poland, Germany, USA.
print(person3.register_person())

person4 = GreenCardRegistration(
    person_name='W Test', person_age=35, country='Poland')
# Registration failed for Viktoria. Eligibility criteria not met: Age must be between 18 and 70, and the country of registration must be one of the following: Ukraine, Poland, Germany, USA.
print(person3.register_person())
