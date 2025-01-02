import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def parse_file():
    with open(f"{__file__.split('.')[0]}.txt") as f:
        l = f.readlines()
        a = int(l[0].strip().split(":")[-1])
        b = int(l[1].strip().split(":")[-1])
        c = int(l[2].strip().split(":")[-1])
        codes = list(map(int, l[-1].strip().split(":")[-1].split(",")))
    return (a, b, c, codes)

def combo(x, registers):
    if x == 4:
        x = registers[0]
    elif x == 5:
        x = registers[1]
    elif x == 6:
        x = registers[2]
    else:
        x = x
    return x

def adv(x, registers):
    x = combo(x,registers)
    registers[0] = registers[0]//(2**x)

def bxl(x, registers):
    registers[1] = registers[1]^x

def bst(x, registers):
    registers[1] = combo(x, registers) % 8

def jnz(y, registers):
    if registers[0] == 0:
        return 
    else:
        registers[3] = y

def bxc(registers):
    registers[1] = registers[1] ^ registers[2]
    
def out(x, registers):
    x = combo(x, registers)
    return x%8

def bdv(x, registers):
    x = combo(x, registers)
    registers[1] = registers[0]//(2**x)

def cdv(x, registers):
    x = combo(x, registers)
    registers[2] = registers[0]//(2**x)

def func(x, y, registers):
    ret = -1
    if x == 0:
        adv(y, registers)
    elif x == 1:
        bxl(y, registers)
    elif x == 2:
        bst(y, registers)
    elif x == 3:
        jnz(y, registers)
    elif x == 4:
        bxc(registers)
    elif x == 5:
        ret = out(y, registers)
    elif x == 6:
        bdv(y, registers)
    else:
        cdv(y, registers)
    
    if x == 3 and registers[0] != 0:
        pass
    else:
        registers[3] += 2
    return ret

def solve_1():
    A, B, C, codes = parse_file()
    registers = [A, B, C, 0]
    outputs = []
    while registers[3] < len(codes):
        x = codes[registers[3]]
        y = codes[registers[3]+1]
        func(x, y, registers, outputs)
        print(registers, x)
    return outputs

def solve_2():
    codes = parse_file()[-1]
    flag = True
    a = 0
    def f(a, ans):
        print(a)
        registers = [a, 0, 0, 0]
        ind = 0
        while registers[3] < len(codes):
            x = codes[registers[3]]
            y = codes[registers[3] + 1]
            ret = func(x, y, registers)
            if ret != -1:
                if ret == codes[ind]:
                    ind += 1
                else:
                    return
            a += 1
        if ind == len(codes):
            ans.add(a)
            return a
    
    ans = set()
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=10000) as executor:
        # Create a list of future tasks
        futures = []
        while flag:
            # Divide the range into smaller batches
            ranges = [(a + i, a + i + 100000) for i in range(0, 10000000, 100000)]

            # Submit tasks for each batch
            for r in ranges:
                future = executor.submit(lambda r=r: [f(x, ans) for x in range(r[0], r[1])])
                futures.append(future)
            
            # Check results as they complete
            for future in as_completed(futures):
                if ans:  # Exit early if condition is met
                    flag = False
                    break

            # Update `a` for the next range
            a += 10000000

        print("Execution time:", time.time() - start_time)
    return min(ans) if ans else None

import asyncio
codes = parse_file()[-1]

import asyncio
import time

async def f_async(a, ans):
    registers = [a, 0, 0, 0]
    ind = 0
    while registers[3] < len(codes):
        x = codes[registers[3]]
        y = codes[registers[3] + 1]
        ret = func(x, y, registers)
        if ret != -1:
            if ret == codes[ind]:
                ind += 1
            else:
                return
        a += 1
    print(a)  # You may want to remove or log this for large ranges
    if ind == len(codes):
        ans.add(a)
        return a

async def solve_2_async():
    codes = parse_file()[-1]
    ans = set()
    a = 0
    flag = True
    start_time = time.time()

    # Using asyncio.create_task to submit concurrent tasks
    tasks = []
    while flag:
        # Divide the range into smaller batches
        ranges = [(a + i, min(a + i + 1000000, 10**10)) for i in range(0, 10**10, 1000000)]  # Adjust chunk size

        for r in ranges:
            # Creating a task for each batch of range
            tasks.append(asyncio.create_task(run_range(r, ans)))

        # Wait for any task to complete
        for task in asyncio.as_completed(tasks):
            await task
            if ans:
                flag = False
                break

        # Update `a` for the next range
        a += 1000000

    print("Execution time:", time.time() - start_time)
    return min(ans) if ans else None

async def run_range(r, ans):
    for x in range(r[0], r[1]):
        await f_async(x, ans)

# To run the async function
asyncio.run(solve_2_async())
