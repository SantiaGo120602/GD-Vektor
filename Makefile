antlr4 = java -jar /usr/local/lib/antlr-4.11.1-complete.jar

build:
	$(antlr4) -Dlanguage=Python3 -visitor -no-listener GDV_Grammar.g4

testAll:
	python3 main.py test/test1_calculadora.GDV
	python3 main.py test/test2_guardar_tangente.GDV
	python3 main.py test/test3_graficar_datos.GDV

testCalculadora:
	python3 main.py test/test1_calculadora.GDV

testTangente:
	python3 main.py test/test2_guardar_tangente.GDV 

testGraficar:
	python3 main.py test/test3_graficar_datos.GDV 

clean:
	find . -maxdepth 1 -type f ! \( -name "Makefile" -o -name "main.py" -o -name "GDV_Grammar.g4" -o -name "MyVisitor.py" -o -name "error_manager.py" \) -exec rm -v {} +
