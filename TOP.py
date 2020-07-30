# Given an array of numbers , find the top K largest numbers in the array
# [5,1,2,9,1] and K = 3 return [5,2,9]
# complexity of n.lg(n)
array = [5, 1, 2, 9, 1]
k = 3
output = sorted(array)
print('1a. top K elements :', output[len(array)-k:])

# complexity of n*k
# find the max in linear time and iterate K times
array_cpy = array
max_array = []
for i in range(k):
    maxelem = max(array_cpy)
    max_array.append(maxelem)
    array_cpy.remove(maxelem)
print('1b. top K elements :', max_array)


# Rooms required to accomodate meetings
# list = [[start time, end time], ...]
# e.g. meeting_list = [[10.00, 11.00], [11.15, 12.00]]
# assign rooms for every start time, check is an existing room can be released
# before assigning a new room
# Reason for choosing : nlog(N) run time, 2X space

meeting_list = [[10.00, 10.45], [10.15, 10.30], [
    10.30, 11.00], [10.45, 11.00], [10.00, 10.32], [10.32, 11.00], [10.00, 11.05]]
start_times = []
end_times = []
min_rooms = 0

for elem in meeting_list:
    start_times.append(elem[0])
    end_times.append(elem[1])

start_times = sorted(start_times)
end_times = sorted(end_times)

# print(start_times)
# print(end_times)

j = 0
for elem in start_times:

    if(end_times[j] <= elem):
        j = j + 1
    else:
        min_rooms = min_rooms + 1
    # print(min_rooms)
print('2. Minimum rooms required: ', min_rooms)

# Number of tasks and threads
#tasks = [5,1,1,1,3]
#threads = 2
# Note : this is the only working solution i could come up with. Sure there is a smarter way to do it.
# Logic is to greedily assign the largest task to the first thread, and try and fill up others.j
# i feel there could be a better DP solution.

#tasks = [5, 4, 3, 5, 1, 1, 3]
#threads = 3
tasks = [5, 1, 1, 3]
threads = 2
thread_pool = list(range(threads))
tasks = sorted(tasks, reverse=True)

#print('total tasks :', tasks)
total_time = 0

while (len(tasks) > 0):
    #print('total tasks X :', tasks)
    for i in range(threads):
        #print('total tasks :', tasks)
        if(i == 0):
            thread_pool[0] = tasks.pop(0)
            if(len(tasks) == 0):
                break
        else:
            thread_pool[i] = tasks.pop(0)
            if(len(tasks) == 0):
                break
            while(thread_pool[i] < thread_pool[0]):
                if (thread_pool[i] + tasks[-1] > thread_pool[0]):
                    break
                else:
                    thread_pool[i] += tasks.pop()
    total_time += thread_pool[0]

print('3.Total Time:', total_time)
