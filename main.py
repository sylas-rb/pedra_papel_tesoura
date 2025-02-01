import pygame
import pygame_gui
from utils.botao import desenhar_gradiente, desenhar_botao, redimensionar
from telas.cadastro import tela_cadastro

pygame.init()

info_tela = pygame.display.Info()
largura_tela = info_tela.current_w
altura_tela = info_tela.current_h

tela = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE)
pygame.display.set_caption("Pedra, Papel e Tesoura")	  
def tela_inicial():	
	#configuraçao do texto
	fonte_titulo = pygame.font.Font(None, 48)
	cor_titulo = (255, 255, 255)
	mensagem = "Pedra, papel,Tesoura"

	#configuraçao do botao
	botao_rect = pygame.Rect(largura_tela // 2 - 100, altura_tela // 2 - 25, 200, 60)
	fonte_botao = pygame.font.Font(None, 36)
	cor_texto = (255, 255, 255)
	cor_borda = (0, 0, 0)
	cor_gradiente1 = (0, 76, 153)
	cor_gradiente2 = (100, 149, 237)
	borda_arrendondada = 10

	#configurações iniciais
	texto_botoes = [
	{"botao":"jogar", "acao": lambda: print("Iniciar o jogo")},
	{"botao":"Estatística", "acao": lambda: print("Exibir estatísticas")},
	{"botao":"Entrar", "acao": lambda: trocar_tela(tela_cadastro(largura_tela, altura_tela))},
	]
	largura_botao = 200
	altura_botao = 60
	espacamento = 10

	botoes = redimensionar(len(texto_botoes), largura_botao, altura_botao, espacamento, largura_tela, altura_tela)
	return mensagem, fonte_titulo, cor_titulo, texto_botoes, botoes, fonte_botao, cor_texto, cor_borda, cor_gradiente1, cor_gradiente2, borda_arrendondada 
relogio = pygame.time.Clock()

tela_atual = tela_inicial()
def trocar_tela(nova_tela):
	global tela_atual
	tela_atual = nova_tela
play = True
while play:
	tempo_delta = relogio.tick(60) / 1000.0
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			play = False
		elif evento.type == pygame.VIDEORESIZE:
			largura_tela, altura_tela = evento.w, evento.h
			tela = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE)
			tela_atual = tela_inicial()
			botoes = redimensionar(len(texto_botoes), largura_botao, altura_botao, espacamento, largura_tela, altura_tela)	
		elif evento.type == pygame.MOUSEBUTTONDOWN:	
			posicao_mouse= pygame.mouse.get_pos()
			for i, botao_rect in enumerate(tela_atual[4]):
				if botao_rect.collidepoint(posicao_mouse):
					tela_atual[3][i]["acao"]()
		elif evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_ESCAPE:
				play = False
	tela.fill((0,0,0))
	mensagem, fonte_titulo, cor_titulo, texto_botoes, botoes, fonte_botao, cor_texto, cor_borda, cor_gradiente1, cor_gradiente2, borda_arrendondada = tela_atual
	texto_redenrizado = fonte_titulo.render(mensagem, True, cor_titulo)
	posicao_texto = texto_redenrizado.get_rect(center=(largura_tela // 2, altura_tela // 4))
	tela.blit(texto_redenrizado, posicao_texto)
	for i, botao in enumerate(botoes):
				texto_botao = texto_botoes[i]
				desenhar_botao(tela, botao, texto_botao["botao"], fonte_botao, cor_texto, cor_borda, cor_gradiente1, cor_gradiente2, borda_arrendondada)
	pygame.display.update()
pygame.quit()