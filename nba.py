import csv
file_name = open('stats-clean','r')

sp = file_name.read().split("\n")

with open('report.csv','w',newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(["NAME", "PERCENT"])

    for elem in sp:

        element = elem.split(",")



        try:
            percentage = format(float(element[4]) / float(element[5]), ".2f")
            if int(element[3]) >= 50 and float(percentage) >= 0.5:
                thewriter.writerow([element[0],str(percentage)])
        except:
            print()


file_name.close()



        











