import pygame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.botao import redimensionar

def tela_cadastro(largura_tela, altura_tela):
	#configuraçao do texto
	fonte_titulo = pygame.font.Font(None, 48)
	cor_titulo = (255, 255, 255)
	mensagem = "Pedra, papel,Tesoura"

	#configuraçao do botao
	fonte_botao = pygame.font.Font(None, 36)
	cor_texto = (255, 255, 255)
	cor_borda = (0, 0, 0)
	cor_gradiente1 = (0, 76, 153)
	cor_gradiente2 = (100, 149, 237)
	borda_arrendondada = 10

	#configurações iniciais
	texto_botoes = [
	{"botao":"Voltar", "acao": lambda: voltar_tela_inicial()},
	]
	largura_botao = 200
	altura_botao = 60
	espacamento = 10

	botoes = redimensionar(len(texto_botoes), largura_botao, altura_botao, espacamento, largura_tela, altura_tela)
	return mensagem, fonte_titulo, cor_titulo, texto_botoes, botoes, fonte_botao, cor_texto, cor_borda, cor_gradiente1, cor_gradiente2, borda_arrendondada 
relogio = pygame.time.Clock()

def voltar_tela_inicial():
	from main import trocar_tela, tela_inicial
	trocar_tela(tela_inicial())	