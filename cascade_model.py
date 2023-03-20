import click
import pandas as pd
import numpy as np


class Configuration:

    def __init__(self, name, config, costs):
        self.config = config
        self.name = name
        self.costs = costs

    def __repr__(self) -> str:
        return f"{type(self).__name__}(config={self.config})"

    def get_total_cost(self, scale=""):
        """ Returns the total cost of all components across this cascade.
        If a scale factor is provided then access the scaled quantity values (or calculate them if not already there)

        :param str scale: scale factor to check or calculate
        :return: sum of all costs for the given scale
        """

        """
        Send a message to a recipient.

        :param str sender: The person sending the message
        :param str recipient: The recipient of the message
        :param str message_body: The body of the message
        :param priority: The priority of the message, can be a number 1-5
        :type priority: integer or None
        :return: the message id
        :rtype: int
        :raises ValueError: if the message_body exceeds 160 characters
        :raises TypeError: if the message_body is not a basestring
        """
        # If this scale value isn't already calculated, calculate it now
        if f'cost{scale}' not in self.config.columns:
            self.scale_cost(scale)

        return self.config[f'cost{scale}'].sum()

    def print_detailed_info(self, sort_expensive=False, scale=""):
        """
        print_detailed_info is a wrapper around get_detailed_info that will print the list of components and prices


        :param sort_expensive: boolean to set if we want to report the most expensive items first
        :return: print the list of all components and costs
        """
        detail_list = self.get_detailed_info(sort_expensive, scale)

        if sort_expensive:
            print("Most expensive components are listed first")
        for x in detail_list:
            print(x)


    def get_detailed_info(self, sort_expensive=False, scale="") -> "pd.series.Series":

        # If this scale value isn't already calculated, calculate it now
        if f'cost{scale}' not in self.config.columns:
            self.scale_cost(scale)

        if sort_expensive:
            config = self.config.sort_values(f'cost{scale}', ascending=False)
        else:
            config = self.config

        detail_list = config.apply(
            lambda row: self.print_row_detail(row, scale) if row.notnull().all() else "", axis=1)

        return detail_list

    def print_row_detail(self, row, scale):
        # Work out if we have an exact price for this quantity or not
        # This means if the quantity in the configuration is listed directly in the Costs csv

        detail_str = ""

        if row[f'quantity{scale}'] == row[f'reference_quantity{scale}']:
            price_detail = "priced from a direct reference to this quantity"
        else:
            price_detail = f"priced from an estimation based on a quantity of {row[f'reference_quantity{scale}']} at a cost of ${row[f'reference_cost{scale}']}"

        detail_str += f"Component is {row.component} and it costs ${row[f'cost{scale}']} at a quantity of {row[f'quantity{scale}']}\n"
        detail_str += f"It is {price_detail}"

        return detail_str

    def scale_cost(self, scale):

        self.config[f'quantity{scale}'] = self.config['quantity'] * scale

        self.config[[f'cost{scale}', f'reference_quantity{scale}', f'reference_cost{scale}']] = self.config.apply(
            lambda row: cost_component(row['component'], row[f'quantity{scale}'],
                                       self.costs) if row.notnull().all() else "", axis=1)


def load_configurations(costs, configs):
    print('\nLoading configurations\n')

    # Load and validate the Costs csv
    costs = pd.read_csv(costs)

    # Drop any rows that only contain null values
    costs.dropna(axis=0, how='all', inplace=True)


    # Convert the headers to lowercase
    costs.columns = [c.lower() for c in costs.columns]

    # Check that the costs are all floats
    try:
        np.array_equal(costs['cost'], costs['cost'].astype(float))
    except ValueError as err:
        print(err)
        raise ValueError("All values in Costs csv Costs column should be floats")

    # Check that the correct headers are in the costs csv
    for req in ['name', 'quantity', 'cost']:
        if req not in costs.columns.values:
            raise ValueError("Costs csv should have Name, Quantity, Cost as headers")

        if costs[req].isna().any():
            raise ValueError(f"A {req} in Costs csv does not have a value")

    # Convert the values in Name column to lowercase
    costs['name'] = costs['name'].apply(str.lower)

    # Check that there are no duplicate name + quantity values
    name_quantity = costs['name'].apply(str) + costs['quantity'].apply(str)
    if not name_quantity.is_unique:
        raise ValueError("Costs csv contains non-unique component and quantity value pairs")

    # Load and validate the Configurations csv
    configs = pd.read_csv(configs)

    # Drop any rows that only contain null values
    configs.dropna(axis=0, how='all', inplace=True)


    # Convert the headers to lowercase
    configs.columns = [c.lower() for c in configs.columns]

    # Get all the names of configs
    config_names = configs['name'].dropna().unique()

    # Check that the quantities are all floats
    try:
        np.array_equal(configs['quantity'], configs['quantity'].astype(float))
    except ValueError as err:
        raise ValueError("'All values in Configurations csv Quantity column should be floats")

    # Check that the correct headers are in the configs csv
    for req in ['name', 'component', 'quantity']:
        if req not in configs.columns.values:
            raise ValueError("Configs csv should have Name, Component, Quantity as headers")

        if configs[req].isna().any():
            raise ValueError(f"A {req} in Configurations csv does not have a value")

    # Convert the values in the Component column to lowercase
    configs['component'] = configs['component'].apply(str.lower)


    # If there are no configs throw an error
    if config_names.size == 0:
        raise ValueError("No configs are present in the Config csv")

    # Add all the components to the configs

    costed_list = []

    configs[['cost', 'reference_quantity', 'reference_cost']] = configs.apply(
        lambda row: cost_component(row['component'], row['quantity'], costs) if row.notnull().all() else "", axis=1)

    for name in config_names:
        costed_list.append(Configuration(name, configs[configs['name'] == name], costs))

    return costed_list


def cost_component(component, quantity, costs):
    if component.lower() not in costs['name'].values:
        raise ValueError(f"Component defined in Configs is not present in Costs - {component}")

    # Get all the quantities and costs for the component as defined in the Costs csv
    cost_df = costs[costs['name'] == component]

    # Work out which quantity from Costs is closest to the quantity we want in Configurations
    closest_index = (cost_df.quantity - quantity).abs().idxmin()

    scaled_cost = quantity / costs.iloc[closest_index].quantity * costs.iloc[closest_index].cost

    return pd.Series([scaled_cost, costs.iloc[closest_index].quantity, costs.iloc[closest_index].cost])

@click.command()
@click.option('--costs', default='./cascade_costs.csv', help="Location of costs csv", )
@click.option('--configs', default="./cascade_configurations.csv", help='Location of configurations csv')
def create_cascade_models(costs, configs):
    """Main method that loads all available cascade configurations"""
    config_list = load_configurations(costs, configs)

    for config in config_list:
        print(f'Printing details of {config.name}\n')
        config.print_detailed_info()

        print(f"\nTotal cost of {config.name} is {config.get_total_cost()}\n")


if __name__ == '__main__':
    create_cascade_models()
