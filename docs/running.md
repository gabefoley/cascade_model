# Running the program

## **Run it on command line**

The entire program can be run directly from the command line

`python cascade_model.py -costs <costs.csv> -configs <configs.csv>`

It will load all of the `Configurations` it finds in the `configs.csv` and print the detailed info (the `Cost` and quantity of each `Component`).

It will then print the total cost of the cascade.

Below is an example output -

```
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

## **Run it as a Python program**

You can also run the Python program from within Python - this allows more control over scaling the configurations.

A worked example is provided in `example.py` that shows how to 

* Access individual configurations directly
* Access the total cost directly
* Automatically scale up configurations and print the new costs
