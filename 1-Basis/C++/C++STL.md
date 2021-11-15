# C++ STL

[TOC]

## STL 组成

- 容器（containers）
- 算法（algorithms）
- 迭代器（iterators）
- 仿函数（functors）
- 配接器（adapters）
- 空间配置器（allocator）

## 容器（containers）

***Sequence containers*** 顺序容器： array [数组]、vector [数组]、deque [双端队列]、fordward_list [单链表]、list [双链表]

**Associative containers** 关联容器：set、map、multiset、multimap / 底层红黑树

**Unordered associative containers** 无序关联容器：unordered_set、unordered_map、unordered_multiset、unordered_multimap /底层哈希表

***Container adaptors*** 容器适配器：stack [ 底层 deque/list]、queue [ 底层 deque/list]、priority_queue [底层 vector + max-heap ]

**底层实现**

| **容器**                                                     | **底层数据结构**  | **时间复杂度**                                            | **有无序** | **可不可重复** | **其他**                                                     |
| ------------------------------------------------------------ | ----------------- | --------------------------------------------------------- | ---------- | -------------- | ------------------------------------------------------------ |
| [array](https://github.com/huihut/interview/tree/master/STL#array) | 数组              | 随机读改 O(1)                                             | 无序       | 可重复         | 支持随机访问                                                 |
| [vector](https://github.com/huihut/interview/tree/master/STL#vector) | 数组              | 随机读改、尾部插入、尾部删除 O(1) 头部插入、头部删除 O(n) | 无序       | 可重复         | 支持随机访问                                                 |
| [deque](https://github.com/huihut/interview/tree/master/STL#deque) | 双端队列          | 头尾插入、头尾删除 O(1)                                   | 无序       | 可重复         | 一个中央控制器 + 多个缓冲区，支持首尾快速增删，支持随机访问  |
| [forward_list](https://github.com/huihut/interview/tree/master/STL#forward_list) | 单向链表          | 插入、删除 O(1)                                           | 无序       | 可重复         | 不支持随机访问                                               |
| [list](https://github.com/huihut/interview/tree/master/STL#list) | 双向链表          | 插入、删除 O(1)                                           | 无序       | 可重复         | 不支持随机访问                                               |
| [stack](https://github.com/huihut/interview/tree/master/STL#stack) | deque / list      | 顶部插入、顶部删除 O(1)                                   | 无序       | 可重复         | deque 或 list 封闭头端开口，不用 vector 的原因应该是容量大小有限制，扩容耗时 |
| [queue](https://github.com/huihut/interview/tree/master/STL#queue) | deque / list      | 尾部插入、头部删除 O(1)                                   | 无序       | 可重复         | deque 或 list 封闭头端开口，不用 vector 的原因应该是容量大小有限制，扩容耗时 |
| [priority_queue](https://github.com/huihut/interview/tree/master/STL#priority_queue) | vector + max-heap | 插入、删除 O(log2n)                                       | 有序       | 可重复         | vector容器+heap处理规则                                      |
| [set](https://github.com/huihut/interview/tree/master/STL#set) | 红黑树            | 插入、删除、查找 O(log2n)                                 | 有序       | 不可重复       |                                                              |
| [multiset](https://github.com/huihut/interview/tree/master/STL#multiset) | 红黑树            | 插入、删除、查找 O(log2n)                                 | 有序       | 可重复         |                                                              |
| [map](https://github.com/huihut/interview/tree/master/STL#map) | 红黑树            | 插入、删除、查找 O(log2n)                                 | 有序       | 不可重复       |                                                              |
| [multimap](https://github.com/huihut/interview/tree/master/STL#multimap) | 红黑树            | 插入、删除、查找 O(log2n)                                 | 有序       | 可重复         |                                                              |
| [unordered_set](https://github.com/huihut/interview/tree/master/STL#unordered_set) | 哈希表            | 插入、删除、查找 O(1) 最差 O(n)                           | 无序       | 不可重复       |                                                              |
| [unordered_multiset](https://github.com/huihut/interview/tree/master/STL#unordered_multiset) | 哈希表            | 插入、删除、查找 O(1) 最差 O(n)                           | 无序       | 可重复         |                                                              |
| [unordered_map](https://github.com/huihut/interview/tree/master/STL#unordered_map) | 哈希表            | 插入、删除、查找 O(1) 最差 O(n)                           | 无序       | 不可重复       |                                                              |
| [unordered_multimap](https://github.com/huihut/interview/tree/master/STL#unordered_multimap) | 哈希表            | 插入、删除、查找 O(1) 最差 O(n)                           | 无序       | 可重复         |                                                              |

## 算法（algorithms）







