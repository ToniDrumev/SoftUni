import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAtSymbolError(Exception):
    pass


class InvalidCharacterError(Exception):
    pass


DOMAINS = (".com", ".bg", ".org", ".net")

email = input()

while True:
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    if email.count("@") > 1:
        raise MustContainOnlyOneAtSymbolError("Email must contain only one @!")

    if len(email.split("@")[0]) < 4:
        raise NameTooShortError("Email name must be at least 5 characters long!")

    if not re.findall(r'\w+', email)[0]:
        raise InvalidCharacterError("Email name must contain only alpha-numeric and underscore characters!")

    if re.findall(r'\.\w+', email)[-1] not in DOMAINS:
        raise InvalidDomainError("Email domain must be one of following: .com, .bg, .org, .net!")

    print("Email is valid!")

    email = input()
