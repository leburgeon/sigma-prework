def get_max_and_min(integers_list: list[int]) -> list[int]:
    current_min = current_max = integers_list[0]

    for i in range(1, len(integers_list)):
        if integers_list[i] < current_min:
            current_min = integers_list[i]
        elif integers_list[i] > current_max:
            current_max = integers_list[i]

    return [current_min, current_max]


def main():
    while True:
        print('please enter your list of integers, separated by commas eg 1,-2,3,-4,5')
        user_input_integers = input('> ')
        integer_list = user_input_integers.split(',')
        invalid_input = False
        for i, num in enumerate(integer_list):
            try:
                integer_list[i] = int(num)
            except:
                print(f'invalid input: {num}')
                invalid_input = True
                break

        if not invalid_input:
            min_max = get_max_and_min(integer_list)
            print(min_max)


if __name__ == '__main__':
    main()
