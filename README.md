[![Twitter](https://badgen.net/badge/icon/gabefoley?icon=twitter&label)](https://twitter.com/gabefoley)

# Cascade Model

This is a basic implementation of a tool that lets us define a set of components (enzymes, reagents, flasks) and their cost at specific quantities.

## Documentation

Read the full documentation here - 
http://gabefoley.github.io/cascade_model


## Quickstart

Clone the repository

```
git clone https://github.com/gabefoley/cascade_model
```

Change into the cascade_model directory
```
cd cascade_model
```

Run the program

```
python cascade_model.py --costs <path_to_costs.csv> --configs <path_to_configs.csv>
```

Try the example data -

```
python cascade_model.py --costs test/files/test_cascade_costs.csv --configs test/files/test_cascade_configuration.csv
```
