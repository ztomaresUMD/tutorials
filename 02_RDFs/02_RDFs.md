# Advanced Techniques: ROOT DataFrames

In this tutorial, you will learn how to use ROOT DataFrames to speed up your analysis code.

# ROOT DataFrames

As we talked about in the previous tutorial, our data is organized in separate events. We loop over these events, as we need to analyze each one individually, and then aggregate the results.

From a computing point of view, this is a achieved using `for` loops over the events. While being easy to write and understand, writing `for` loops in `PyROOT` is not a very efficient way to process the large datasets that we have to work with in this field.

Instead, we can use ROOT DataFrames (RDFs), which are highly optimized frameworks to manipulate our data. The key point here is that you define actions that are applied on the whole data at once; for example, if you apply a selection, it will be performed on all events in the DataFrame. This type of columnar operation is a lot quicker computationally. (Don't be afraid, these are just `for` loops under the hood! They are just more efficient than the `for` loops in `PyROOT`, and take care of some parallelization for you, allowing for things to scale seamlessly, but more on that later.)

Here is a simple comparison of the two methods:

```python
# simple for loop
for event in events:
    for particle in event.particles:
        if particle.pt > 10:
            hist.fill(particle.pt)
```

```python
# RDF
df = df.Filter("particles.pt > 10")
df.Histo1D("particles.pt")
```

ROOT's [docs](https://root.cern/doc/master/classROOT_1_1RDataFrame.html) provide good documentation, tutorials, and a crash course on RDFs, check them out!

> *Exercise*: Write the same analysis to extract the invariant mass of the dimuon system using RDFs. The result should be exactly the same! Try running over more events, and note the speed between the simple `for` loop and RDFs.