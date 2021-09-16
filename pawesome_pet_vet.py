def main():
    animals = [["edgr allan","dog", 80],["jane clawston","cat", 20],["franze catka","cat", 60],["bark twain","dog", 40]]\

    answer = input("check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit")

    while answer != "q":
        if answer == "i":
            name = input("gimme the name")
            type = input("gimme the type")
            urgency = int(input("gimme the urgency (0-100)"))

            while urgency > 100 or urgency < 0:
                urgency = int(input("please enter (0-100)"))

            print(name + " is checked in!")
            new = [name,type, urgency]
            animals.append(new)
        elif answer == "o":

            for x, element in enumerate(animals):
                str1 = ""
                str1 = element[0] + ", " + element[1]
                print(x+1, "-" , str1)
            answer1 = int(input("Please enter a number to check an animal out of the clinic"))
            checked_out = animals[answer1-1][0]
            print(checked_out, " is checked out")
            animals.pop(answer1-1)
            for x, element in enumerate(animals):
                str1 = ""
                str1 = element[0] + ", " + element[1]
                print(x + 1, "-", str1)

        elif answer == "m":
            maxx = 0
            final = []



            for elem in animals:
                if elem[2] > maxx:
                    maxx = elem[2]
                    final = elem

            print(final[0], final[1], "with urgency", final[2], ", should be seen right away!")
        elif answer == "l":
            minn = 100
            final = []

            for elem in animals:
                if elem[2] < minn:
                    minn = elem[2]
                    final = elem

            print(final[0], final[1], "with urgency", final[2], ", can wait!")

        elif answer == "f":
            names = input("please enter a name to search for")
            for elem in animals:
                if names in elem:
                    print(elem)
                    break
                else:
                    print("None")
                    break
        elif answer == "a":
            output = []


            for elem in animals:
                output.append(elem[0])

            output.sort()

            for x, elements in enumerate(output):
                print(x+1,"-", elements)


















        answer = input("check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit")




main()
