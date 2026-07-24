
class Calculator:
    def __init__(self):
        self.file_name = "Calculator_History.txt"
        with open(self.file_name,'a') as f:
            pass

    def show_history(self):
        with open(self.file_name,'r') as f:
            data = f.read()
            if data:
                print("-------History------")
                print(data)
            else:
                print("No Previous History")
        
    def save_history(self,data):
        with open(self.file_name,'a') as f:
            f.write(data+"\n")

    def clear_history(self):
        with open(self.file_name,'w') as f:
            pass 
        print('History Cleared Successfully....') 

    
    def add(self,a,b):
        add = a+b 
        print(add)
        data = f"{a} + {b} = {add}" 
        self.save_history(data) 

    def subtract(self,a,b):
        sub = a-b 
        print(sub)
        data= f"{a} - {b} = {sub}" 
        self.save_history(data) 

    def multiply(self,a,b):
        mul = a*b 
        print(mul)
        data = f"{a} * {b} = {mul}"  
        self.save_history(data)
        
    def divide(self,a,b):
        try:
            div = a/b 
            print(div)
            data =  f"{a} / {b} = {div}" 
            self.save_history(data)
        except ZeroDivisionError:
            print("You can't divide with 0.")

    def validate_entered_numbers(self,message):
        while True:
            try:
                value_of_num = int(input(message))
                return value_of_num
            except ValueError:
                print(" ")
                print("You entered an Invalid number.......!")
                print(" ")

    def get_numbers(self,choose_the_number):
        a = self.validate_entered_numbers("Enter the value of a: ")
        b = self.validate_entered_numbers("Enter the value of b: ")

        if choose_the_number == 1:
            self.add(a,b)

        elif choose_the_number == 2:
            self.subtract(a,b)

        elif choose_the_number == 3:
            self.multiply(a,b)

        elif choose_the_number == 4:
            self.divide(a,b)

def main():

    cal = Calculator()

    while True:

        print("*********************")
        print("Simple Calculator")
        print("*********************")

        print('1.Add')
        print('2.Subtract')
        print('3.Multiply')
        print('4.Divide')
        print('5.Show History')
        print("6.Clear History")
        print("7.Exit")
        print(" ")

        try:
            choose_the_number = int(input("Enter the Number from the Above: "))
        except ValueError:
            print("Invalid Number......!")
            print("")
            continue

        if choose_the_number in [1,2,3,4]:
            cal.get_numbers(choose_the_number)

        elif choose_the_number == 5:
            cal.show_history()

        elif choose_the_number == 6:
            cal.clear_history()

        elif choose_the_number ==7:
            print("Thank you for using the calculator..")
            break
        
        else:
            print("")
            print("Please enter the number from the given options......!")
            print("")

if __name__=="__main__":
    main()