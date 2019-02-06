using System;
using ByteComm;

namespace DummyServerTest
{
    class Program
    {
        private const string sockname = "tcp://*:6566";

        static void Main(string[] args)
        {
            ByteServer cl = new ByteServer(sockname);
            cl.Dummy_Serve();
        }
    }
}
