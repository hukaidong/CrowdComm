using System;
using System.Text;
using NetMQ;
using NetMQ.Sockets;

namespace ByteComm
{
    public class ByteServer
    {
        readonly ResponseSocket socket;

        public ByteServer(string sockname)
        {
            socket = new ResponseSocket();
            socket.Bind(sockname);
        }

        public void Send_Byte(byte[] message)
        {
            socket.SendFrame(message);
        }

        public void Send_String(string message)
        {
            socket.SendFrame(Encoding.ASCII.GetBytes(message));
        }

        public byte[] Recv_Byte()
        {
            return socket.ReceiveFrameBytes();
        }

        public string Recv_String()
        {
            return socket.ReceiveFrameString();
        }

        public string Try_Recv_String()
        {
            string a;
            bool result = socket.TryReceiveFrameString(out a);
            return result? a: "";
        }

        public void Dummy_Serve()
        {
            while (true)
            {
                string msg_recv = Recv_String();
                string msg = "From C#, I've got: " + msg_recv;
                Send_String(msg);
            }
        }

        public void Close()
        {
            socket.Close();
        }
    }
}