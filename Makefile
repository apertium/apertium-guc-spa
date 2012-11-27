all:
	apertium-validate-dictionary apertium-guc-spa.guc-spa.dix
	lt-comp lr apertium-guc-spa.guc-spa.dix spa-guc.autobil.bin
	lt-comp rl apertium-guc-spa.guc-spa.dix spa-guc.autobil.bin
	apertium-validate-dictionary apertium-guc-spa.spa.dix
	lt-comp lr apertium-guc-spa.spa.dix spa-guc.automorf.bin apertium-guc-spa.spa.acx
	lt-comp rl apertium-guc-spa.guc.dix spa-guc.autogen.bin
#	cg-comp apertium-guc-spa.spa-guc.rlx spa-guc.rlx.bin
	lrx-comp apertium-guc-spa.spa-guc.lrx spa-guc.autolex.bin
	apertium-preprocess-transfer apertium-guc-spa.spa-guc.t1x spa-guc.t1x.bin
	apertium-preprocess-transfer apertium-guc-spa.spa-guc.t1x spa-guc.t2x.bin
	apertium-preprocess-transfer apertium-guc-spa.spa-guc.t3x spa-guc.t3x.bin
	apertium-gen-modes modes.xml
