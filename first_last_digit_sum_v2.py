#!/usr/bin/python

import os,sys,re

number_word_list = ['one','two','three','four','five','six','seven','eight','nine']
numeric_list = [1,2,3,4,5,6,7,8,9]

def find_first_last_digit(inp):
    index_begin = index_end = ''
    integer_list = re.findall('\d+',inp)
    if integer_list:
        begin_digit_integer = map(int,integer_list[0])[0]
        end_digit_integer = map(int,integer_list[-1])[-1]
        index_begin = inp.index(str(begin_digit_integer))
        index_end = inp.index(str(end_digit_integer))
    for number_word in number_word_list:
        matched_number_word_list = re.findall(number_word,inp)
        if matched_number_word_list:
            match_number_word = matched_number_word_list[0]
            index_matched_number = inp.index(match_number_word)
            inp_split = inp.split(match_number_word)
        if index_matched_number < index_begin:
            index_begin = index_matched_number
            index_number = number_word_list.index(match_number_word)
            begin_digit_integer = numeric_list[index_number]
        if inp_split[-1] == '':
            lastchars = inp_split[-2] + match_number_word
            index_end = inp.index(lastchars) + len(inp_split[-2])
            index_number = number_word_list.index(match_number_word)
            end_digit_integer = numeric_list[index_number]
        else:
            lastchars = match_number_word + inp_split[-1]
            index_matched_number_end = inp.index(lastchars)
            if index_matched_number_end > index_end:
                index_end = index_matched_number_end
                index_number = number_word_list.index(match_number_word)
                end_digit_integer = numeric_list[index_number]
        final_num = str(begin_digit_integer) + str(end_digit_integer)
        return final_num

    if __name__ == '__main__':
        input_data = sys.argv[1]
        sum_num = 0
        fl = open('C:\Users\Ranji\PycharmProjects\pythonProject\output.csv','r')
        if os.path.isfile(input_data):
            inp_file = open(input_data,'r')
            for line in inp_file:
                line = line.strip()
                two_digit_number = find_first_last_digit(input_data)
                sum_num += int(two_digit_number)
                dat = line + ',' + two_digit_number
                fl.write(dat + '\n')
        else:
            sum_num = find_first_last_digit(input_data)

        print(sum_num)
