# Prime clock

Just a little project for me to learn [manim](https://github.com/ManimCommunity/manim). It is a visualization of an algorithm that computes prime factorization of consecutive integers.

The algorithm keeps track of the current number written in different bases. The multiplicity of the prime p in the prime factorization of n is exactly the number of trailing zeros in the base-p expansion of n. Furthermore, a number n can have at most one prime factor that is larger than the square root of n. So if we find all prime factors of n that are at most the square root of n, we can find the last prime factor (if there is any) by dividing n by all prime factors we have found.

The case shown in the animation is where we keep track of the base-p expansion of n for all primes up to 31. The smallest number that is not prime and does not have a factor of at most 31 is 37^2 = 1369. Thus, the animation shows prime factorization up to 1368.
