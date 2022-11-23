from src.core import Storage
storage = Storage('bnc', 'resources')

def num_is_legit(num, length):
    if len(num) != length:
        return False
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                return False
    return True

if not storage.exists('bnclists.json'):
    print('Fresh BNCSolver installation! Rendering solving data (it might take a while).')
    lists = {length: [str(num) for num in range(10 ** (length - 1), 10 ** length) if num_is_legit(str(num), length)] for length in range(1, 10)}
    storage.write_json('bnclists.json', lists)
    print('Render complete!')
else:
    lists = storage.load_json('bnclists.json')

class BncSolver:
    def __init__(self, length=4):
        self.length = length
        self.possible_nums_list = lists[str(length)].copy()

        self.attempts = []

    def compare_numbers(self, a, b):
        """
        compare 2 numbers and tells how many bulls and cows in it
        :param a: str of first number
        :param b: str of second number
        :return: tuple (bulls,cows)
        """
        bulls = 0
        cows = 0
        for dig1 in range(self.length):
            if a[dig1] == b[dig1]:
                bulls += 1
            for dig2 in range(self.length):
                if a[dig1] == b[dig2]:
                    cows += 1
        cows -= bulls  # becasue it includes the bulls
        return bulls, cows

    def guess(self, answer_bulls, answer_cows, number=None):
        """
        main algorithm, runs the interactive programm
        :return: none
        
        print("\nWelcome to the game Bulls&Cows, guess a number and let the programm"
            "find your guess.\n\n"
            "Think of a number of 4 digits, no duplicates, and no zeros.\n"
            "answer the questions by assigning 2 numbers each time "
            "like that-\n\"Bulls\" \"Cows\"\n"
            "Example: the number is 1234, the guess was 2134, "
            "so your answer should be \'2 2\'\n"
            "Good luck!\n")
        """

        number_try = self.possible_nums_list[0] if not number else number
        new_list = []

        for num in self.possible_nums_list:
            # check if numbers in list fits current result, if not, remove them
            if self.compare_numbers(num, str(number_try)) == (int(answer_bulls), int(answer_cows)):
                new_list.append(num)
        self.possible_nums_list = new_list
        return self.possible_nums_list[0] if self.possible_nums_list else None