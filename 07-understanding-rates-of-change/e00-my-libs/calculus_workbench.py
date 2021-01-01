from my_calculus import get_cumulative_value_function, get_integral_function, approximate_integral_value, get_approximate_average_rate_function, get_approximate_derivative_function, approximate_derivative_value

# This is the actual volume function
def actual_volume(t):
    return (t - 4) ** 3 / 64 + 3.3

# This is the actual flow rate function
def actual_flow_rate(t):
    return 3*(t-4)**2 / 64

# Let's get the function and compare a few values
estimated_volume = get_cumulative_value_function(actual_flow_rate, actual_volume(0), digits=3)

for t in range(1, 11):
    print('Actual={}; Estimated={}'.format(actual_volume(t), estimated_volume(t)))
print('======================\n')

# Validating the syntactic sugar
estimated_integral = get_integral_function(actual_flow_rate, actual_volume(0), digits=3)

for t in range(1, 11):
    print('Actual={}; Estimated={}'.format(actual_volume(t), estimated_integral(t)))

print('======================\n')
for x in range(1, 11):
    print('Actual={}; Estimated={}'.format(actual_volume(x), approximate_integral_value(actual_flow_rate, actual_volume(0), 0.5, x)))


## Now doing some validation on derivatives
print('======================\n')
estimated_flow_rate = get_approximate_average_rate_function(actual_volume, digits=3)

for x in range(1, 11):
    print('Actual={}; Estimated={}'.format(actual_flow_rate(x), estimated_flow_rate(x)))

## And some validation on the syntactic sugar
print('======================\n')
estimated_derivative = get_approximate_derivative_function(actual_volume, digits=3)

for x in range(1, 11):
    print('Actual={}; Estimated={}'.format(actual_flow_rate(x), estimated_derivative(x)))

print('======================\n')
for x in range(1, 11):
    print('Actual={}; Estimated={}'.format(actual_flow_rate(x), approximate_derivative_value(actual_volume, x, digits=6)))
