import multiprocessing as mp
import os


def task_2():
    # თითოეული პროცესი ბეჭდავს თავის უნიკალურ ნომერს (PID)
    print(f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    # ეს არის omp_set_num_threads(4)-ის შესაბამისი ლოგიკა
    process_count = 4
    processes = [mp.Process(target=task_2) for _ in range(process_count)]

    # ყველა პროცესის ერთდროულად გაშვება
    for p in processes:
        p.start()

    # ყველა პროცესის დასრულების ლოდინი (Synchronization)
    for p in processes:
        p.join()

# ახსნა: ჩვენ ხელით ვქმნით 4 ცალკეულ პროცესს. ეს უზრუნველყოფს,
# რომ ოპერაციულმა სისტემამ ზუსტად 4 პარალელური 'worker' გამოიყენოს.
