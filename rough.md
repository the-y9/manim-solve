$$
\begin{array}{c}
\text{QUESTION:}\\\\
\lim_{n \to \infty} \sum_{k=1}^{n} \dfrac{k^3 + 6k^2 + 11k + 5}{(k+3)!}
\end{array}
$$

$$
\lim_{n \to \infty} \sum_{k=1}^{n} \dfrac{k^3 + 6k^2 + 11k + 6 -1}{(k+3)!}
$$

$$
\lim_{n \to \infty} \sum_{k=1}^{n} \dfrac{(k+1)(k+2)(k+3)-1}{(k+3)!}
$$
$$
\lim_{n \to \infty} \sum_{k=1}^{n} \left( \dfrac{(k+1)(k+2)(k+3)}{(k+3)(k+2)(k+1)k!} -  \dfrac{1}{(k+3)!} \right)
$$

$$
\lim_{n \to \infty} \sum_{k=1}^{n} \left( \dfrac{1}{k!} -  \dfrac{1}{(k+3)!} \right)
$$

$$
\text{Expanding the sum:} \sum_{k=1}^{n} 
$$
$$
\lim_{n \to \infty} \left( 
\left( \dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \dfrac{1}{4!} + \cdots +  \dfrac{1}{n!} \right) - \left( \dfrac{1}{(1+3)!} + \dfrac{1}{(2+3)!} + \cdots + \dfrac{1}{(n+3)!} \right) 
\right)
$$
$$
\lim_{n \to \infty} \left( 
\left( \dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \dfrac{1}{4!} + \cdots +  \dfrac{1}{n!} \right) - \left( \dfrac{1}{4!} + \dfrac{1}{5!} + \cdots + \frac{1}{n!} + \cdots + \dfrac{1}{(n+3)!} \right) 
\right)
$$
$$
\lim_{n \to \infty} \left( 
\left( \dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} \right) - \left( \frac{1}{(n+1)!} + \frac{1}{(n+2)!} + \dfrac{1}{(n+3)!} \right) 
\right)
$$
$$
\text{As } n \to \infty, \left( \frac{1}{(n+1)!} + \frac{1}{(n+2)!} + \dfrac{1}{(n+3)!} \right) \to 0, \text{ so, we have:} 
$$
$$
\dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} = 1 + \dfrac{1}{2} + \dfrac{1}{6} = \dfrac{10}{6}
$$
$$
= \dfrac{5}{3}
$$