# Randomness
How do we code Randomness ?

## Hardware (Non-Deterministic/True/Physical) RNG
* Generates random numbers from a physical process capable of producing entropy (in other words, the device always has access to a physical entropy source)
* Nature provides ample phenomena that generate low-level, statistically random "noise" signals, including thermal and shot noise, jitter and metastability of electronic circuits, Brownian motion, atmospheric noise, radioactive decay.
  Noise source > analog signals > digitizer > bit stream > conditioner(extractor) > random number
<hr>

## Pseudo (Deterministic) RNG
* Utilizes a deterministic algorithm to generate a sequence of numbers whose properties 
  approximate the properties of sequences of random numbers.
* The PRNG-generated sequence is <b><i>not truly random</i></b>, because it is completely determined by an 
  initial value, called the PRNG's <b><i>seed</i></b> (which may include truly random values).
* Important in practice for their speed in number generation and their reproducibility.

### PRNG Algorithms
### 1. Linear Congruential Generators
   The generator is defined by the recurrence relation:<br>
   <h4>X<sub>n+1</sub> = (aX<sub>n</sub> + c) mod m</h4><br>
        m is "modulus"<br>
        a is "multiplier"<br>
        c is "increment"<br>
        X<sub>0</sub> is "seed" value<br>
   
   [Python Code](lcgrandom.py)

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
    These combinations of values are most suitable for getting long <i>periods</i> (steps before which LCG funtion loops).
    <br>

### 2. xorshift128+

From Javascript's v8 engine official source code:
```C++
static inline void XorShift128(uint64_t* state0, uint64_t* state1) {
    uint64_t s1 = *state0;
    uint64_t s0 = *state1;
    *state0 = s0;
    s1 ^= s1 << 23;
    s1 ^= s1 >> 17;
    s1 ^= s0;
    s1 ^= s0 >> 26;
    *state1 = s1;
  }
```
<hr>

## Random() funtion in progamming languages

1. Javascript
   * Math.Random() implementation depends on engine (browser).
   * v8 uses xorshift128+
2. Python
3. Java
4. C++
