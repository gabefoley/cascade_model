# Inputs and outputs

## **Basic inputs**

**There are three important concepts -**

**`Components`**

A reagent, enzyme, flask, etc... Any object that can be used in a cascade and can have a quantity and a cost.

**`Costs`**

How much something costs for a given quantity

**`Configurations`**

A set of different combinations of Components, that can have different individual quantities and therefore different individual Costs

**There are two spreadsheets that must be supplied -**

**`Costs spreadsheet`**

Contains a list of all the `Components` and their `Costs` at a specific quantity
There can be multiple identical `Components` as long as they have different quantities.

Here is an example `Costs spreadsheet`. Note that there are multiple unit prices for Substrate.


|    | Name           |   Quantity |   Cost |
|---:|:---------------|-----------:|-------:|
|  0 | DHAD           |         10 |     12 |
|  1 | KARI           |         10 |      4 |
|  2 | ALS            |         10 |      5 |
|  3 | Beaker         |         20 |    100 |
|  4 | Substrate      |         30 |     20 |
|  5 | Substrate      |        250 |     14 |
|  6 | Alginate beads |         10 |     90 |


**`Configurations spreadsheet`**

Contains all of the `Configurations` that lists the name and quantity of each `Component`.
There can be multiple `Configurations` within the one spreadsheet (with different `Components` and/or quantities of `Componenets`)



Here is an example `Configurations spreadsheet`


|    | **Name**             | **Component**      |   **Quantity** |
|---:|:-----------------|:---------------|-----------:|
|  0 | Small_cascade    | DHAD           |         10 |
|  1 | Small_cascade    | KARI           |         10 |
|  2 | Small_cascade    | ALS            |         10 |
|  3 | Small_cascade    | Beaker         |         20 |
|  4 | Small_cascade    | Substrate      |         30 |
|  5 |               |             |         |
|  6 |               |             |         |
|  7 | Alginate_cascade | DHAD           |         10 |
|  8 | Alginate_cascade | KARI           |         10 |
|  9 | Alginate_cascade | ALS            |         10 |
| 10 | Alginate_cascade | Beaker         |         20 |
| 11 | Alginate_cascade | Substrate      |         30 |
| 12 | Alginate_cascade | Alginate beads |         10 |



## **Basic outputs**

The basic workflow is to -

* Take all the `Configurations` listed in a `Configurations spreadsheet`
* Estimate the `Cost` based on the unit price contained within the `Costs` spreadsheet for each `Component`
* `Costs` are either derived directly from the unit price or from the closest unit price to the desired quantity
* Now we can get the individual costs of each `Component` within each `Configuration`
* We can also get the total cost of a `Configuration`
* We can also scale the quantities in a `Configuration` by a certain factor and re-estimate the costs - see 
