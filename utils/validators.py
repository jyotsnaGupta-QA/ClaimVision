import re
from datetime import datetime


class Validator:

    @staticmethod
    def validate_name(name):

        if not name.strip():
            return "Full Name is required."

        if len(name.strip()) < 3:
            return "Full Name must be at least 3 characters."

        if not re.match(r"^[A-Za-z ]+$", name):
            return "Full Name can contain only letters."

        return None

    @staticmethod
    def validate_email(email):

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, email):
            return "Invalid email address."

        return None

    @staticmethod
    def validate_phone(phone):

        if not phone.isdigit():
            return "Phone Number must contain only digits."

        if len(phone) != 10:
            return "Phone Number must be exactly 10 digits."

        return None

    @staticmethod
    def validate_vehicle_number(number):

        pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$'

        if not re.match(pattern, number):
            return "Invalid vehicle number."

        return None

    @staticmethod
    def validate_year(year):

        current_year = datetime.now().year

        if year < 1990 or year > current_year:
            return "Invalid manufacturing year."

        return None

    @staticmethod
    def validate_policy(policy):

        if len(policy.strip()) < 8:
            return "Invalid policy number."

        return None

    @staticmethod
    def validate_location(location):

        if not location.strip():
            return "Accident location is required."

        return None

    @staticmethod
    def validate_description(description):

        if len(description.strip()) < 20:
            return (
                "Accident description must be at least "
                "20 characters."
            )

        return None