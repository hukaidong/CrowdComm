PROTOSOURCE = $(wildcard *.proto)
PROTORB = $(addprefix ruby/, \
	$(addsuffix _pb.rb, $(basename $(PROTOSOURCE)) ) )


$(PROTORB): $(PROTOSOURCE)
	-protoc $^ --ruby_out=ruby

ruby: $(PROTORB)

all:


clean: 
	@echo
	-rm $(PROTORB)

.PHONY:
	all clean ruby
