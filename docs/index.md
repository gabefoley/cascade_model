# Cascade model

This is a basic implementation of a tool that lets us define a set of components (enzymes, reagents, flasks) and their cost at specific quantities.

We can then define a set of configurations of these components. For example, some cascades might use different immobalisation methods or different relative quantities of enzymes.

For each configuration we define we can then

* get the cost of each component, 
* sort these costs by most expensive, 
* get an overall cost for the configuration,
* multiply all quantities by a given factor and re-estimate the cost for the new quantities.

!!! warning 

    Currently this implements a per quantity price for a component and then assumes the quantity you need to use in your configuration dictates the price you buy this at.
    In other words, it assumes that you don't share components across cascades.
    Ideally for each configuration we would want a total quantity used in a single cascade as well as a per quantity price that could be shared across multiple cascades.
    
