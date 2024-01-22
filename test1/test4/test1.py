class MyClass:
    def __init__(self,age) -> None:
        age = 0
        self.age = 0
    
    def my_static_method(self):
        print(MyClass.age)
        return "Hello, this is a static method!"
    def add():
        MyClass.age += 1
        return

# 클래스 이름으로 직접 호출
print(MyClass.my_static_method())  # "Hello, this is a static method!"


print(MyClass.add())  # "Hello, this is a static method!"
print(MyClass.my_static_method())  # "Hello, this is a static method!"
my_instance = MyClass()
print(my_instance.my_static_method())  