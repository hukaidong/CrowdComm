#!/usr/bin/env python
# encoding: utf-8

import zmq

class ByteClient(object):
  def __init__(self, sock_name):
      self._ctx = zmq.Context()
      self.pipe = self._ctx.socket(zmq.REQ)
      self.pipe.connect(sock_name)

  def send_byte(self, string):
      self.pipe.send_string(string)

  def recv_byte(self):
      return self.pipe.recv_string()

  def send_and_recv(self, string):
      self.send_byte(string)
      return self.recv_byte()

if __name__ == '__main__':
  bc = ByteClient(r"ipc:///tmp/sock_temp")
  try:
    while (True):
      s = input()
      print(bc.send_and_recv(s))
  except KeyboardInterrupt:
    print("bye.")

