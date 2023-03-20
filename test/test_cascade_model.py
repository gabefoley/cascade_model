import cascade_model
import pytest
import subprocess
from click.testing import CliRunner



def test_successful_model():
    # Basic test to check that the Configuration can be loadad correctly
    config_list = cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                                    "./files/test_cascade_configurations.csv")

    # Check that lengths of list and names are correct
    assert (len(config_list) == 2)
    assert (config_list[0].name == 'Small_cascade')
    assert (config_list[1].name == 'Alginate_cascade')

    small_cascade = config_list[0]

    # Check that total cost of a Configuration is correct
    assert (small_cascade.get_total_cost() == 141)

    # Check that sorting the detailed info by expense works
    lines = small_cascade.get_detailed_info(sort_expensive=True)

    assert next(x for x in
                lines) == "Component is beaker and it costs $100.0 at a quantity of 20.0\nIt is priced from a direct " \
                          "reference to this quantity"

    # Check that not sorting the detailed info by expense works
    lines = small_cascade.get_detailed_info(sort_expensive=False)

    assert next(x for x in
                lines) == "Component is dhad and it costs $12.0 at a quantity of 10.0\nIt is priced from a direct " \
                          "reference to this quantity"


def test_upscaling_model():
    # Test to check that upscaling the configurations works

    config_list = cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                                    "./files/test_cascade_configurations.csv")

    small_cascade = config_list[0]

    # Create new columns that scale these quantities by 2 and then generate updated costs
    scale_factor = 2
    small_cascade.scale_cost(scale_factor)

    assert (small_cascade.get_total_cost() == 141)
    assert (small_cascade.get_total_cost(scale=scale_factor) == 282)

def test_checking_upscale_amount_without_upscaling_first():
    # If we ask for the total cost of a scale factor we haven't calculated, it should be calculated and then returned
    config_list = cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                                    "./files/test_cascade_configurations.csv")

    small_cascade = config_list[0]

    # Set the scale_factor but don't explicitly scale the configuration
    scale_factor = 2

    assert (small_cascade.get_total_cost() == 141)
    assert (small_cascade.get_total_cost(scale=scale_factor) == 282)

def test_estimating_cost_non_default_higher():

    config_list = cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                                    "./files/test_cascade_configurations_estimate_cost_small.csv")


    assert (len(config_list) == 1)
    assert (config_list[0].name == 'Estimated_cascade')

    small_cascade = config_list[0]

    # Check that total cost of a Configuration is correct
    assert (small_cascade.get_total_cost() == 26)

    # Check that sorting the detailed info by expense works
    lines = small_cascade.get_detailed_info(sort_expensive=True)

    assert lines[0] == "Component is dhad and it costs $24.0 at a quantity of 20\nIt is priced from an estimation based on a quantity of 10.0 at a cost of $12.0"
    assert lines[1] == "Component is kari and it costs $2.0 at a quantity of 5\nIt is priced from an estimation based on a quantity of 10.0 at a cost of $4.0"


def test_from_command_line():

    # Basic test to check that the Configuration can be loadad correctly
    costs = "./files/test_cascade_costs.csv"
    configs = "./files/test_cascade_configurations.csv"

    result = subprocess.check_output(['python', '../cascade_model.py', '--costs', costs, '--configs', configs])

    assert ('Total cost of Alginate_cascade is 231.0' in result.decode())


def test_command_line_directly():

    # Basic test to check that the Configuration can be loadad correctly
    costs = "./files/test_cascade_costs.csv"
    configs = "./files/test_cascade_configurations.csv"

    # os.system(f"python ../cascade_model.py --costs {costs} --configs {configs}")

    runner = CliRunner()
    result = runner.invoke(cascade_model.create_cascade_models, ["--costs", costs, "--configs", configs])

    # Split all the output and just get the final line to check the command line call worked
    output = [x for x in result.output.split("\n") if x]
    assert output[-1] == 'Total cost of Alginate_cascade is 231.0'

    assert result.exit_code == 0



def test_cost_name_is_null():
    with pytest.raises(ValueError, match='A name in Costs csv does not have a value'):
        cascade_model.load_configurations("./files/test_cascade_costs_name_null.csv",
                                          "./files/test_cascade_configurations.csv")


def test_cost_cost_is_null():
    with pytest.raises(ValueError, match='A cost in Costs csv does not have a value'):
        cascade_model.load_configurations("./files/test_cascade_costs_cost_null.csv",
                                          "./files/test_cascade_configurations.csv")


def test_cost_quantity_is_null():
    with pytest.raises(ValueError, match='A quantity in Costs csv does not have a value'):
        cascade_model.load_configurations("./files/test_cascade_costs_quantity_null.csv",
                                          "./files/test_cascade_configurations.csv")


def test_config_name_is_null():
    with pytest.raises(ValueError, match='A name in Configurations csv does not have a value'):
        cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                          "./files/test_cascade_configs_name_null.csv")


def test_config_component_is_null():
    with pytest.raises(ValueError, match='A component in Configurations csv does not have a value'):
        cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                          "./files/test_cascade_configs_component_null.csv")


def test_config_quantity_is_null():
    with pytest.raises(ValueError, match='A quantity in Configurations csv does not have a value'):
        cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                          "./files/test_cascade_configs_quantity_null.csv")


def test_cost_column_has_non_float():
    with pytest.raises(ValueError, match='All values in Costs csv Costs column should be floats'):
        cascade_model.load_configurations("./files/test_cascade_costs_non_float.csv",
                                          "./files/test_cascade_configurations.csv")


def test_costs_has_incorrect_headers():
    # If the Costs csv doesn't have "Name, Quantity, Cost" as headers, throw an error
    with pytest.raises(ValueError, match='Costs csv should have Name, Quantity, Cost as headers'):
        cascade_model.load_configurations("./files/test_cascade_costs_wrong_headers.csv",
                                          "./files/test_cascade_configurations.csv")


def test_costs_has_correct_headers_case_insensitive():
    # If the Costs csv has "Name, Quantity, Cost" as headers, regardless of case, it should work
    config_list = cascade_model.load_configurations("./files/test_cascade_costs_diff_case_headers.csv",
                                                    "./files/test_cascade_configurations.csv")

    assert (len(config_list) == 2)
    assert (config_list[0].name == 'Small_cascade')
    assert (config_list[1].name == 'Alginate_cascade')
    assert (config_list[0].get_total_cost() == 141)


def test_configs_has_incorrect_headers():
    # If the Configurations csv doesn't have "Name, Component, Quantity" as headers, throw an error
    with pytest.raises(ValueError, match='Configs csv should have Name, Component, Quantity as headers'):
        cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                          "./files/test_cascade_configs_wrong_headers.csv")


def test_configs_has_correct_headers_case_insensitive():
    # If the Configurations csv has "Name, Component, Quantity" as headers, regardless of case, it should work
    config_list = cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                                    "./files/test_cascade_configurations_diff_case_headers.csv")

    assert (len(config_list) == 2)
    assert (config_list[0].name == 'Small_cascade')
    assert (config_list[1].name == 'Alginate_cascade')
    assert (config_list[0].get_total_cost() == 141)


def test_quantities_column__in_configs_has_non_float():
    with pytest.raises(ValueError, match='All values in Configurations csv Quantity column should be floats'):
        cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                          "./files/test_cascade_configs_non_float.csv")


def test_different_case_components_between_costs_and_configs():
    # If there is a different upper / lower case used between configs and costs we should still be able to work it out
    config_list = cascade_model.load_configurations("./files/test_cascade_costs.csv",
                                                    "./files/test_cascade_configs_diff_case_components.csv")

    assert (len(config_list) == 2)
    assert (config_list[0].name == 'Small_cascade')
    assert (config_list[1].name == 'Alginate_cascade')
    assert (config_list[0].get_total_cost() == 141)


def test_duplicate_components_in_costs():
    # If more than one component is defined with the same name in a costs.csv, throw an error

    with pytest.raises(ValueError, match="Costs csv contains non-unique component and quantity value pairs"):
        cascade_model.load_configurations("./files/test_cascade_costs_duplicate_components_same_quantities.csv",
                                          "./files/test_cascade_configurations.csv")


def test_duplicate_components_in_costs_due_to_case():
    # If more than one component has the same name, even with a different case, throw an error
    with pytest.raises(ValueError, match="Costs csv contains non-unique component and quantity value pairs"):
        cascade_model.load_configurations(
            "./files/test_cascade_costs_duplicate_components_same_quantities_diff_case.csv",
            "./files/test_cascade_configurations.csv")


def test_duplicate_components__in_costs_diff_quantities():
    config_list = cascade_model.load_configurations("./files/test_cascade_costs_duplicate_components_diff_quantities.csv",
                                                    "./files/test_cascade_configurations.csv")

    # Check that lengths of list and names are correct
    assert (len(config_list) == 2)
    assert (config_list[0].name == 'Small_cascade')
    assert (config_list[1].name == 'Alginate_cascade')

    small_cascade = config_list[0]

    # Check that total cost of a Configuration is correct
    assert (small_cascade.get_total_cost() == 141)


def test_no_configurations_found():
    # If no cascade configurations are found in a configurations.csv, throw an error
    with pytest.raises(ValueError, match="No configs are present in the Config csv"):
        cascade_model.load_configurations(
            "./files/test_cascade_costs.csv",
            "./files/test_cascade_no_configurations.csv")




