import multiprocessing as mp
import os


def task_1():
    # os.getpid() არის omp_get_thread_num()-ის შესაბამისი (პროცესის ID)
    # mp.cpu_count() აბრუნებს ბირთვების მთლიან რაოდენობას
    pid = os.getpid()
    total_cores = mp.cpu_count()
    print(f"Hello OpenMP | Process ID: {pid} | Total Cores: {total_cores}")


if __name__ == "__main__":
    # ვქმნით ერთ ქვე-პროცესს და ვუშვებთ მას
    p = mp.Process(target=task_1)
    p.start()
    p.join()  # ველოდებით პროცესის დასრულებას

# ახსნა: Python-ში ვიყენებთ multiprocessing ფექიჯს. თითოეულ 'worker'-ს
# აქვს თავისი უნიკალური PID, რაც C++-ის Thread ID-ის ანალოგია.
