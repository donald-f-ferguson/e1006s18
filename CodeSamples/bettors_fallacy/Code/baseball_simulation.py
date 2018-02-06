from simulator import simulator_core as sc
import matplotlib.pyplot as plt

def simulate_season(avg, games):
    event_stream = sc.random_set(avg, games)
    return event_stream

def hitless_streak_lengths(season):
    result = sc.failure_streak_lengths(season)
    return result

def streak_histogram(streaks):
    result = sc.histogram_streak_lengths(streaks)
    return result;


def combine_histograms(x,y):
    result = []

    x_len = len(x)
    y_len = len(y)
    max_len = max(x_len, y_len)

    for i in range(0,max_len):
        if i >=  x_len:
            x.append(0)
        if i >= y_len:
            y.append(0)
        to_add = x[i] + y[i]
        result.append(to_add)

    return result

'''
h1 = simulate_season(0.333, 30)
s1 = hitless_streak_lengths(h1)
g1 = streak_histogram(s1)

print("Season = ", h1)
print("Streaks = ", s1)

h2 = simulate_season(0.333, 30)
s2 = hitless_streak_lengths(h2)
g2 = streak_histogram(s2)

print("Season = ", h2)
print("Streaks = ", s2)

print("Histo1 = ",g1)
print("Histo2 = ", g2)

t = combine_histograms(g1,g2)
print("Combined = ",t)
'''

n = 10000
ab = 600
avg = 0.333
result = []

for i in range(0,n):
    h1 = simulate_season(0.250,600)
    s1 = hitless_streak_lengths(h1)
    g1 = streak_histogram(s1)
    result = combine_histograms(result,g1)

for j in range(0,len(result)):
    result[j]=result[j]/n

print("Final histogram = ", result)




def add_to_plot(x, y):
    result = False
    if (isinstance(x, int) or isinstance(x, float)) and \
            (isinstance(y, int) or isinstance(y, float)):
        plt.plot(x, y, "ro")
        result = True

    return result


for i in range(15, len(result)):
    add_to_plot(i, result[i])

plt.title("No of streaks.")
plt.xlabel("Streak length")
plt.ylabel("No. of streaks of length")
plt.show()