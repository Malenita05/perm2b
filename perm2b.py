import time

x = []

for i in range(10000000):
    x.append(i)

def bubble_s(lst):
    inicio = time.time()
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    fin = time.time()
    return  fin - inicio

#print(f"BubbleSort: {bubble_s(x):.10f}")
#print("----------------------------------------------------")

def insertion_s(lsta):
    inicio = time.time()
    for i in range(1, len(lsta)):
        j = i
        while j > 0 and lsta[j] < lsta[j-1]:
            lsta[j], lsta[j-1] = lsta[j-1], lsta[j]
            j -= 1
    fin = time.time()
    return fin - inicio

print(f"insertionSort: {insertion_s(x):.10f}")
print("----------------------------------------------------")
