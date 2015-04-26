# -*- coding: utf-8 -*-
preco = float(raw_input('Informe o preço do produto: '))
desconto = float(raw_input('Informe o percentual de desconto: '))
print 'O desconto foi de R$ %.2f' % (preco * desconto/100)
print 'O valor com desconto foi R$ %2.f' % (preco - (preco * desconto/100))
