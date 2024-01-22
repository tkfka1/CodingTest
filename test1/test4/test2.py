       
class PersonWithSelf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# 객체 생성
person1 = PersonWithSelf("Alice", 30)
person2 = PersonWithSelf("Bob", 25)

# 각 객체의 메서드 호출
print(person1.greet())  # "Hello, my name is Alice and I am 30 years old."
print(person2.greet())  # "Hello, my name is Bob and I am 25 years old."여기서 person1과 person2는 각각 다른 name과 age 값을 가집니다. self를 사용함으로써 각 인스턴스는 독립된 상태를 유지합니다.


