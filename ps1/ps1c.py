# Take input
annual_salary = float(input("Enter the starting salary: "))

#Initialize variables
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = 0.25
r = 0.04
months = 36
max_portion_saved = 1
min_portion_saved = 0
portion_saved = 0
steps = 0
possible = False

#check whether it is possible to meet the target with current portion saved
while max_portion_saved!=min_portion_saved:
    steps+=1
    portion_saved = round((max_portion_saved+min_portion_saved)/2,4)
    current_savings = 0
    current_salary = annual_salary
    for month in range(months):
        current_savings = current_savings*(1+r/12)+portion_saved*current_salary/12
        if month%6==0:
            current_salary *= (1+semi_annual_raise)
    diff = current_savings - total_cost*portion_down_payment
    if abs(diff)<=100:
        possible = True
        break
    elif diff<0:
        min_portion_saved = portion_saved+0.0001
    else:
        max_portion_saved = portion_saved-0.0001

#print output
if possible:
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years")
