import json
import dateutil.parser
import Modify
import gc

class Parse:

    Modify.Modify()

    with open('modsession.json') as json_file:
        data = json.load(json_file)

    file = open("output.csv", "w")
    port = open("port.txt", "w+")
    ip = open("ip.txt", "w+")
    time = open("time.txt", "w+")

    count = 0
    honeypots = {}
    for x in data:
        if "protocol" not in x:
            file.write("," + x["timestamp"]["$date"] + "," + x["source_ip"] + ",")
        else:
            file.write(x["protocol"] + "," + x["timestamp"]["$date"] + "," + x["source_ip"] + ",")
        file.write(str(x["destination_port"]) + "," + x["honeypot"] + "\n")
        port.write(str(x["destination_port"]) + "\n")
        # str = x["timestamp"]["$date"]
        time.write(str(dateutil.parser.isoparse(x["timestamp"]["$date"].rstrip('Z') + "+00")) + "\n")
        ip.write(x["source_ip"] + "\n")
        count += 1
        if x["honeypot"] in honeypots:
            honeypots[x["honeypot"]] += 1
        else:
            honeypots[x["honeypot"]] = 1

    print("Total Number of Attacks:", count, "\n")
    gc.collect()

    printer = sorted(honeypots.items(), reverse=True, key=lambda x: x[1])
    print("Honeypots Ranked by Attacks: ")
    for key in printer:
        line_new = '{:<14}  {:<2}  {:<2}'.format(key[0], ":", key[1])
        print("\t" + line_new)
    file.close()

    ip.seek(0)
    attack = open("ipAnalysis.txt", "w")
    D = {}
    for aline in ip:
        temp = aline.rstrip()
        if temp in D:
            D[temp] = D.get(temp) + 1
        else:
            D[temp] = 1

    printer = sorted(D.items(), reverse=True, key=lambda x: x[1])
    for key in printer:
        attack.write(key[0] + ": " + str(key[1]) + "\n")

    print("\nTop 5 Attacker IPs:")
    for x in range(0, 5):
        print("\t" + str(printer[x][0]) + "\t:\t" + str(printer[x][1]))

    attack.close()
    ip.close()

    port.seek(0)
    ported = open("portAnalysis.txt", "w")
    dic = {}
    for aline in port:
        temp = aline.rstrip()
        if temp in dic:
            dic[temp] = dic.get(temp) + 1
        else:
            dic[temp] = 1

    printer = sorted(dic.items(), reverse=True, key=lambda x: x[1])
    for key in printer:
        ported.write(key[0] + ": " + str(key[1]) + "\n")

    print("\nTop 5 Attacked Ports:")
    for x in range(0, 5):
        line_new = '{:<6}  {:<2}  {:<2}'.format(printer[x][0], ":", printer[x][1])
        print("\t" + line_new)

    ported.close()
    port.close()

    time.seek(0)
    hours = {}
    max = 0
    count = 0
    for each in time:
        hour = str(each[9]) + str(each[11]) + str(each[12])
        if hour in hours:
            hours[hour] = hours.get(hour) + 1
        else:
            hours[hour] = 1

    total = 0
    for key in hours:
        total += 1
        if int(key) - 699 > 24:
            count += int(hours.get(key))
            count -= int(hours.get(str(int(key)-100)))
        else:
            count += int(hours.get(key))
        if count > max:
            max = count
    print("\nMax Attacks in 24 hrs:", max)
    print("Total Runtime (approx): ", total, "hrs")

    time.close()
