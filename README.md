# Hopfield-Model
Utilizes the three kinds of updates for the Hopfield model: synchronous, asynchronous ordered, and asynchronous random. The program plots the Energy as a function of iteration.

The program takes in 3 command-line arguments:

1) The type of update <br/>
  </t>a) Synchronous (```synch```) - all your X values are updated every iteration <br/>
  </t>b) Asynchronous random (```asynchrand```) - A random X value is chosen to be updated every iteration <br/> 
  </t>c) Asynchronous order (```asynchorder```) - An X value is updated if the previous X value was updated the previous iteration ((iteration) % (dimension of X vector)) gives the index to be updated this iteration, if we say that the iterations start at 0) <br/>
2) The amount of inputs/dimension of weight matrix
3) Symmettry of weight matrix (`1` if it should be symmetric, `0` if values should be chosen randomly)

E.g. 

```python3 hopfield.py asynchorder 2 0``` uses asynchronous order update, an input vector of size 2, and a weight matrix with randomly picked values <br/>
```python3 hopfield.py synch 3 1``` uses synchronous update, an input vector of size 3, and a symmetric weight matrix.

