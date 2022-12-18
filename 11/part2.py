import sys
from gmpy2 import mul, mpz


class Monkey:
    def __init__(self, name, items, operation, test, if_true, if_false, inspections=0):
        self.name = name
        self.items = list(map(int, items))
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = inspections

    def __str__(self):
        return (f"Monkey: {self.name}\nItems: {self.items}\nOper: {self.operation}\nTest: {self.test}\n"
            f"If true: {self.if_true}\nIf false: {self.if_false}\nInspections: {self.inspections}")

    def get_name(self):
        return self.name

    def get_items(self):
        return self.items
    
    def add_item(self, item):
        self.items.append(item)
    
    def pop_item(self):
        self.items.pop(0)

    def get_operation(self):
        return self.operation
    
    def get_test(self):
        return self.test

    def get_if_true(self):
        return self.if_true

    def get_if_false(self):
        return self.if_false
    
    def get_inspections(self):
        return self.inspections

    def inspect(self):
        self.inspections += 1


input = open(sys.argv[1], 'r').read().splitlines()

# List to hold monkey objects
monkeys = []

# Set up some temp vars to hold current monkey info as we loop through input
current_monkey = None
current_items = []
current_op = []
current_test = None
current_true = None
current_false = None

# We end up dealing with some real big numbers if we use the same logic as part 1
# To fix this, we multiply all the tests together to get a multiple of all tests
# Later we will first mod the operation result by this value, and then mod that value by the test
# and store the first mod value
modulo = 1

# Loop through the input grabbing the info about each monkey
for i, line in enumerate(input):
    line = line.strip()
    if line.startswith("Monkey"):
        current_monkey = line.split(" ")[-1].strip(":")
    elif line.startswith("Starting"):
        current_items = (line[16:].split(", "))
    elif line.startswith("Operation"):
        current_op = line.split(" ")[-3:]
    elif line.startswith("Test"):
        current_test = int(line.split(" ")[-1])
    elif line.startswith("If true"):
        current_true = int(line.split(" ")[-1])
    elif line.startswith("If false"):
        current_false = int(line.split(" ")[-1])
    # On blank lines we take what we currently know and create a monkey object
    # We also update our mod value with the current test
    elif line == "":
        monkeys.append(Monkey(current_monkey, current_items, current_op, 
            current_test, current_true, current_false))
        modulo *= current_test
    # Might be a better way to catch this but this creates the last monkey in 
    # the list as theres no blank line at the end of the input
    if i == (len(input) - 1):
        monkeys.append(Monkey(current_monkey, current_items, current_op, 
            current_test, current_true, current_false))
        modulo *= current_test
    
# Now lets run through 10000 rounds of passes and track number of times a monkey inspects an item
num_rounds = 10000

for i in range(num_rounds):
    for monkey in monkeys:
        item_list = list(monkey.get_items())

        for item in item_list:
            monkey.inspect()
            op = list(monkey.get_operation())

            for x in range(len(op)):
                if op[x] == "old":
                    op[x] = item
                    
            if op[1] == "+":
                op_result = int(op[0]) + int(op[2])
                op_result %= modulo
                test = op_result % monkey.get_test()
                if test == 0:
                    monkeys[monkey.get_if_true()].add_item(op_result)
                    monkey.pop_item()
                else:
                    monkeys[monkey.get_if_false()].add_item(op_result)
                    monkey.pop_item()
                
            elif op[1] == "*":
                op_result = int(op[0]) * int(op[2])
                op_result %= modulo
                test = op_result % monkey.get_test()
                if test == 0:
                    monkeys[monkey.get_if_true()].add_item(op_result)
                    monkey.pop_item()
                else:
                    monkeys[monkey.get_if_false()].add_item(op_result)
                    monkey.pop_item()
                    

inspection_list = []
for monk in monkeys:
    inspection_list.append(monk.get_inspections())

inspection_list.sort()
print(inspection_list[-1] * inspection_list[-2])