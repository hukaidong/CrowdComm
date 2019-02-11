
module CrowdComm
  require 'ffi-rzmq'

  module Utils

    def got_error(rc)
      unless ZMQ::Util.resultcode_ok?(rc)
        STDERR.puts "Operation failed, errno [#{ZMQ::Util.errno}] description [#{ZMQ::Util.error_string}]"
        caller(1).each { |callstack| STDERR.puts(callstack) }
        return true
      end
      false
    end

  end
end
