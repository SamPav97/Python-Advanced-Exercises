def endsw(comm, doms):
    result = False
    for dom in doms:
        if comm.endswith(dom):
            result = True
    return result


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = [".com", ".bg", ".org", ".net"]
while True:
    # Input an email
    command = input()
    if command == "End":
        break
    # Check if @ is in the given email
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    # Split by @ to have the separate the name and domain
    command = command.split("@")
    # Check if the name has the necessary length
    if len(command[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
    # Function that receives the domain of the given email and checks if that domain is in the allowed domains
    # Function returns True if given domain is in valid domains
    if not endsw(command[1], domains):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(domains)}")

    print("Email is valid")
