class Address:

    def __init__(self, is_male: bool,
                 firstname: str, lastname: str,
                 address_line_1: str, address_line_2: str,
                 pcode: str, town: str, phone: str = "", country: str = "CH"):
        self.is_male = is_male
        self.firstname = firstname
        self.lastname = lastname
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.pcode = pcode
        self.town = town
        self.phone = phone
        self.country = country

    def __repr__(self):
        return f"Address(is_male: {self.is_male}, fistname: {self.firstname}, lastname: {self.lastname})"


class Fee:

    def __init__(self, description: str, price: float, unit: float = 1):
        self.description = description
        self.price = price
        self.unit = unit

    def __repr__(self):
        return f"<{self.__class__.__name__}(description: {self.description}, units: {self.unit}, price {self.price})>"

    @property
    def total_costs(self) -> float:
        return self.unit * self.price


class Expense:

    def __init__(self, description: str, amount: float):
        self.description = description
        self.amount = amount

    def __repr__(self):
        return f"<{self.__class__.__name__}(description: {self.description}, amount: {self.amount})>"

    @property
    def total_costs(self) -> float:
        return self.amount
