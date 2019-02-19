PROTOSOURCE = $(wildcard *.proto)
PROTORB = $(addprefix ruby/, \
	$(addsuffix _pb.rb, $(basename $(PROTOSOURCE)) ) )
PROTOCS = $(addprefix cs/, \
	$(addsuffix .cs, $(basename $(PROTOSOURCE)) ) )


$(PROTORB): $(PROTOSOURCE)
	-protoc $^ --ruby_out=ruby

$(PROTOCS): $(PROTOSOURCE)
	-protoc $^ --csharp_out=cs

all: ruby cs

ruby: $(PROTORB)

cs: $(PROTOCS)


clean: 
	@echo
	-rm $(PROTORB)

.PHONY:
	all clean ruby cs
