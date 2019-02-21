using System;
using System.Text;
using NetMQ;
using NetMQ.Sockets;

namespace ByteComm
{
    public class ByteClient
    {
        readonly RequestSocket socket;

        public ByteClient(string sockname)
        {
            socket = new RequestSocket(sockname); 
        }

        public void Send_Byte(byte[] message)
        {
            socket.SendFrame(message);
        }

        public byte[] Recv_Byte()
        {
            return socket.ReceiveFrameBytes();
        }

        public void Send_String(string message)
        {
            socket.SendFrame(Encoding.ASCII.GetBytes(message));
        }

        public string Recv_String()
        {
            return socket.ReceiveFrameString();
        }

        public byte[] Send_And_Recv(byte[] message)
        {
            Send_Byte(message);
            return Recv_Byte();
        }

        public string Send_And_Recv(string message)
        {
            Send_String(message);
            return Recv_String();
        }

        public void Close()
        {
            socket.Close();
        }
    }
}
