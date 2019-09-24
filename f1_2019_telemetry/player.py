#! /usr/bin/env python3

import argparse
import time
import sqlite3
import socket

from f1_2019_telemetry.packets import HeaderFieldsToPacketType

def playback(filename, realtime_factor):

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.connect(('<broadcast>', 20777))

    query = "SELECT timestamp, packet FROM packets ORDER BY pkt_id;"

    cursor.execute(query)

    t_first_packet = None
    t_start_playback = time.monotonic()
    while True:
        timestamped_packet = cursor.fetchone()
        if timestamped_packet is None:
            break
        (timestamp, packet) = timestamped_packet
        if t_first_packet is None:
            t_first_packet = timestamp
        t_playback = (timestamp - t_first_packet) / realtime_factor + t_start_playback
        t_sleep = max(0.0, t_playback - time.monotonic())
        time.sleep(t_sleep)
        sock.send(packet)
        print(timestamp)

    cursor.close()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Replay an F1 2019 session as UDP packets")

    parser.add_argument("-r", "--rtf")
    parser.add_argument("-d", "--destination")
    parser.add_argument("-p", "--port")
    parser.add_argument("filename")

    playback(filename, realtime_factor)
    
if __name__ == "__main__":
    main()
