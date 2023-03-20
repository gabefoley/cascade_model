import cascade_model

# Paths where the Costs and Configurations spreadsheets are stored
cost_path = "./test/files/test_cascade_costs.csv"
config_path = "./test/files/test_cascade_configurations.csv"

# Path with a Configuration where the exact quantites don't match what we have in the Costs spreadsheet and will need to be re-estimated
reestimate_config_path = "./test/files/test_cascade_configurations.csv"

config_list = cascade_model.load_configurations(cost_path, config_path)

# Load the two configurations and print their detailed info and total cost
for config in config_list:
    print(f'Printing details of {config.name}\n')
    config.print_detailed_info()

    print(f"\nTotal cost of {config.name} is ${config.get_total_cost()} \n")


# Scale one of the cascades and print the scaled values

small_cascade = config_list[0]

print("------------------------------------------")

print (f"Now lets scale all the quantities of {small_cascade.name} by 3\n")
small_cascade.scale_cost(3)
print (f"The previous total cost was {small_cascade.get_total_cost()} but now it is {small_cascade.get_total_cost(scale=3)}")
print("------------------------------------------")

print ("You can either scale the cost directly by using 'scale_cost' or if you pass a scale value to 'get_total_cost' or 'print_detailed_info' it will scale it for you")

print (f"Print the detailed info for {small_cascade.name} after scaling it by 10\n")
small_cascade.print_detailed_info(scale=10)
print(f"\nTotal cost of {small_cascade.name} is ${small_cascade.get_total_cost(scale=10)} \n")
