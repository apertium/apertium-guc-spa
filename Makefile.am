###############################################################################
## Makefile for Wayuu--Spanish
###############################################################################

LANG1=guc
LANG2=spa
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)
BASENAME=apertium-$(PREFIX1)

TARGETS_COMMON =		\
	$(PREFIX1).automorf.bin	\
	$(PREFIX1).autobil.bin	\
	$(PREFIX1).autogen.bin	\
	$(PREFIX2).automorf.bin	\
	$(PREFIX2).prob		\
	$(PREFIX2).autobil.bin	\
	$(PREFIX2).autolex.bin	\
	$(PREFIX2).autogen.bin	\
	$(PREFIX2).t1x.bin	\
	$(PREFIX2).t2x.bin	\
	$(PREFIX2).t3x.bin

# This include defines goals for install-modes, .deps/.d, autobil.prefixes and .mode files:
@ap_include@

###############################################################################
## Monolingual transducers
###############################################################################

$(PREFIX2).automorf.bin: apertium-guc-spa.spa.dix
	apertium-validate-dictionary apertium-guc-spa.spa.dix
	lt-comp lr apertium-guc-spa.spa.dix $(PREFIX2).automorf.bin apertium-guc-spa.spa.acx

$(PREFIX2).autogen.bin: apertium-guc-spa.guc.dix
	apertium-validate-dictionary apertium-guc-spa.guc.dix
	lt-comp rl apertium-guc-spa.guc.dix $(PREFIX2).autogen.bin


###############################################################################
## Bilingual dictionaries
###############################################################################

$(PREFIX1).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $<
	lt-comp lr $< $@

$(PREFIX2).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $<
	lt-comp rl $< $@

###############################################################################
## Lexical selection rules
###############################################################################

$(PREFIX2).autolex.bin: $(BASENAME).$(PREFIX2).lrx
	lrx-comp $< $@


###############################################################################
## Structural transfer rules
###############################################################################


$(PREFIX2).t1x.bin: $(BASENAME).$(PREFIX2).t1x
	apertium-validate-transfer $<
	apertium-preprocess-transfer $< $@

$(PREFIX2).t2x.bin: $(BASENAME).$(PREFIX2).t2x
	apertium-validate-interchunk $<
	apertium-preprocess-transfer $< $@

$(PREFIX2).t3x.bin: $(BASENAME).$(PREFIX2).t3x
	apertium-validate-postchunk $<
	apertium-preprocess-transfer $< $@

###############################################################################
## Distribution
###############################################################################

EXTRA_DIST=					\
		$(BASENAME).$(PREFIX1).dix	\
		$(BASENAME).$(PREFIX2).lrx	\
		$(BASENAME).$(PREFIX2).t1x	\
		$(BASENAME).$(PREFIX2).t2x	\
		$(BASENAME).$(PREFIX2).t3x	\
		$(BASENAME).$(LANG1).dix	\
		$(BASENAME).$(LANG2).dix	\
		$(PREFIX2).prob			\
		modes.xml

###############################################################################
## Installation
###############################################################################

apertium_guc_spadir=$(prefix)/share/apertium/$(BASENAME)/

# Files which should be installed to $(prefix)/share/apertium/$(BASENAME)/:
apertium_guc_spa_DATA=	\
	$(TARGETS_COMMON)				\
	$(BASENAME).$(PREFIX2).t1x			\
	$(BASENAME).$(PREFIX2).t2x			\
	$(BASENAME).$(PREFIX2).t3x


# All modes are created by the same goal, listing several will just give problems with make -j2
noinst_DATA=modes/$(PREFIX1).mode

install-data-local: install-modes

###############################################################################
## Cleanup
###############################################################################

CLEANFILES = $(TARGETS_COMMON)
clean-local:
	-rm -rf .deps modes

###############################################################################
## Test
###############################################################################

test: all
	echo "house" | apertium -d . -f line guc-spa | tee .test-mt
	@echo "house" > .test-ref
	@diff .test-ref .test-mt
	echo "house" | apertium -d . -f line spa-guc | tee .test-mt
	@echo "house" > .test-ref
	@diff .test-ref .test-mt
	@rm .test-ref .test-mt
