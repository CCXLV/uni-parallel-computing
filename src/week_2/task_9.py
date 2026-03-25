import multiprocessing as mp
import time


def critical_print(lock, process_id):
    # 'with lock' არის #pragma omp critical-ის პირდაპირი ანალოგი
    with lock:
        print(f"--- Process {process_id} entered to critical section ---")
        time.sleep(0.1)  # სიმულაცია
        print(f"Process {process_id} finished working.")


if __name__ == "__main__":
    mutex = mp.Lock()
    processes = [mp.Process(target=critical_print, args=(mutex, i)) for i in range(4)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

# ახსნა: Lock (Mutex) უზრუნველყოფს, რომ კონსოლზე ბეჭდვის დროს ტექსტი
# არ აირიოს. მხოლოდ ერთ პროცესს აქვს უფლება ფლობდეს 'Lock'-ს მოცემულ დროს.
