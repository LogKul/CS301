import time

LIST_LENGTHS = [100, 10000, 1000000, 100000000, 10000000000]
INTERVAL = 10

def test_runtime(f, arg, lengths, intvl, f_out):
    avg_runtime = 0

    for i in range(intvl):
        start_time = time.time()
        f(arg)
        end_time = time.time()
        avg_runtime += (end_time - start_time)
    avg_runtime = avg_runtime / intvl
    f_out.write(str(avg_runtime) + ",")

f_out = open("lmao.csv", "w+")

# --CODE BELOW--


# --CLOSE FILE
f_out.close()