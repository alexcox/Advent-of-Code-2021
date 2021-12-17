from math import prod

input = open('input/day16.txt', 'r').read()
input = ''.join(list(map(lambda x: bin(int(x, 16))[2:].zfill(4), list(input))))

values = []

def part1(packet = input):
    packet_len = len(packet)
    V = int(packet[:3], 2)
    values.append(V)
    packet = packet[3:]
    T = int(packet[:3], 2)
    packet = packet[3:]
    if T == 4: # literal value:
        value = ''
        while packet:
            value += packet[1:5]
            fc = packet[0]
            packet = packet[5:]
            if fc == '0': break
    else: # operator
        I = packet[:1]
        packet = packet[1:]
        if I == '0':
            sub_packet_len = int(packet[:15], 2)
            packet = packet[15:]
            subpackets = packet[:sub_packet_len]
            while subpackets:
                subpackets = part1(subpackets)
            packet = packet[sub_packet_len:]
        else:
            sub_packet_count = int(packet[:11], 2)
            packet = packet[11:]
            for i in range(sub_packet_count):
                packet = part1(packet)
    return packet

def part2(packet = input):
    packet_len = len(packet)
    V = int(packet[:3], 2)
    packet = packet[3:]
    T = int(packet[:3], 2)
    packet = packet[3:]
    if T == 4: # literal value:
        value = ''
        while packet:
            value += packet[1:5]
            fc = packet[0]
            packet = packet[5:]
            if fc == '0':
                return packet, int(value, 2)
    else: # operator
        I = packet[:1]
        packet = packet[1:]
        vs = []
        if I == '0':
            sub_packet_len = int(packet[:15], 2)
            packet = packet[15:]
            subpackets = packet[:sub_packet_len]
            packet = packet[sub_packet_len:]
            while subpackets:
                subpackets, _ = part2(subpackets)
                vs.append(_)
        else:
            sub_packet_count = int(packet[:11], 2)
            packet = packet[11:]
            for i in range(sub_packet_count):
                packet, _ = part2(packet)
                vs.append(_)
        if T == 0:
            return packet, sum(vs)
        elif T == 1:
            return packet, prod(vs)
        elif T == 2:
            return packet, min(vs)
        elif T == 3:
            return packet, max(vs)
        elif T == 5:
            return packet, 1 if vs[0] > vs[1] else 0
        elif T == 6:
            return packet, 1 if vs[0] < vs[1] else 0
        elif T == 7:
            return packet, 1 if vs[0] == vs[1] else 0

part1()
print(f'Solution to part 1: {sum(values)}')
print(f'Solution to part 2: {part2()[1]}')