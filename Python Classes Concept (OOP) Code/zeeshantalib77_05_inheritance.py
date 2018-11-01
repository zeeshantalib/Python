#--------------------------- Inheritance

class Parent1:
    value1="P1 1"
    value2="P1 2"
class Parent2:
    value1="P2 1"
    value2="P2 2"

class Child (Parent1,Parent2):
      pass
parent_=Parent1()
print(parent_.value1)
print(parent_.value2)

child_=Child()
print(child_.value1)
print(child_.value2)

