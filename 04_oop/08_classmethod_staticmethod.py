class FixetFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    
    def from_sum(self, value1, value2):
        return FixetFloat(value1 + value2)
    

number = FixetFloat(19.9999)
print(number)
new_number = FixetFloat.from_sum(1, 19, 20)
print(new_number)