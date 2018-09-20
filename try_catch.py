def divide():
    try:
        input_no1=int(input("enter no1\t"))
        input_no2=int(input("enter no2\t"))
        div=input_no1/input_no2
        print(div)
    except Exception as e:
        print("the error is", e), type(e)
    finally:
        print("The program ends here ")
        
#catching error for a particular exception:
#except ZeroDivisionError :
#       print("Do not enter zero in sec no")
divide()
