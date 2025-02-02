# Advanced Computational Theory Course

## Project: Universal Program

### Overview

This project explores the concept of a universal program, which can simulate any other program given the correct input. The focus is on understanding the mechanics of computation and the universality of certain computational models.

### Decoder Program Input Test

**Input:**
```
21 46
```

**Output:**
```
[A1] X1 <- X1 + 1
IF X1 != 0 GOTO A1
```

### Universal Program Input Test

**Input:**
```
45 34 350 2 46
2 1
```

**Output:**
```
1 2 1 0 0 0 0 
2 1 1 0 0 0 0 
3 1 1 0 0 1 0 
4 1 1 0 0 1 0 
5 1 1 0 0 1 1 
1 1 1 0 0 1 1 
2 0 1 0 0 1 1 
3 0 1 0 0 2 1 
4 0 1 0 0 2 1 
5 0 1 0 0 2 2 
```


### Additional Resources

- **Textbook:** "Computability complexity and languages fundamentals of theoretical computer science" by Martin D. Davis

These resources can provide further insights into the theoretical underpinnings of universal computation and help deepen your understanding of the concepts covered in this project.
