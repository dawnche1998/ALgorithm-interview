[TOC]



### C++ 11 匿名函数

[C++11](https://en.wikipedia.org/wiki/C%2B%2B11) supports anonymous functions, called *lambda expressions*, which have the form:

```C++
[capture](parameters) -> return_type { function_body }
```

This is an example lambda expression:

```C++
[](int x, int y) { return x + y; }
```

C++11 also supports [closures](https://en.wikipedia.org/wiki/Closure_(computer_science)), here called captures. Captures are defined between square brackets `[`and `]` in the declaration of lambda expression. The mechanism allows these variables to be captured by value or by reference. The following table demonstrates this:

**通过值域或者引用来'捕获'**

```C++
[]        // No captures, the lambda is implicitly convertible to a function pointer.
[x, &y]   // x is captured by value and y is captured by reference.
[&]       // Any external variable is implicitly captured by reference if used
[=]       // Any external variable is implicitly captured by value if used.
[&, x]    // x is captured by value. Other variables will be captured by reference.
[=, &z]   //z is captured by reference. Other variables will be captured by value.
```

from [C++ (since C++11) ](https://en.wikipedia.org/wiki/Anonymous_function#C++_(since_C++11))

