from multiprocessing import Pool
import os
import time


def loop_body(i):
    # თუ დიაპაზონი მცირე ზომისაა Python ხშირად ერთ პროცესზე უშვებს იტერაციას,
    # time.sleep ის გამოყენებით კი იძულებული ხდება სხვა პროცესებიც გამოიყენოს
    time.sleep(0.1)
    # ვაჩვენებთ თუ რომელმა PID-მა შეასრულა კონკრეტული იტერაცია
    print(f"Iteration {i:2} was done by PID: {os.getpid()}")


if __name__ == "__main__":
    # Pool(4) არის #pragma omp parallel for-ის პირდაპირი ალტერნატივა
    with Pool(processes=4) as pool:
        # pool.map ავტომატურად ანაწილებს 0-19 დიაპაზონს 4 პროცესზე
        pool.map(loop_body, range(20))

# ახსნა: Pool.map ფუნქცია ჭრის ციკლს ნაწილებად და თითოეულ
# ნაწილს გადასცემს თავისუფალ პროცესს შესასრულებლად.
