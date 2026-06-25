# Interpolation
## Sample Output

### Search Example

```text
Array: [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
Searching for: 35
Found at index: 5
Comparisons: 3
```

### Performance Comparison with Binary Search

```text
      Size    IS Time(ms)    BS Time(ms)   IS Comparisons   BS Comparisons
---------------------------------------------------------------------------
      1000         0.0084         0.0066                4                9
      5000         0.0088         0.0044                6                7
     10000         0.0091         0.0045                4                6
     50000         0.0088         0.0074                2               15
    100000         0.0121         0.0086                5               17
```

### Observation

- Interpolation Search required fewer comparisons than Binary Search for larger datasets.
- Binary Search showed slightly lower execution time in some cases due to lower computational overhead.
- Interpolation Search performs best when the data is sorted and uniformly distributed.
- As the dataset size increases, the number of comparisons made by Interpolation Search remains significantly lower than Binary Search.

### Conclusion

The experimental results demonstrate that Interpolation Search can outperform Binary Search in terms of comparison count when data is uniformly distributed. This makes it a suitable choice for large sorted datasets where reducing search operations is important.
