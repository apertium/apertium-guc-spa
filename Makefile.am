#	cg-comp apertium-guc-spa.$(PREFIX2).rlx $(PREFIX2).rlx.bin

LANG1=guc
LANG2=spa
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)
BASENAME=apertium-$(PREFIX1)

TARGETS_COMMON=$(PREFIX2).autobil.bin $(PREFIX2).autogen.bin $(PREFIX2).autolex.bin $(PREFIX2).automorf.bin $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin $(PREFIX2).mode $(PREFIX2).prob

CLEANFILES = -rf $(TARGETS_COMMON) modes


$(PREFIX1).autobil.bin: apertium-guc-spa.guc-spa.dix
	apertium-validate-dictionary apertium-guc-spa.guc-spa.dix
	lt-comp lr apertium-guc-spa.guc-spa.dix $(PREFIX2).autobil.bin

$(PREFIX2).autobil.bin: apertium-guc-spa.guc-spa.dix
	apertium-validate-dictionary apertium-guc-spa.guc-spa.dix
	lt-comp rl apertium-guc-spa.guc-spa.dix $(PREFIX2).autobil.bin

$(PREFIX2).automorf.bin: apertium-guc-spa.spa.dix
	apertium-validate-dictionary apertium-guc-spa.spa.dix
	lt-comp lr apertium-guc-spa.spa.dix $(PREFIX2).automorf.bin apertium-guc-spa.spa.acx

$(PREFIX2).autogen.bin: apertium-guc-spa.guc.dix
	apertium-validate-dictionary apertium-guc-spa.guc.dix
	lt-comp rl apertium-guc-spa.guc.dix $(PREFIX2).autogen.bin

$(PREFIX2).autolex.bin: apertium-guc-spa.$(PREFIX2).lrx
	lrx-comp apertium-guc-spa.$(PREFIX2).lrx $(PREFIX2).autolex.bin

$(PREFIX2).t1x.bin: apertium-guc-spa.$(PREFIX2).t1x
	apertium-preprocess-transfer apertium-guc-spa.$(PREFIX2).t1x $(PREFIX2).t1x.bin

$(PREFIX2).t2x.bin: apertium-guc-spa.$(PREFIX2).t2x
	apertium-preprocess-transfer apertium-guc-spa.$(PREFIX2).t2x $(PREFIX2).t2x.bin

$(PREFIX2).t3x.bin: apertium-guc-spa.$(PREFIX2).t3x
	apertium-preprocess-transfer apertium-guc-spa.$(PREFIX2).t3x $(PREFIX2).t3x.bin

$(PREFIX2).mode: modes.xml
	apertium-gen-modes modes.xml
	cp *.mode modes/

apertium_guc_spa_DATA=$(TARGETS_COMMON)
apertium_guc_spadir=$(prefix)/share/apertium/apertium-$(PREFIX1)/
apertium_guc_spa_modesdir=$(prefix)/share/apertium/modes/

EXTRA_DIST=$(BASENAME).$(LANG1).dix \
  	   $(BASENAME).$(LANG2).dix \
           $(BASENAME).$(PREFIX2).lrx \
	   $(BASENAME).$(PREFIX1).dix \
           $(PREFIX2).prob \
	   $(BASENAME).$(PREFIX2).t1x \
	   $(BASENAME).$(PREFIX2).t2x \
	   $(BASENAME).$(PREFIX2).t3x \
	   modes.xml 

install-data-local:
	mv modes modes.bak
	apertium-gen-modes modes.xml apertium-$(PREFIX1)
	rm -rf modes
	mv modes.bak modes
	test -d $(DESTDIR)$(apertium_ht_modesdir) || mkdir $(DESTDIR)$(apertium_guc_spa_modesdir)
	$(INSTALL_DATA) $(PREFIX2).mode $(DESTDIR)$(apertium_guc_spa_modesdir)
	rm $(PREFIX2).mode 
	$(INSTALL_DATA) $(BASENAME).$(PREFIX2).t1x $(DESTDIR)$(apertium_guc_spadir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX2).t2x $(DESTDIR)$(apertium_guc_spadir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX2).t3x $(DESTDIR)$(apertium_guc_spadir)

