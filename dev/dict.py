#!/usr/bin/python3
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy;


#<b>acompañante </b><i>n.m., n.f. </i>o'uyaajana.
#<b>abdomen </b><i>n.m. </i>ale'e.
#<b>abertura </b><i>n.f. </i>o'u1.
#<b>abierto, -ta </b><i>adj. </i>jutataa.
#<b>acuerdo </b><i>n.m. </i>(estar de acuerdo)
#<b>abogado, -da </b><i>n.m., n.f. </i>pütchipü'ü.
#<b>abrir </b><i>v.tr. </i>ajutalaa.
#<b>abuelo, -la </b><i>n.m. </i>atuushi, taata.
#<b>acción </b><i>n.f. </i>(mala) aainjala. <i>V. </i>hacer.
#<b>agua </b><i>n.f. </i>wüin. (sitio donde hay agua)
#<b>aguaitacamino </b>REG. <i>n.m. </i>(ave)
#<b>aceite </b><i>n.m. </i>seita, (comestible)
#<b>aguardiente </b><i>n.m. </i>chirinchi.
#<b>aguja </b><i>n.f. </i>wutia.
#<b>agujero </b><i>n.m. </i>o'u
#<b>amigo, -ga </b><i>n.m., n.f. </i>atünajutü, (para
#<b>aire </b><i>n.m. </i>jouktai.
#<b>ala </b><i>n.f. </i>atüna. (tener alas) katünaa.
#<b>amistad </b><i>n.f. </i>(tener amistad) aleewaa.
#
 
eslemma = '';
estags = ''
gulemma = '';
gucomment = '';
for line in open(sys.argv[1]).readlines(): #{
	if len(line) < 1: #{
		continue;
	#}
	line = line.replace('<b>', '');
	line = line.replace('<i>', '');
	line = line.replace('</b>', ';');
	line = line.replace('</i>', ':');
	line = line.strip();
	
	state = 0;
	for c in line: #{
		if c == '(': #{
			state = 3;
			continue;
		#}
		if c == ')': #{
			state = 2;
			continue;
		#}
		if c == ';': #{
			state = 1
			continue;
		#}
		if c == ':': #{
			state = 2;
			continue;
		#}

		if state == 3: #{
			gucomment = gucomment + c;
		#}
		if state == 0: #{
			eslemma = eslemma + c;
		#}
		if state == 1: #{
			estags = estags + c;
		#}
		if state == 2: #{
			gulemma = gulemma + c;
		#}
	#}	

	if eslemma.count(',') > 0: #{
		gucomment = gucomment + '| ' + eslemma;
		eslemma = eslemma.split(',')[0];
	#}
	
	genero = 'GD';
	if estags.count('m.') > 0: #{
		genero = 'm';
	elif estags.count('f.') > 0: #{
		genero = 'f';
	#}
	gulemma = gulemma.strip('. ');
	eslemma = eslemma.strip('. ');
	if gulemma.count(',') > 0: #{
		for sub in gulemma.split(','): #{
			if sub.strip() == '': #{
				continue;
			#}
			print('<e><p><l>' + sub.strip().replace(' ', '<b/>') + '<s n="n"/></l><r>' + eslemma.strip() + '<s n="n"/><s n="' + genero + '"/></r></p></e> <!-- ' + gucomment + ' -->');
#			print('%s ; %s ; %s ; %s' % (eslemma, estags, sub.strip(), gucomment));
		#}
	else: #{
		if gulemma.strip() == '': #{
			continue;
		#}
		print('<e><p><l>' + gulemma.strip().replace(' ', '<b/>') + '<s n="n"/></l><r>' + eslemma.strip() + '<s n="n"/><s n="' + genero + '"/></r></p></e> <!-- ' + gucomment + ' -->');
		#print('%s ; %s ; %s ; %s' % (eslemma, estags, gulemma, gucomment));
	#}

	eslemma = '';
	estags = '';
	gulemma = '';
	gucomment = '';
#}
