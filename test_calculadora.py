import calculadora as calc

def test_soma_positivos():
    assert calc.soma(2, 3) == 5

def test_soma_negativos():
    assert calc.soma(-1, -5) == -6

def test_soma_misto():
    assert calc.soma(10, -2) == 8

def test_subtrai_positivos():
    assert calc.subtracao(10, 5) == 5

def test_subtrai_com_zero():
    assert calc.subtracao(5, 0) == 5
    
def test_multiplicacao_positivos():
	assert calc.multiplicacao(4, 5) == 20
     
def test_multiplicacao_por_zero():
    assert calc.multiplicacao(7, 0) == 0
    
def test_multiplicacao_negativos():
	assert calc.multiplicacao(-3, -6) == 18

def test_divisao_positivos():
	assert calc.divisao(10, 2) == 5
    
def test_divisao_por_zero():
	try:
		calc.divisao(5, 0)
		assert False, "Expected ValueError"
	except ValueError as e:
		assert str(e) == "Divisão por zero não é permitida."
            
def test_modulo_positivos():
	assert calc.modulo(10, 3) == 1

def test_modulo_negativos():
	assert calc.modulo(-10, 3) == 2