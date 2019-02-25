using System;
using System.Threading;
using NetMQ;
using NetMQ.Sockets;

namespace CrowdWorld
{
    public class SpinServer
    {
          public bool ReqReady, RepReady;
          public byte[] ReqProto, RepProto;
          public bool Connected;

          private bool _listenerCancelled;
          private string sockname;
          private readonly Thread _listenerWorker;

          private void ListenerWork()
          {
              AsyncIO.ForceDotNet.Force();
              var spin = new SpinWait();
              using (var server = new ResponseSocket())
              {
                  server.Bind(sockname);

                  while (!_listenerCancelled)
                  {
                      RepReady = false;
                      if (!server.TryReceiveFrameBytes(out ReqProto)) {
                          spin.SpinOnce();
                          continue;
                      }
                      ReqReady = true;
                      while (!(RepReady || _listenerCancelled)) {
                        spin.SpinOnce();
                    }
                      server.TrySendFrame(RepProto);
                  }
              }
              NetMQConfig.Cleanup();
          }

          public SpinServer(string sname)
          {
              sockname = sname;
              _listenerWorker = new Thread(ListenerWork);
          }

          public void Start()
          {
              _listenerCancelled = false;
              _listenerWorker.Start();
          }

          public void Stop()
          {
              _listenerCancelled = true;
              _listenerWorker.Join();
          }
    }
}
