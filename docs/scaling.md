# Estimating and scaling

## **Estimating costs**

Prices for increased quantities do not scale linearly. To deal with this, the `Costs spreadsheet` can take any number of quantity / cost pairs. This makes adding more detail to the `Costs spreadsheet` straightforward and improves the estimations.

When a `Component` from the `Configurations spreadsheet` is crosschecked against the `Costs spreadsheet` - a simple check is performed to find the quantity that is the closest to what is wanted. Then this quantity / cost pair is that one that is used to provide a price point for the desired `Component`.


## **Scaling cascades**

Once a `Configuration` is loaded in, all of its quantities can be scaled by a factor, and the new `Costs` will be worked out again in reference to the `Costs spreadsheet`.

So, if by scaling the quantity, a more appropriate pair of quantity / cost values from the `Costs spreadsheet` should be used - this will be reflected in the updated, scaled cost.

```
small_cascade.print_detailed_info()
```

```
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

Total cost of Small_cascade is $141.0 
```

```
small_cascade.print_detailed_info(scale=10)
```

```
Component is dhad and it costs $120.0 at a quantity of 100.0
It is priced from an estimation based on a quantity of 10.0 at a cost of $12.0
Component is kari and it costs $40.0 at a quantity of 100.0
It is priced from an estimation based on a quantity of 10.0 at a cost of $4.0
Component is als and it costs $50.0 at a quantity of 100.0
It is priced from an estimation based on a quantity of 10.0 at a cost of $5.0
Component is beaker and it costs $1000.0 at a quantity of 200.0
It is priced from an estimation based on a quantity of 20.0 at a cost of $100.0
Component is substrate and it costs $16.8 at a quantity of 300.0
It is priced from an estimation based on a quantity of 250.0 at a cost of $14.0

Total cost of Small_cascade is $1226.8
```


## **Recalculation of cost after scaling**

Note that we have two price points for Substrate.

Costs spreadsheet

|    | Name           |   Quantity |   Cost |
|---:|:---------------|-----------:|-------:|
|  4 | Substrate      |         30 |     20 |
|  5 | Substrate      |        250 |     14 |

Configuration spreadsheet

|    | **Name**             | **Component**      |   **Quantity** |
|---:|:-----------------|:---------------|-----------:|
|  4 | Small_cascade    | Substrate      |         30 |

Before scaling, it is priced at the first quantity / cost pair

```
Component is substrate and it costs $20.0 at a quantity of 30.0
It is priced from a direct reference to this quantity
```

After scaling, it is priced at the second quantity / cost pair

```
Component is substrate and it costs $16.8 at a quantity of 300.0
It is priced from an estimation based on a quantity of 250.0 at a cost of $14.0
```