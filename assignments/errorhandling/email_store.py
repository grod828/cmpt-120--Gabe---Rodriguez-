from ast import increment_lineno
from genericpath import exists
from logging import exception


class EmailStore:

    def __init__(self):
        '''
        Constructor method.
        '''
        self.emails = []

    def exists(self, email):
        '''
        Method that checks if an email exists in store.
        '''
        return email in self.emails

    def add(self, first_name, last_name):
        '''
        Method that adds a new email to the store.
        The email address is of the format {first_name}.{last_name}{count}@marist.edu

        @return the email that was added.
        '''
        # State if first name or last name is None, then ____ needs to occur (aka an exception)
        if first_name == None or last_name == None:
            raise Exception(
                "'first_name' and/or 'last_name' might not be None")

        email = None
        count = 1
        while True:
            email = f"{first_name.lower()}.{last_name.lower()}{count}@marist.edu"

            if self.exists(email):
                count += 1
                continue
            break

        self.emails.append(email)
        return email

    def remove(self, email):
        '''
        Method that removes an email from the store.
        '''
        if not self.exists(email):
            raise Exception("The email '{email}' does not already exist")
        else:
            self.emails.remove(email)
