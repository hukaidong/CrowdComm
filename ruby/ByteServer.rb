require './Util'

module CrowdComm
  require 'ffi-rzmq'

  class ByteServer
    include ZMQ
    include CrowdComm::Utils

    def initialize(sockname)
      @context = Context.new(1)
      @pipe = @context.socket(REP)
      if got_error @pipe.bind(sockname)
        raise "Fail to listen on #{sockname}" 
      end
      puts "Listening on #{sockname}"
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

    def dummy_serve
      byte_decode = proc do |b|
        b.to_i
      end

      begin
        loop do
          msg = get_bytes
          send_bytes "I've got: #{msg}"
        end
      rescue Interrupt => e
        puts "\rServer shutting down..."
        @pipe.close
      end
    end
  end
end

if __FILE__ == $0
  CrowdComm::ByteServer.new('ipc:///tmp/sock_temp').dummy_serve
end
