Take some time after you have played with the code above to reflect on these questions:

What happens when Kp is large?
What happens when Kp is small?
Do we reach our desired goal?
How does control effort vary with different Kp values?
How does the steady state offset and overshoot vary with different Kp values?

1. the overshoot is larger, and the oscillation frequency is higher, and it will take longer time to settle
2. the overshoot is smaller, and the oscillation frequency is lower, and it will settle sooner. When it's small enough it even might not reach the setpoint.
3. yes
4. positively related
5. overshoot with kp: positively related; ss offset: not directly related?

```
Take some time after you have played with the code above to reflect on these questions:

What happens when Ki is large?
What happens when Ki is small?
Do we reach our desired goal?
How does control effort vary with different Ki values?
How does the steady state offset and overshoot vary with different Ki values?

1. the oscillation is larger and settling time is longer
2. oscillation is smaller and settling time is shorter, but may not reach the setpoint
3. yes
4. the oscillation for u_i will be larger with larger Ki; if Ki is very small then u_i may appear​ to be linear
5. overshoot becomes larger with larger Ki, but doesn't change too much; the larger Ki, the smaller ss error

```
Take some time after you have played with the code above to reflect on these questions:

What happens when Kd is large?
What happens when Kd is small?
Do we reach our desired goal?
How does control effort vary with different Kd values?
How does the overshoot vary with different Kd values?

1. there was nearly no settling/oscillations if Kd is large enough
2. there were oscillations and if Kd is small enough, the setpoint may never be reached.
3. no, there was some constant steady state error
4. positively related
5. negatively related

```
Take some time after you have played with the code above to reflect on these questions:

Is this better than PD control?
How do the parameters work together?
Do we reach our desired goal?
How does control effort look?

1. Yes
2. Kp sets the overshoot; Ki adjusts the sse; Kd helps with reduction of the overshoot and oscillations
3. Yes
4. almost like a 90 degree angle
