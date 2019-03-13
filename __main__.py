import sys
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_problems(data_file_path):
    with open(data_file_path, 'r') as sch_file:
        for line in sch_file:
            yield line.strip()

def main(**kwargs):
    check_this_filename = "check_this"
    against_that_filename = "against_that"
    check_this_filepath = BASE_DIR + '/{}.txt'.format(check_this_filename)
    against_that_filepath = BASE_DIR + '/{}.txt'.format(against_that_filename)


    # with open(against_that_filepath) as ath, open(check_this_filepath) as ctf:
    with open(against_that_filepath) as ath:
        lines_against = ath.read().strip('\"').splitlines()
        lines_against = set(lines_against)
        # lines_length = len(lines_against)

        # lines_check = ctf.read().splitlines()
        # lines_check = [l.split(';$;') for l in lines_check]
        # lines_check = set(lines_check)

        # print('\n'.join(list(lines_check - lines_against).reverse()))

        # ok_count = len(lines_check - lines_against)
        ok_count = 0
        absent_count = 0
        test_count = 0




        # for problem in read_problems(check_this_filepath):
        #     test_count = test_count + 1

        #     i = 0
        #     for l in lines_against:
        #         i = i + 1
        #         lines_length = len(lines_against)
        #         if problem in l:
        #             ok_count = ok_count + 1
        #             break

        #         if i == lines_length:
        #             absent_count = absent_count + 1
        #             print(problem)

        # absent_count = test_count - ok_count

        for problem in read_problems(check_this_filepath):
            problem = problem.replace('\\"', '\"')
            if problem not in lines_against:
                absent_count = absent_count + 1
                print(problem)
            else:
                ok_count = ok_count + 1

        # print('test count: {}'.format(test_count))
        print('absent count: {}'.format(absent_count))
        print('ok count: {}'.format(ok_count))



if __name__ == '__main__':
    main(**dict(arg.replace('-', '').split('=')
                for arg in sys.argv[1:]))  # kwargs

