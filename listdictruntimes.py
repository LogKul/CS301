import time

LIST_LENGTHS = [100, 10000, 1000000, 100000000, 10000000000]
INTERVAL = 10


def test_runtime(f, arg, lengths, intvl, f_out):

    for list_length in lengths:
        # --Generate list--
        n_length_list = [1] * list_length

        # --Run function intvl times and take average--
        avg_runtime = 0
        for i in range(intvl):
            start_time = time.time()
            f(arg, list_length)
            end_time = time.time()
            avg_runtime += (end_time - start_time)
        avg_runtime = avg_runtime / intvl

        # --Write average runtime given specific list length--
        f_out.write(str(avg_runtime) + ",")

    # --Make sure to add newline after all relevant info is added to csv file--
    f_out.write("\n")


f_out = open("lmao.csv", "w+")

# --CODE BELOW--


# --CLOSE FILE--
f_out.close()
