from multiprocessing import Pool


def process_arrays(index):
    # სიმულაცია: გვაქვს ორი მასივი A და B
    # რეალურ დავალებაში აქ მასივებიდან წაიკითხავდით მნიშვნელობებს
    a_val = index
    b_val = index * 10

    # ტასკი 4 & 5: გაორმაგება და შეკრება
    c_val = a_val + b_val
    return c_val


if __name__ == "__main__":
    # 10 ელემენტიანი მასივის დამუშავება პარალელურად
    with Pool(4) as p:
        # ინდექსების მიხედვით პარალელური გამოთვლა
        result_array_c = p.map(process_arrays, range(10))

    print(f"Result array C: {result_array_c}")

# ახსნა: თითოეული ინდექსის გამოთვლა ხდება სხვადასხვა ბირთვზე.
# ეს არის მონაცემთა პარალელიზმის (Data Parallelism) მაგალითი.
