def maxNumberOfEventsCanBeAttended(events):
     minHeap = []
    maxDays = max(i[1] for i in events) # find maximum how many days can this events.
    from heapq import heappush, heappop
    hmap = collections.defaultdict(list)
    for s,e in events: hmap[s].append(e)
    count = 0
    for i in range(1, maxDays + 1):
        if i in hmap: # add events as day progresses to our calender aka minHeap.
            for e in hmap[i]: heappush(minHeap, [e, i]) # adding events
            # remove expired events.
        while minHeap and minHeap[0][0] < i: heappop(minHeap)
        if minHeap: # if there are any active events, attend one of em.
            heappop(minHeap) # attending an event.
            count += 1 
    return count


N = int(input())
eventsStart = []
eventsEnd = []
events = []
for i in range(N):
    eventsStart.append(int(input()))

for i in range(N):
    eventsEnd.append(int(input()))

for i in range(N):
    events.append([eventsStart[i], eventsEnd[i]])

print(maxNumberOfEventsCanBeAttended(events))
