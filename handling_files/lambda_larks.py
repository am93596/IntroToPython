# Lambda Functions

def add(n1, n2):
    return n1 + n2


print(add(2, 4))


add2tog = lambda n1, n2: n1 + n2
print(add2tog(2, 4))


# Map

def double_add_one(n):
    return (n * 2) + 1


nums = [1, 2, 3, 4, 5]
new_nums = list(map(double_add_one, nums))
print(new_nums)

new_nums2 = list(map(lambda n: (n * 2) + 1, nums))
print(new_nums2)

savings = [234.00, 555.00, 674.00, 78.00]
# savings = each saving plus 10%
# implement this using map and a lambda function
increased_savings = list(map(lambda n: n + n/10, savings))
print(increased_savings)


# Filter
def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, nums)))  # Filter will keep anything that is true, and drop anything that is false

# Write the above using a lambda function
print(list(filter(
    lambda n: n % 2 == 0, range(210)
)))

# AND NOW FOR SOMETHING COMPLETELY DIFFERENT

# List Comprehension

savings = [234.00, 555.00, 674.00, 78.00]
bonus = [x + x/10 for x in savings] # Square brackets for a list; round brackets for a generator; designed for iterating over and getting one at a time
#print(bonus)

large_savings = [x for x in savings if x > 500]
print(large_savings)

large_savings_bonus = [x + x/10 for x in savings if x > 500]
print(large_savings_bonus)
