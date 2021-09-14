import os
from Trialteration import Trialteration
from Trialteration import Point

def run_pi(ip_address):
    makedir = 'mkdir ' + ip_address
    connect = 'ssh yarinop@' + ip_address + ' python Client.py'
    steal_doc = 'scp yarinop@' + ip_address + ':signals.txt ' + ip_address
    os.system(makedir)
    os.system(connect)
    os.system(steal_doc)

def power_to_distance(rssi):
    n = 2
    TxPower = -12 #+6dbm(class), -52
    distance  = 10 ** ((TxPower + rssi) / 10*n)
    return distance

class device:
    def __init__(self, ids):
        self.id = ids
        self.coordinates = list()
        self.strengths = list()
        self.distance = list()
        self.location = Point(0,0)

def combine(ip, locs):
    devices = []

    file1 = open('192.168.1.36/signals' + '.txt', "r")

    lines1 = file1.readlines()

    device_id = lines1[2][8:-2]
    curr_device = device(device_id)
    print ("device id: ", device_id)
    curr_device.coordinates.append(locs[0])
    curr_device.coordinates.append(locs[1])
    curr_device.coordinates.append(locs[2])

    curr_device.strengths.append(int(lines1[3][14:-3]))


    devices.append(curr_device)
    return devices

def run_all(locs):
    ip = '192.168.1.36'
    run_pi(ip)
    devices = combine(ip, locs)

    for curr_device in devices:
        curr_device.distance.append(power_to_distance(curr_device.strengths[0]))


    for curr_device in devices:
        curr_device.location = Trialteration(locs[0], locs[1], locs[2], curr_device.distance[0], 9, 3.2)
        XY = Trialteration(pointA, pointB, pointC, )
        print ("X: " +XY.getX() + " Y: " + XY.getY())

    for curr_device in devices:
        print ("Device ID: " + curr_device.id + " X Value: " + str(curr_device.location.getX()))
        print (" Y Value: " + str(curr_device.location.getY())) #the line was too long

def main():
    locs = []
    locs.append(Point(0, 0))
    locs.append(Point(5, 0))
    locs.append(Point(3, -6))
    run_all(locs)

main()
