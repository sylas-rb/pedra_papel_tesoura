import pygame
import pygame_gui

def desenhar_gradiente(surface, cor1, cor2, rect):
	for y in range(rect.height):
		proporcao = y / rect.height
		r = int(cor1[0] * (1 - proporcao) + cor2[0] * proporcao)
		g = int(cor1[1] * (1 -  proporcao) + cor2[1] * proporcao)
		b = int(cor1[2] * (1 - proporcao) + cor2[2] * proporcao)
		pygame.draw.line(surface, (r,g,b), (rect.x, rect.y + y), (rect.x + rect.width, rect.y + y))
		
def desenhar_botao(surface, rect, texto, fonte, cor_texto, cor_borda, cor_gradiente1, cor_gradiente2, borda_arrendondada):
	botao_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
	pygame.draw.rect(botao_surface, cor_borda, botao_surface.get_rect(), border_radius=borda_arrendondada)
	gradiente_surface = pygame.Surface((rect.width - 4, rect.height - 4), pygame.SRCALPHA)
	desenhar_gradiente(gradiente_surface, cor_gradiente1, cor_gradiente2, gradiente_surface.get_rect())
	gradiente_mask = pygame.Surface((rect.width - 4, rect.height -4), pygame.SRCALPHA)
	pygame.draw.rect(gradiente_mask, (255, 255, 255), gradiente_mask.get_rect(), border_radius=borda_arrendondada - 2)
	gradiente_surface.blit(gradiente_mask, (0,0), special_flags=pygame.BLEND_RGBA_MIN)
	botao_surface.blit(gradiente_surface, (2, 2))
	surface.blit(botao_surface, rect.topleft)
	
	texto_renderizado = fonte.render(texto, True, cor_texto)
	texto_rect = texto_renderizado.get_rect(center=rect.center)
	surface.blit(texto_renderizado, texto_rect)
	
def redimensionar (quantidade, largura, altura, espacamento, largura_tela, altura_tela):
	botoes = []
	altura_total = quantidade * altura + (quantidade - 1) * espacamento
	y_inicial = altura_tela // 2 - altura_total // 2
	for i in range(quantidade):
		x = largura_tela // 2 - largura // 2
		y = y_inicial + i * (altura + espacamento)
		botoes.append(pygame.Rect(x,y, largura, altura))
	return botoes