# the python script for finding the best kali linux mirror
# according to your country, (having the lowest latency)
# designed by Mrsingh2002 (https://github.com/mrsinghh2002)

import re
import sys
import subprocess
import urllib
import xmltodict
from threading import Thread
import os


# values
hostlist = dict()
results = dict()
threads = list()


# measuring the latency and printing the latency speed for each and every
# mirror that is present in kali mirrors
def measureLatency(hostname):
    res = ''
    # -c 4 means that we are sending 4 packets to a particular mirrors
    p = subprocess.Popen(['ping', '-c 4', hostname], stdout=subprocess.PIPE, stderr= subprocess.PIPE).communicate()
    res = [x.decode('utf-8') for x in p]
    if not res[0]:
        # if there is not value returned then assigning the res as error
        results[hostname] = 9999
        res = "\033[31merror\033[0m"
    else:
        # regex expression for finding the time taken for sending a packet
        latencies = re.findall(r'time=([0-9\.]*)\sms', res[0])
        latencies = list(map(float, latencies))
        # finding the best average from sending 4 packets
        # we will be adding all the time taken divided to the length of our packets
        try:
            average = sum(latencies) / len(latencies)
            results[hostname] = average # main part was this as are logic is saved to results
            res = "\033[32m" + str(round(average, 2)) + "ms\033[0m" # this res is just for showing the user what's really happening with the script
            print("\033[32m[*]\033[0m Pinging \033[32m{hostname}\033[0m ... latency {latency}". format(hostname = hostname, latency = res))
        except:
            pass



def mainFunction():
    # getting the list of mirrors from meta4 file of kali
    meta_file = urllib.request.urlopen("http://http.kali.org/README.meta4")
    lists = xmltodict.parse(meta_file)

    print("\033[33m[*]\033[0m Calculating the mirror latency...")
    # metalink > file > url
    for info in lists['metalink']['file']['url']:
        url = urllib.parse.urlparse(info["#text"])
        # url contain scheme, netloc, path params, query and fragments
        hostlist[url.netloc] = str(url.path).replace("/README", "") #path='/kali/README'
        # url.netloc will give all the mirros
        # print(url.netloc)
        thread = Thread(target=measureLatency, args=[url.netloc])
        thread.start()
        # append all the threads to the list that we created above
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("\033[33m[*]\033[0m finding the best mirror for you :) ....")
    # taking results dict and converting it to a list with each item as ('mirror': 120.92)
    # also arranging them with pings in ascending order
    result = sorted(results.items(), key= lambda item: item[1])
    selected = result[0]
    # print(result)
    print("\033[33m[*]\033[0m found! the selected mirror: \033[32m{}\033[0m ... latency \033[32m{} ms\033[0m".format(selected[0], round(selected[1], 2)))

    selectedMirror = selected[0]
    # backing up the original file
    print("\033[33m[*]\033[0m backuping original /etc/apt/sources.list to /etc/apt/sources.list.bak")
    os.popen('cp /etc/apt/sources.list /etc/apt/sources.list.bak')
    print("\033[33m[*]\033[0m updating /etc/apt/source.list")
    newcontent = []

    try:
        read_only_sources_list = open("/etc/apt/sources.list", "r")
        for line in read_only_sources_list:
            if(re.search(r'# add with better-mirror', line)):
                # skip this section
                pass

            elif(re.search(r'^deb http(?:s|)://(.*)/kali kali-rolling', line)):
                newcontent.append("\n# " + line)

            elif re.search(r'^#\s*deb http(?:s|)://(.*)/kali kali-rolling', line):
                newcontent.append("\n" + line)

            elif re.search(r'^#\s*deb-src http(?:s|)://(.*)/kali kali-rolling', line):
                newcontent.append(line + "\n")

            elif line.strip():
                pass

            else:
                newcontent.append(line)

        newcontent.append("\ndeb http://{hostname}{path} kali-rolling main non-free contrib # add with better-mirror\n".format(hostname = selectedMirror, path=hostlist[selectedMirror]))



    except PermissionError:
        sys.exit("\033[31m[*] unsufficient permissions ... cannot open sources.list file\033[0m]")

    finally:
        read_only_sources_list.close()

    # writing the lines in sources.list file
    source_list = open("/etc/apt/sources.list", "w")

    for line in newcontent:
        source_list.writelines(line)

    # closing the file

    source_list.close()

    print("\033[33m[*]\033[0m running apt-get update for you....")
    os.system("apt-get update")
    print("\033[33m[*]\033[0m Thanks For Using The Tool!")












# first checking whether the user is running the command using sudo
# then,
# continue the command only if the user has kali distro

def sudoCheck():

    if not os.getuid() == 0:
        sys.exit("\n\033[31mcan please run this with root or sudo")
    else:
        osCheck()


def osCheck():
    # checking whether user has supported version or not
    with open('/etc/os-release') as release:

        version = re.search("VERSION_CODENAME=\"(.*)\"", release.read())
        if version[1] != "kali-rolling" :
            sys.exit("Don't know what destro you are using")
        elif version[1] == 'kali-rolling':
            sys.exit(mainFunction())


        else:
            sys.exit("Don't know what distro you are using")


    release.close()



if __name__ == "__main__":
    sudoCheck()
