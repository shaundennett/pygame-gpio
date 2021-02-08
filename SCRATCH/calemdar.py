

cal_1 = [(10,11)]
cal_2 = [(9,10),(12,14)]

restricted = [(1,8),(12,13),(19,23)]

all = [cal_1, cal_2, restricted]
#create timeslots

all_ts = []
ts_1 = []

for cal in all:
    for start, end  in cal:
        print(f" {start} : {end}")
        #work out the timeslots
        for slot in range(start,end + 1):
            ts_1.append(slot)
    print("hello")
    all_ts.append(ts_1)
    ts_1 = []

slots = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23}

set_1 = set(all_ts[0] + all_ts[1] + all_ts[2])

#all_used_slots = set(all_ts[0]).union(set(all_ts[1])) some more text 
print("--------------------------")
print(set_1)
print(slots.symmetric_difference(set_1))
print("--------------------------")




