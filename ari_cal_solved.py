'''
1) receives a list of strings that are arithmetic problems and
2) returns the problems arranged vertically and side-by-side.
3) The function should optionally take a second argument.
4) When the second argument is set to `True`, the answers should be displayed.

Sample lists:
['3801 - 2', '123 + 49']
['1 + 2', '1 - 9380']
['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87']
['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']
['3 + 855', '988 + 40']
['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']

Rules
The function will return the correct conversion if the supplied problems are properly formatted,
otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
a) If there are too many problems supplied to the function. The limit is five, anything more will return:
"Error: Too many problems." -ok

b) The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error.
Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
"Error: Operator must be '+' or '-'." -ok

c) Each number (operand) should only contain digits. Otherwise, the function will return:
"Error: Numbers must only contain digits."-ok

d) Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
"Error: Numbers cannot be more than four digits." -ok

If the user supplied the correct format of problems, the conversion you return will follow these rules:
i) There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand,
both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
ii) Numbers should be right-aligned.
iii) There should be four spaces between each problem.
iv) There should be dashes at the bottom of each problem.
The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

'''
"""
# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

# Run unit tests automatically
main()
"""

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


'''
1) receives a list of strings that are arithmetic problems and
2) returns the problems arranged vertically and side-by-side.
3) The function should optionally take a second argument.
4) When the second argument is set to `True`, the answers should be displayed.
'''
import re
problems = list()
def arithmetic_arranger(problems, answer=False):
    x = str(problems).split('],')
    if len(x) == 1:
        #funtru = 0
        prob_string = x[0]
    else:
      #funtru = x[1].strip()
        prob_string = x[0]+']'


    nsp_string = prob_string.replace(" ","")
    prob = nsp_string.split(",")
    lstnum = list()
    lstop = list()
    numdigsum = 0
    for item in prob:
        nums = re.findall('[0-9999]+', item)
        ops = re.findall('[+]|[-]', item)
        for num in nums:
            if len(str(num)) > 4:
                return("Error: Numbers cannot be more than four digits.")
                quit()
            numdigsum = numdigsum + len(str(num))
            lstnum.append(num)
        for op in ops:
            lstop.append(op)

    if len(lstop)<len(prob):
        return("Error: Operator must be '+' or '-'.")
        quit()
    if len(prob) > 5:
        return("Error: Too many problems.")
        quit()
    sum_digcha = 2+2*len(prob) + len(prob) + len(prob) - 1  + numdigsum
    if len(nsp_string) != sum_digcha:
        return("Error: Numbers must only contain digits.")
        quit()

    lsttop = list()
    lstbot = list()
    lstdsh = list()
    lstans = list()
    lstfulans = list()
    betprob = 4*' '
    for n in range(0,len(lstnum),2):
        evnum = lstnum[n]
        odnum = lstnum[n+1]
        opchar = lstop[int(n/2)]

        if opchar == '+':
            ans = int(evnum) + int(odnum)
        elif opchar == '-':
            ans = int(evnum) - int(odnum)
        lstans.append(ans)

        difflen = len(evnum) - len(odnum)

        if difflen<0:
            addsp_evnum = (-1*difflen + 2)*" " + evnum
            lsttop.append(addsp_evnum)
            lstbot.append(opchar + " " + odnum)

        if difflen>0:
            addsp_odnum = (difflen)*" " + odnum
            lstbot.append(opchar + " " + addsp_odnum)
            lsttop.append(2*" " + evnum)

        if difflen == 0:
            lsttop.append(2*" " + evnum)
            lstbot.append(opchar + " " + odnum)

    for i in range(len(prob)):
        dashes = len(lstbot[i])*"-"
        lstdsh.append(dashes)
        dif_dhan = len(lstdsh[i]) - len(str(lstans[i]))
        if dif_dhan > 0:
            fullans = dif_dhan*" " + str(lstans[i])
            lstfulans.append(fullans)
        else:
            lstfulans.append(lstans[i])

    jlstop = betprob.join(lsttop)
    jlstbot = betprob.join(lstbot)
    jlstdsh = betprob.join(lstdsh)
    jlstfulans = betprob.join(lstfulans)
    if answer:
        return(jlstop + "\n" + jlstbot+ "\n" + jlstdsh + "\n" + jlstfulans)
    else:
        return(jlstop+ "\n" + jlstbot + "\n" + jlstdsh)


    #return arranged_problems
