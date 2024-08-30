def find_sum(value_1,value_2):
    try:
        print(value_1+value_3)
    except NameError:
        print("Function nffame error")
    finally:
        print("Sum finally")
try:
    find_sum(12,13)
except NameError:
    print("Invocation name error")
finally:
    print("Invocation finally")