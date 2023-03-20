[![Twitter](https://badgen.net/badge/icon/gabefoley?icon=twitter&label)](https://twitter.com/gabefoley)

# Cascade Model

This is a basic implementation of a tool that lets us define a set of components (enzymes, reagents, flasks) and their cost at specific quantities.

## Documentation

[Read the full documentation here](http://gabefoley.github.io/cascade_model)


## Quickstart

Clone the repository

```
git clone https://github.com/gabefoley/cascade_model
```

Change into the cascade_model directory
```
cd cascade_model
```

Try the example data -

```
python cascade_model.py --costs test/files/test_cascade_costs.csv --configs test/files/test_cascade_configurations.csv
```

Run the program with your own data

```
python cascade_model.py --costs <path_to_costs.csv> --configs <path_to_configs.csv>
```

## Output

The output from running the example data should be -

```
Loading configurations

Printing details of Small_cascade

Component is dhad and it costs $12.0 at a quantity of 10.0
It is priced from a direct reference to this quantity
Component is kari and it costs $4.0 at a quantity of 10.0
It is priced from a direct reference to this quantity
Component is als and it costs $5.0 at a quantity of 10.0
It is priced from a direct reference to this quantity
Component is beaker and it costs $100.0 at a quantity of 20.0
It is priced from a direct reference to this quantity
Component is substrate and it costs $20.0 at a quantity of 30.0
It is priced from a direct reference to this quantity

Total cost of Small_cascade is 141.0

Printing details of Alginate_cascade

Component is dhad and it costs $12.0 at a quantity of 10.0
It is priced from a direct reference to this quantity
Component is kari and it costs $4.0 at a quantity of 10.0
It is priced from a direct reference to this quantity
Component is als and it costs $5.0 at a quantity of 10.0
It is priced from a direct reference to this quantity
Component is beaker and it costs $100.0 at a quantity of 20.0
It is priced from a direct reference to this quantity
Component is substrate and it costs $20.0 at a quantity of 30.0
It is priced from a direct reference to this quantity
Component is alginate beads and it costs $90.0 at a quantity of 10.0
It is priced from a direct reference to this quantity

Total cost of Alginate_cascade is 231.0
```

Please read [the documentation](http://gabefoley.github.io/cascade_model) for more examples and use cases.
