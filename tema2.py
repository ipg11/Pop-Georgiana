sir_articol='Nineta Talpoș are 22 ani, anul acesta a absolvit Facultatea de Drept din cadrul Universității „Lucian Blaga“ din Sibiu și se pregătește pentru susținerea examenului de admitere în Barou pentru a deveni avocat. Pentru Nineta, viața ei a fost mereu o balanță între școală și activitatea de la fermă. Crescând într-o familie dedicată creșterii animalelor, a fost influențată de această tradiție. În ferma familiei Talpoș din comuna Marpod, județul Sibiu, întâlnim un efectiv de aproximativ 700 de oi'
jumatate=len(sir_articol)//2
prima_parte=sir_articol[:jumatate]
a_doua_parte=sir_articol[jumatate:]
prima_parte=prima_parte.upper()
prima_parte=prima_parte.strip()
a_doua_parte=a_doua_parte[::-1]
a_doua_parte=a_doua_parte.capitalize()
semnele=('.',',','!')
a_doua_parte=a_doua_parte.replace[semnele]
rezultat=prima_parte+a_doua_parte