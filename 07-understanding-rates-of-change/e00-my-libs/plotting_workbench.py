import numpy as np
import matplotlib.pyplot as plt
from my_linear_equations import standard_form_fn, secant_line
import matplotlib.patches as patches

# The most relevant plot related examples and exercises are collected here
# annotated, and explained


## Scenario 1: Single plot, heavily annotated
## + title includes LaTeX!
## + Each curve has a legend
## + axis with labels

fig, ax = plt.subplots()

plt.title(
    'Volume of oil in the tank over time\n'
    r'$ volume(t) = \frac{(t - 4)^3}{64} + 3.3 $', fontsize=16)

# plotting the volume
def volume(t):
    return (t - 4) ** 3 / 64 + 3.3

ts = np.linspace(0, 10, 100)
plt.plot(ts, volume(ts), label='volume over time')

plt.xlabel(r'time (hr)')
plt.ylabel(r'volume (bbl)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 2
## + custom ticks
## + several plots,
## + annotated secants

def v(t):
    return (t - 4) ** 3 / 64 + 3.3

secant_point_start = (4, v(4))
secant_point_end = (9, v(9))

secant_fn = standard_form_fn(secant_point_start, secant_point_end)

fig, ax = plt.subplots()

plt.title(
    'Volume of oil in the tank over time\n'
    r'$ volume(t) = \frac{(t - 4)^3}{64} + 3.3 $'
    '\n and secant line from t=4 and t = 9', fontsize=16)

plt.ylim(0, v(10))
plt.xticks(np.arange(0, 11, step=1))

# plotting the volume
ts = np.linspace(0, 10, 100)
plt.plot(ts, v(ts), label='volume over time')

ts = np.linspace(4, 9, 100)
plt.plot(ts, secant_fn(ts), label='secant line for t=4 and t=9')

# this is just styling
ts = np.linspace(0, 4, 100)
plt.plot(ts, secant_fn(ts), color='orange', linestyle='dashed')
ts = np.linspace(9, 10, 100)
plt.plot(ts, secant_fn(ts), color='orange', linestyle='dashed')
vs = np.linspace(0, v(4))
ts = 4 * np.ones(len(vs))
plt.plot(ts, vs, color='black', linestyle='dashed')
vs = np.linspace(0, v(9))
ts = 9 * np.ones(len(vs))
plt.plot(ts, vs, color='black', linestyle='dashed')


plt.xlabel(r'time (hr)')
plt.ylabel(r'volume (bbl)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 3:
## + Scatter plot

fig, ax = plt.subplots()

plt.title(
    'Volume of oil in the tank over time\n'
    r'$ volume(t) = \frac{(t - 4)^3}{64} + 3.3 $', fontsize=16)

plt.ylim(0, v(10))
plt.xticks(np.arange(0, 11, step=1))

# plotting the volume
ts = np.linspace(0, 10, 100)
plt.plot(ts, v(ts), label='volume over time')

# secant line #1
ts = np.linspace(1, 4, 100)
plt.plot(ts, secant_line(v, 1, 4)(ts), label='secant line from t=2 and t=4', color='orange')
plt.scatter([1, 4], [v(1), v(4)], color='orange')

# secant line #2
ts = np.linspace(6, 9, 100)
plt.plot(ts, secant_line(v, 6, 9)(ts), label='secant line from t=6 and t=9', color='orange')
plt.scatter([6, 9], [v(6), v(9)], color='orange')



plt.xlabel(r'time (hr)')
plt.ylabel(r'volume (bbl)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 4
## + pure scatter plot

def average_flow_rate(v, t1, t2):
    return (v(t2) - v(t1))/(t2 - t1)

def interval_flow_rates(v, t1, t2, dt):
    time_samples = np.arange(t1, t2, dt)
    return [(t, average_flow_rate(v, t, t + dt)) for t in time_samples]

# Plot
fig, ax = plt.subplots()

plt.title(
    'Interval flow rates between t=0 and t=10, interval=1 hour', fontsize=16)

plt.xticks(np.arange(0, 11, step=1))

# plotting the interval flow rate as a scatter plot
series = interval_flow_rates(volume, 0, 10, 1)
times = [t for (t, _) in series]
rates = [r for (_, r) in series]
plt.scatter(times, rates, label='interval flow rate')


plt.xlabel(r'time (hr)')
plt.ylabel(r'average flow rate (bbl/hr)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 5
## + Custom Rectangle on a section of the chart


# Plot
fig, ax = plt.subplots()

plt.title(
    'Volume over time, from t=0 to t=10', fontsize=16)

plt.xticks(np.arange(0, 11, step=1))

# plotting the volume function
ts = np.linspace(0, 10, 100)
plt.plot(ts, volume(ts), label='volume')

rect = patches.Rectangle((0.5, volume(0.5)), 1, .5, edgecolor='b', facecolor='none')
ax.add_patch(rect)

plt.xlabel(r'time (hr)')
plt.ylabel(r'flow rate (bbl/hr)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 6
# + tangent line to show slope... only as a segment

def line_function(t):
    return 0.421875 * t + (2.878125 - 0.421875)

# Plot
fig, ax = plt.subplots()

plt.title(
    'Volume over time, from t=0 to t=10', fontsize=16)

plt.xticks(np.arange(0, 11, step=1))

# plotting the volume function
ts = np.linspace(0, 10, 100)
plt.plot(ts, volume(ts), label='volume')

ts = np.linspace(0, 5, 100)
plt.plot(ts, line_function(ts), label='line with slope 0.421875', color='orange')

plt.scatter(1, volume(1), color='C0')

plt.xlabel(r'time (hr)')
plt.ylabel(r'flow rate (bbl/hr)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 7
## + Step plot

def flow_rate(t):
    return 3*(t-4)**2 / 64

# Plot
fig, ax = plt.subplots()

plt.title(
    'flow rate over time, from t=0 to t=10\n'
    'with scatter plot for flow rate in 1-hour intervals', fontsize=16)

plt.xticks(np.arange(0, 11, step=1))

# plotting the flow_rate function
ts = np.linspace(0, 10, 100)
plt.plot(ts, flow_rate(ts), label='actual flow rate', color='C0')

# plotting the flow_rate values at t=0,1,2,...10
ts = np.arange(0, 11, step=1)
plt.scatter(ts, flow_rate(ts), label='sampled flow rate', color='C0')

# plotting the ladder chart (step plot in stricter terms)
ts = np.arange(0, 11, step=1)
plt.step(ts, flow_rate(ts), label='step flow rate', color='orange', where='post')

plt.xlabel(r'time (hr)')
plt.ylabel(r'flow rate (bbl/hr)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 8
## + shaded rectangles for Riemann sums

# Plot
fig, ax = plt.subplots()

plt.title(
    'flow rate over time, from t=0 to t=10\n'
    'with scatter plot for flow rate in 1-hour intervals', fontsize=16)

plt.xticks(np.arange(0, 11, step=1))

# plotting the flow_rate function
ts = np.linspace(0, 10, 100)
plt.plot(ts, flow_rate(ts), label='actual flow rate', color='C0')

# plotting the flow_rate values at t=0,1,2,...10
ts = np.arange(0, 11, step=1)
plt.scatter(ts, flow_rate(ts), label='sampled flow rate', color='C0')

# plotting the ladder chart (step plot in stricter terms)
ts = np.arange(0, 11, step=1)
plt.step(ts, flow_rate(ts), label='step flow rate', color='orange', where='post')

# plotting the rectangles
ts = np.arange(0, 11, step=1)
plt.bar(ts, flow_rate(ts), 1, align='edge', label='flow rate bars', color='#FFD8B6', edgecolor='orange')

plt.xlabel(r'time (hr)')
plt.ylabel(r'flow rate (bbl/hr)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

## Scenario 9
## + Only a few rectangles for Riemann sums


# These are the functions used to come up with the estimated volume function
def small_volume_change(q, t, dt):
    return q(t) * dt

def volume_change(q, t1, t2, dt):
    return sum(small_volume_change(q, t, dt) for t in np.arange(t1, t2, dt))

def approximate_volume(q, v0, dt, T):
    return v0 + volume_change(q, 0, T, dt)

def approximate_volume_function(q, v0, dt):
    def volume_function(T):
        return approximate_volume(q, v0, dt, T)
    return volume_function
# Plot
fig, ax = plt.subplots()

plt.title(
    'Actual vs. Estimated flow rate over time, from t=0 to t=10\n'
    '(displaying Riemann sums) for 0.5-hour intervals', fontsize=16)

plt.xticks(np.arange(0, 11, step=1))

# plotting the actual volume function
ts = np.linspace(0, 10, 100)
plt.plot(ts, flow_rate(ts), label='actual flow rate', color='C0')

# plotting the volume points at t = 4, t = 8
ts = [4]
plt.scatter(ts, [flow_rate(t) for t in ts], label='estimated instant volume', color='C0')

# plotting the ladder chart (step plot in stricter terms)
ts = np.arange(0, 4, step=0.5)
plt.step(ts, [flow_rate(t) for t in ts], label='step volume', color='orange', where='post')

# plotting the rectangles
ts = np.arange(0, 4, step=0.5)
plt.bar(ts, [flow_rate(t) for t in ts], 0.5, align='edge', label='volume bars', color='#FFD8B6', edgecolor='orange')

plt.xlabel(r'time (hr)')
plt.ylabel(r'volume (bbl)')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()