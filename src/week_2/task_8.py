from multiprocessing import Pool


def get_sum(numbers):
    # თითოეული პროცესი ითვლის თავის წილ მონაკვეთს
    return sum(numbers)


if __name__ == "__main__":
    # მონაცემები: 1-დან 100-მდე
    data = list(range(1, 101))

    # ვყოფთ მონაცემებს 4 ჩანკად (ნაწილად)
    chunks = [data[i : i + 25] for i in range(0, 100, 25)]

    with Pool(processes=4) as pool:
        # map აგროვებს თითოეული პროცესის მიერ დაბრუნებულ ნაწილობრივ ჯამებს
        partial_sums = pool.map(get_sum, chunks)

    # საბოლოო 'Reduction' ხდება მთავარ პროცესში
    final_total = sum(partial_sums)

    print(f"Partial sums: {partial_sums}")
    print(f"Final sums: {final_total}")

# ახსნა: Python-ში 'Reduction' სრულდება მონაცემების დაყოფით და შემდეგ
# ქვე პროცესებიდან მიღებული შედეგების სეკრებით.
