import os
import time


def scan_into_file():
    print('scanning...')
    scan = 'hcitool scan > addresses.txt'  # looks for other blue-tooth discoverable devices and puts them into a file "addresses"
    os.system(scan)
    print('finished scanning.')


# writes them into "addresses.txt" in the following format: 12:34:56:78:90:00 name_of_device

def get_list_of_addresses():
    address_length = 18  # length of blue-tooth address
    addresses = []  # list of addresses

    file = open("addresses.txt", "r")  # reads the file which we scanned into
    lines = file.readlines()  # gets a list of all the lines in the file

    for line in lines[1:]:  # goes over each device's scan
        addresses.append(line[1:address_length])  # cuts out the address (the first 17 characters of each line)

    file.close()  # closes the file
    os.remove("addresses.txt")  # deletes the file so no residue
    return addresses  # returns the list purely of all the addresses


def signal_strength(addresses):
    strength_to_address = []  # the array which we will put the tuples with the address and the signal strength

    if os.path.exists("strength.txt"):  # checks if the file "strength" already exists (residue)
        os.remove("strength.txt")  # if it does then deletes it
    for address in addresses:  # goes over all the addresses
        connect = 'rfcomm connect 0 ' + address + ' 10 >/dev/null &'  # sends feelers to the address
        find = 'hcitool rssi ' + address + ' > strength.txt'  # while connected quickly check strength and put it into strength.txt
        os.system(connect)  # "attempt connection" should be refused
        time.sleep(4)  # let it refuse
        os.system(find)  # get the signal strength
        strength_to_address.append((address,
                                    get_strength()))  # makes array of tuples in the format of: (address, strength of signal to address) from strength.txt
    return strength_to_address  # returns the tuple of arrays


def get_strength():
    file = open("strength.txt", "r")  # opens the file "strength.txt" which has the echoed results of the rssi
    lines = file.readlines()  # puts the one line into lines
    if len(lines) > 0:  # if the line exists go over it to grab the strength
        strength = lines[0][19:len(lines[0]) - 1]  # gets the number you need
    else:  # if there is no line then it didn't get a signal so throw an error
        strength = "error, no lines in strength"  # puts an error message instead of the strength
    file.close()  # closes the file "strength.txt"
    return strength  # returns either the signal strength or the error message


def put_into_file(array):
    i = 0
    if os.path.exists("signals.txt"):  # checks if the file "addresses" already exists (residue)
        os.remove("signals.txt")  # if it does then deletes it
    signal_str = open("signals.txt", "w+")  # makes the file "addresses"
    signal_str.write('{' + '\n')
    for signals in array:
        signal_str.write('"' + str(i) + '" : {' + '\n')
        signal_str.write('"ID" : ' + '"' + signals[0] + '",' + "\n")
        signal_str.write('"strength" : ' + '"' + signals[1] + '",' + "\n")
        signal_str.write('},' + '\n')
        i += 1
    signal_str.write('}')
    signal_str.close()
    return


print('app started....')
scan_into_file()  # scans and gets unformatted address
address = get_list_of_addresses()  # formats the addresses
print(address)  # prints it
signals = signal_strength(address)  # gets the signal strength of each address
print(signals)  # prints the tuples of address and signal strength
put_into_file(signals)
with open("signals.txt") as file:
    print(file.read())
import os
import time


def scan_into_file():
	print('scanning...')
	scan = 'hcitool scan > addresses.txt'  # looks for other blue-tooth discoverable devices and puts them into a file "addresses"
	os.system(scan)
	print('finished scanning.')


# writes them into "addresses.txt" in the following format: 12:34:56:78:90:00 name_of_device

def get_list_of_addresses():
	address_length = 18  # length of blue-tooth address
	addresses = []  # list of addresses

	file = open("addresses.txt", "r")  # reads the file which we scanned into
	lines = file.readlines()  # gets a list of all the lines in the file

	for line in lines[1:]:  # goes over each device's scan
		addresses.append(line[1:address_length])  # cuts out the address (the first 17 characters of each line)

	file.close()  # closes the file
	os.remove("addresses.txt")  # deletes the file so no residue
	return addresses  # returns the list purely of all the addresses


def signal_strength(addresses):
	strength_to_address = []  # the array which we will put the tuples with the address and the signal strength

	if os.path.exists("strength.txt"):  # checks if the file "strength" already exists (residue)
		os.remove("strength.txt")  # if it does then deletes it
	for address in addresses:  # goes over all the addresses
		connect = 'rfcomm connect 0 ' + address + ' 10 >/dev/null &'  # sends feelers to the address
		find = 'hcitool rssi ' + address + ' > strength.txt'  # while connected quickly check strength and put it into strength.txt
		os.system(connect)  # "attempt connection" should be refused
		time.sleep(4)  # let it refuse
		os.system(find)  # get the signal strength
		strength_to_address.append((address,
									get_strength()))  # makes array of tuples in the format of: (address, strength of signal to address) from strength.txt
	return strength_to_address  # returns the tuple of arrays


def get_strength():
	file = open("strength.txt", "r")  # opens the file "strength.txt" which has the echoed results of the rssi
	lines = file.readlines()  # puts the one line into lines
	if len(lines) > 0:  # if the line exists go over it to grab the strength
		strength = lines[0][19:len(lines[0]) - 1]  # gets the number you need
	else:  # if there is no line then it didn't get a signal so throw an error
		strength = "error, no lines in strength"  # puts an error message instead of the strength
	file.close()  # closes the file "strength.txt"
	return strength  # returns either the signal strength or the error message


def put_into_file(array):
	i = 0
	if os.path.exists("signals.txt"):  # checks if the file "addresses" already exists (residue)
		os.remove("signals.txt")  # if it does then deletes it
	signal_str = open("signals.txt", "w+")  # makes the file "addresses"
	signal_str.write('{' + '\n')
	for signals in array:
		signal_str.write('"' + str(i) + '" : {' + '\n')
		signal_str.write('"ID" : ' + '"' + signals[0] + '",' + "\n")
		signal_str.write('"strength" : ' + '"' + signals[1] + '",' + "\n")
		signal_str.write('},' + '\n')
		i += 1
	signal_str.write('}')
	signal_str.close()
	return


print('app started....')
scan_into_file()  # scans and gets unformatted address
address = get_list_of_addresses()  # formats the addresses
print(address)  # prints it
signals = signal_strength(address)  # gets the signal strength of each address
print(signals)  # prints the tuples of address and signal strength
put_into_file(signals)
with open("signals.txt") as file:
	print(file.read())
