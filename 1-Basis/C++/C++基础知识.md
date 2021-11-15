# C++函数

## 构造函数和析构函数的初始化顺序

> 本回答参考[C++ 构造函数初始化顺序](https://blog.csdn.net/qq_30835655/article/details/66971183), [C++奇奇怪怪的题目之构造析构顺序](http://gaocegege.com/Blog/cpp/cppclass)

有**多个基类的派生类(多继承)** 的构造函数初始化按照如下顺序进行：

1. 先执行虚拟继承的父类的构造函数;
2. 然后从左到右执行普通继承的父类的构造函数;
3. 接着按照定义的顺序执行数据成员的初始化;
4. 最后调用类自身的构造函数；

析构函数就无脑的将构造函数顺序反转即可。多继承形式下的构造函数和单继承形式基本相同，只是要在派生类的构造函数中调用多个基类的构造函数。

实例代码如下：

```c++
#include <iostream>
 
using namespace std;
 
class OBJ1
{
public:
    OBJ1() { cout << "OBJ1" << endl; }
    ~OBJ1() { cout << "OBJ1 destory" << endl;}
};
 
class OBJ2
{
public:
    OBJ2() { cout << "OBJ2\n"; }
    ~OBJ2(){cout << "OBJ2 destory" <<endl;}
};
 
class Base1
{
public:
    Base1() { cout << "Base1" << endl; }
    ~Base1() { cout << "Base1 destory" << endl; }
};
 
class Base2
{
public:
    Base2() { cout << "Base2" << endl; }
    ~Base2() { cout << "Base2 destory" << endl; }
};
 
class Base3
{
public:
    Base3() { cout << "Base3" << endl; }
    ~Base3() { cout << "Base3 destory" << endl; }
};
 
class Base4
{
public:
    Base4() { cout << "Base4" << endl; }
    ~Base4() { cout << "Base4 destory" << endl; }
};
 
class Derived :public Base1, virtual public Base2,
    public Base3, virtual public Base4
{
public:
    Derived() { cout << "Derived ok" << endl; }
    ~Derived() { cout << "Derived destory" << endl; }
protected:
    OBJ1 obj1;
    OBJ2 obj2;
};
 
int main()
{
    Derived aa;
    cout << "construct ok"<<endl;
    return 0;
}
```

程序输出结果如下：

> Base2
> Base4
> Base1
> Base3
> OBJ1
> OBJ2
> Derived ok
> construct ok
> Derived destory
> OBJ2 destory*
> OBJ1 destory
> Base3 destory
> Base1 destory
> Base4 destory
> Base2 destory



