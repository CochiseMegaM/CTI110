#This is a code for sales Profit predictions
#Date: jun,18,2019
#CTI-110 P2T1-Sales Prediction
#Kenneth Howard
total_sales = float(input('Enter the projected sales:'))

# Calculate the profit as 23 persent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit,  ',.2f'))
