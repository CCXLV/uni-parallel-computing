import multiprocessing as mp


def increment(counter, lock, atomic_mode):
    for _ in range(100000):
        if atomic_mode:
            # Task 7: Atomic/Lock-ის გამოყენება უსაფრთხოებისთვის
            with lock:
                counter.value += 1
        else:
            # Task 6: Race Condition (Lock-ის გარეშე)
            counter.value += 1


if __name__ == "__main__":
    # 'i' ნიშნავს shared integer-ს (საერთო მეხსიერება)
    val = mp.Value("i", 0)
    mutex = mp.Lock()  # ეს არის 'Talking Stick'

    # შეცვალეთ True -> False-ზე რომ ნახოთ შეცდომა (Task 6)
    procs = [mp.Process(target=increment, args=(val, mutex, True)) for _ in range(4)]

    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print(f"Final value: {val.value}")

# ახსნა: Lock-ის გარეშე პროცესები ერთდროულად ცდილობენ ცვლადის შეცვლას,
# რაც იწვევს მონაცემების დაკარგვას. Lock უზრუნველყოფს 'Mutual Exclusion'-ს.
