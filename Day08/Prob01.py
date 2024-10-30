
class Employees:

    head = None

    @classmethod
    def set_head(cls, head_name):
        cls.head = head_name

    @classmethod
    def get_head(cls):
        return cls.head

Employees.set_head("Micheal")
print(Employees.get_head())




