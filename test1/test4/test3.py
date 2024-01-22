class PersonWithoutSelf:
    name = ""
    age = 0

    @staticmethod
    def set_name(new_name):
        PersonWithoutSelf.name = new_name

    @staticmethod
    def set_age(new_age):
        PersonWithoutSelf.age = new_age

    @staticmethod
    def greet():
        return f"Hello, my name is {PersonWithoutSelf.name} and I am {PersonWithoutSelf.age} years old."

# 클래스 메서드를 통해 이름과 나이 설정
PersonWithoutSelf.set_name("Alice")
PersonWithoutSelf.set_age(30)

# 클래스 메서드 호출
print(PersonWithoutSelf.greet())  # "Hello, my name is Alice and I am 30 years old."

# 다른 인스턴스에 대한 설정
PersonWithoutSelf.set_name("Bob")
PersonWithoutSelf.set_age(25)

# 동일한 클래스 메서드 호출
print(PersonWithoutSelf.greet())  # "Hello, my name is Bob and I am 25 years old."이 경우 PersonWithoutSelf 클래스는 모든 인스턴스에 대해 동일한 상태(즉, 최근에 설정된 이름과 나이)를 공유합니다. self가 없기 때문에, 각 인스턴스는 고유한 상태를 가질 수 없습니다.
