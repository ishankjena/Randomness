# Randomness
How do we code Randomness ?

## Hardware random number generator
* hardware/true/non-deterministic/physical random number generator
* generates random numbers from a physical process capable of producing entropy (in other words, the device always has access to a physical entropy source)
* Nature provides ample phenomena that generate low-level, statistically random "noise" signals, including thermal and shot noise, jitter and metastability of electronic circuits, Brownian motion, atmospheric noise.

  Noise source > analog signals > digitizer > bit stream > conditioner(extractor) > random number


## Pseudo Random Number Generator
* Also called Deterministic random numer generator
* utilizes a deterministic algorithm to generate a sequence of numbers whose properties 
  approximate the properties of sequences of random numbers.
* The PRNG-generated sequence is not truly random, because it is completely determined by an 
  initial value, called the PRNG's seed (which may include truly random values).
* important in practice for their speed in number generation and their reproducibility.

### Linear Congruential Generators
* simple approach to generate pseudo random numbers.
* The generator is defined by the recurrence relation:<br>
  <p align="center">
  <strong>X<sub>n+1</sub> = (aX<sub>n</sub> + c) mod m</strong><br>
        m is "modulus"<br>
        a is "multiplier"<br>
        c is "increment"<br>
        X<sub>0</sub> is "seed" value<br>
  </p>
* [Code]()

<table>
  <th>Implementation </th>
  <th>modulus: m</th>
  <th>increment: c</th>
  <th>multiplier: a</th>
  <tr>
    <td>C++ 11's minstd_rand</td>
    <td>2<sup>31</sup>-1</td>
    <td>48271</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Java's java.util.Random</td>
    <td>2<sup>48</sup></td>
    <td>25214903917</td>
    <td>11</td>
  </tr>
</table>
