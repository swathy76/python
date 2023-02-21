class Time:
    def __init__(self):
        self.__hr=int(input("Enter the hour:"))
        self.__min=int(input("Enter the minute:"))
        self.__sec=int(input("Enter the second:"))
    def __add__(self,ob2):
        hour=self.__hr+ob2.__hr
        print()
        print("sum of hours:",hour)
        minute=self.__min+ob2.__min
        print("sum of minutes:",minute)
        second=self.__sec+ob2.__sec
        print("sum of second:",second)
        if hour>24:
            hour=hour%24
        if minute>=60:
            hour=hour+minute//60
            minute=minute%60
        if second>=60:
            minute=minute+second//60
            second=second%60
        return hour,minute,second
print("Enter the time for 1st object:")
obj1=Time()
print()
print("Enter the time for 2nd object:")
obj2=Time()
sum=obj1+obj2
print()
print("sum is",sum)