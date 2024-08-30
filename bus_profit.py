def calculate(distance,no_of_passengers):
    fuel_price_per_liter = 70
    bus_mileage = 10 
    ticket = 80
     
    profit = (no_of_passengers * ticket) 
    loss = (distance / bus_mileage) * 70
    total_profit = profit - loss
    if total_profit > 0:
        return total_profit
    else:
        return -1
#Provide different values for distance, no_of_passenger and test your program
distance=100
no_of_passengers=10
print(calculate(distance,no_of_passengers))


'''Assume that the following information are given:
Price per litre of fuel = 70
Mileage of the bus in km/litre of fuel = 10
Price(Rs) per ticket = 80

The bus runs on multiple routes having different distance in kms and number of passengers.
Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.'''