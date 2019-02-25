require 'CrowdComm/Util'

module CrowdComm
  require 'ffi-rzmq'

  class ByteClient
    include ZMQ
    include CrowdComm::Utils

    def initialize(sockname = "tcp://localhost:6566")
      @context = Context.new(1)
      @pipe = @context.socket(REQ)
      rc = @pipe.connect(sockname)
      raise "Fail to connect ot server." if got_error(rc)
    end

    def send_bytes(bytes)
      if got_error @pipe.send_string(bytes)
        raise 'Fail to send message'
      end
    end

    def get_bytes
      msg = ''
      if got_error @pipe.recv_string(msg)
        raise 'Fail to receive message'
      end
      msg
    end

    def send_and_get(bytes)
      send_bytes(bytes)
      get_bytes
    end

    def dummy_serve
      begin
        loop do 
          msg = gets.chomp
          puts send_and_get(msg)
        end
      rescue Interrupt => _
        puts "Bye."
      end
    end
  end
end

if __FILE__ == $0
  CrowdComm::ByteClient.new('tcp://localhost:6566').dummy_serve 
end
