using System;
using ByteComm;

namespace DummyClientTest
{
    class Program
    {
        private const string sockname = "tcp://localhost:6566";

        static void Main(string[] args)
        {
            ByteClient cl = new ByteClient(sockname);
            while (true) 
            {
                string msg = Console.ReadLine();
                msg = cl.Send_And_Recv(msg);
                Console.WriteLine(msg);
            }
        }
    }
}
