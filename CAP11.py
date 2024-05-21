class Person:
    def __init__(self, name):
        self.name = name

    def calculate_tax(self, total_income):
        if total_income < 300000:
            print(f"{self.name} is exempted from taxation as gross income is below Nu. 300,000.")
            return 0  # Exempt from taxation if income is below 300,000

        tax_brackets = [
            (300000, 0.0),  
            (400000, 0.1),  
            (650000, 0.15), 
            (1000000, 0.2), 
            (1500000, 0.25), 
            (float('inf'), 0.3)  
        ]

        tax_payable = 0
        previous_limit = 0

        for limit, rate in tax_brackets:
            if total_income > limit:
                taxable_income = limit - previous_limit
                tax_payable += taxable_income * rate
                previous_limit = limit
            else:
                taxable_income = total_income - previous_limit
                tax_payable += taxable_income * rate
                break

        if tax_payable >= 1000000:
            tax_payable *= 1.1

        return tax_payable

class Employee(Person):
    def __init__(self, name, employment_income, pf_contribution, gis_contribution):
        super().__init__(name)
        self.employment_income = employment_income
        self.pf_contribution = pf_contribution
        self.gis_contribution = gis_contribution

    def calculate_income(self):
        return self.employment_income - self.pf_contribution - self.gis_contribution

class Landlord(Person):
    def __init__(self, name, rental_income):
        super().__init__(name)
        self.rental_income = rental_income

    def calculate_income(self):
        return self.rental_income * 0.8

class Investor(Person):
    def __init__(self, name, dividend_income):
        super().__init__(name)
        self.dividend_income = dividend_income

    def calculate_income(self):
        if self.dividend_income > 30000:
            return (self.dividend_income - 30000) * 0.9
        else:
            return self.dividend_income

class Consultant(Person):
    def __init__(self, name, other_income):
        super().__init__(name)
        self.other_income = other_income

    def calculate_income(self):
        return self.other_income * 0.7

# Example usage
employee = Employee("Tshechi", 500000, 50000, 10000)
landlord = Landlord("Pala", 400000)
investor = Investor("Lakezin", 100000)
consultant = Consultant("Wangchu", 700000)

# Calculate and print taxes
for person in [employee, landlord, investor, consultant]:
    income = person.calculate_income()
    tax = person.calculate_tax(income)
    print(f"{person.name}'s total income: Nu. {income:.2f}")
    print(f"{person.name}'s total tax payable: Nu. {tax:.2f}")
    print()
