# // PROBLEM DEFINITION
# // ------------------
# // Reverse each word in the input string.
# // The order of the words will be unchanged.
# // A word is made up of letters and/or numbers.
# // Other characters (spaces, punctuation) will not be reversed.
# // NOTES
# // ------
# // Write production quality code
# // We prefer clarity over performance (though if you can achieve both - great!)
# // You can use the language that best highlights your programming ability
# // the template below is in C++
# // A working solution is preferred (assert in main() should succeed)
# // Bonus points for good tests

def reverse(sentence):
    sentence_list = sentence.split(" ")
    reverse_list = []
    for s in sentence_list:
        if s.isalnum():
            # check if all letters are alphanumeric
            reverse_list.append(s[::-1])
        else:
            # if not all alphanumeric
            letters = list(s)
            indices = []
            reversed_letters = []
            punctuation = []

            # identify position of punctuation
            for i in range(len(letters)):
                if not letters[i].isalnum():
                    indices.append(i)
                    punctuation.append(letters[i])
                else: 
                    # keep alphanumeric
                    reversed_letters.append(letters[i])

            # print(indices)
            # print(punctuation)
            
            reversed_letters.reverse()

            # add back punctuation in normal spot
            for idx in range(len(indices)):
                reversed_letters.insert(indices[idx], punctuation[idx])
                # if idx == 0:
                #     reversed_letters.insert(indices[idx], punctuation[idx])
                # elif idx != len(indices):
                #     reversed_letters.insert(indices[idx]+1, punctuation[idx])
            
            rev_string = ''.join(reversed_letters)
            reverse_list.append(rev_string)

    return ' '.join(reverse_list)
    

def main():
    # line = input("Enter sentence: ")
    # print(reverse(line))

    # TESTS

    # double space
    assert reverse("hi  my name's john 123") == "ih  ym sema'n nhoj 321"

    # single space
    assert reverse("hi my name's john 123") == "ih ym sema'n nhoj 321"   

    # only letters
    assert reverse("hi my name's john") == "ih ym sema'n nhoj"  

    # seperate numbers
    assert reverse("1 2 3 4") == "1 2 3 4"

    # only numbers
    assert reverse("1234") == "4321"        

    # consecutive punctuation
    assert reverse("hi m??y name's john") == "ih y??m sema'n nhoj"   

    # no spaces (single word)
    assert reverse("himynameisjohn") == "nhojsiemanymih"

main()