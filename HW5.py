import string
import random
import os
import time
import multiprocessing as mp


def randomLetter():
    return random.choice(string.ascii_lowercase)


def randomLetterIterator(n):
    generated_letters = []
    for i in range(n):
        generated_letters.append(randomLetter())
    return generated_letters


def randomLetterWrapperMultiCore(num_letters, num_available_cores):
    import multiprocessing as mp

    results = []
    if __name__ == '__main__':
        pool = mp.Pool(num_available_cores)

        results = pool.map(randomLetterIterator, [int(num_letters / num_available_cores)] * num_available_cores)

        pool.close()

    return results


num_available_cores = os.cpu_count() - 1
num_letters = 1000000


if __name__ == '__main__':
    pool = mp.Pool(num_available_cores)

    start_time_multiple = time.time()
    results = [pool.apply(randomLetterIterator, args=(int(num_letters / num_available_cores),))]
    end_time_multiple = time.time()
    pool.close()

    start_time_single = time.time()
    randomLetterIterator(num_letters)
    end_time_single = time.time()

    print('Time for ' + str(num_letters) + ' letters on single core: {} seconds'.format(end_time_single - start_time_single))
    print('Time for ' + str(num_letters) + ' letters on multiple cores: {} seconds'.format(end_time_multiple - start_time_multiple))
