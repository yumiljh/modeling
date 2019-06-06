# modeling
数据建模记录

## 匿名打分记录还原模型
> 记录一次数据建模的过程：背景是根据5名评委的匿名打分的加权结果反推出各自打分情况。

> 备注：使用Markdown输入公式的教程：https://oiltang.com/2014/05/04/markdown-and-mathjax/

数据集： $Y = \alpha X$

数据集详细描述： $y_i = \alpha_{ij}x_{ij}, i \in [1,12], j \in [1,5]$



建模：

1、令同一评委的打分方差最小： $f_1(X) = \sum_j^m \sum_i^n \frac{(x_{ij} - \overline {x_j})^2}{n} \rightarrow min, n = 12, m = 5 $

2、令所有评委对同一对象的打分方差最小： $f_2(X) = \sum_i^n \sum_j^m \frac{(x_{ij} - \overline{x_i})^2}{m} \rightarrow min, n = 12, m = 5$

3、加权求最优解： $F(X) = \alpha f_1(X) + \beta f_2(X) \rightarrow min$


