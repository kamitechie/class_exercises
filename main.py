from datetime import date

# Challenge 1 - Dog class


class Dog:

    def __init__(self, name, size, breed='Unknown', date_of_birth=None):
        self.name = name
        self.size = size
        self.breed = breed
        self.date_of_birth = date_of_birth

    def bark(self):
        return 'woof!'

    def get_name(self):
        return self.name

    def set_name(self, set_name):
        if len(set_name) < 2 or len(set_name) > 30:
            return 'Name should be between 2 and 30 letters'
        else:
            self.name = set_name.title()
            return self.name

    def dog_years(self):
        return (date.today().year - self.date_of_birth.year)*7

    def formatted_birth_date(self):
        return self.date_of_birth.strftime('%d/%m/%Y')
