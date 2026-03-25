from multiprocessing import Pool
import time


def compute_sum(chunk):
    return sum(chunk)


if __name__ == "__main__":
    # 10 მილიონი ელემენტი
    size = 10_000_000
    data = list(range(size))

    # სერიული გამოთვლა (Serial)
    start_serial = time.time()
    total_serial = sum(data)
    end_serial = time.time()
    print(f"Total time: {end_serial - start_serial:.4f} seconds")

    # პარალელური გამოთვლა (Parallel Reduction)
    # ვყოფთ მასივს 4 ნაწილად
    chunk_size = size // 4
    chunks = [data[i : i + chunk_size] for i in range(0, size, chunk_size)]

    start_parallel = time.time()
    with Pool(processes=4) as pool:
        partial_sums = pool.map(compute_sum, chunks)
    total_parallel = sum(partial_sums)
    end_parallel = time.time()

    print(f"Parallel time: {end_parallel - start_parallel:.4f} seconds")

# ახსნა: დროის გასაზომად ვიყენებთ time.time()-ს.
# დიდ მასივებზე პარალელური გამოთვლა უფრო სწრაფია, რადგან დავალება
# ნაწილდება CPU-ს რამდენიმე ბირთვზე.
