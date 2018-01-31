from simulator import simulator_core as sc


# Simple test of the coin flipper.
def test_flipper():
    total = 0
    prob = 0.333
    count = 10000
    for i in range(0,count):
        total = total + sc.random_event(0.333)

    avg = total / count
    print("test_flipper: result = ", avg,", expectation = ", prob, " flips = ", count)


#test_flipper()

def test_event_string_avg():
    event_stream = sc.random_set(0.333, 10000)
    count = len(event_stream)
    total = 0
    for i in range(0, count):
        total = total + event_stream[i]

    avg = total / count
    print("test_event_string: avg = ", avg, " element count = ", count)


#test_event_string_avg()


def eyeball_event_str():
    event_stream = sc.random_set(0.333,10)
    print("Event stream = ", event_stream)


#eyeball_event_str()

def eyeball_streak_length():
    event_stream = sc.random_set(0.333, 20)
    print("Event stream = ", event_stream)
    fail_streaks = sc.failure_streak_lengths(event_stream)
    print("Hist = ", fail_streaks)


eyeball_streak_length()

def eyeball_histogram():
    event_stream = sc.random_set(0.250, 600)
    print("Event stream = ", event_stream)
    fail_streaks = sc.failure_streak_lengths(event_stream)
    print("Streaks = ", fail_streaks)
    fail_histo = sc.histogram_streak_lengths(fail_streaks)
    print("Histogram = ", fail_histo)

eyeball_histogram()


