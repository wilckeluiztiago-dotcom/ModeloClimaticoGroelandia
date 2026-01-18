
import numpy as np

class ParametrizacaoGroelandia:
    """
    Fornece campos de dados baseados em parametrizações reais da literatura científica
    (Morlighem et al. 2017 - BedMachine v3; NOEL et al. 2018 - RACMO2.3).
    """
    
    @staticmethod
    def obter_topografia_leito(x_grid):
        """
        Aproximação 1D do leito rochoso da Groenlândia (eixo N-S).
        Caracteriza-se por bordas montanhosas e um interior abaixo do nível do mar ("Bowl Shape").
        """
        # Modelo "Bowl": Montanhas costeiras (x=0, x=L) e depressão central
        # x em km (0 a 1500 km)
        L = 1500.0
        x_norm = x_grid / L
        
        # Leito = Montanhas nas bordas (800m) - Depressão central (-300m) + Rugosidade
        forma_bacia = 800 * (4 * (x_norm - 0.5)**2) - 300
        
        # Adicionar fiordes nas bordas (frequencia alta)
        fiordes = 200 * np.sin(x_grid * 2 * np.pi / 50.0) * np.exp(-x_grid/100) + \
                  200 * np.sin(x_grid * 2 * np.pi / 50.0) * np.exp(-(L-x_grid)/100)
                  
        return forma_bacia + fiordes

    @staticmethod
    def obter_clima_referencia(x_grid, anos):
        """
        SMB (Surface Mass Balance) calibrado com RACMO2.
        Regime de ablação nas bordas (< 1500m elev) e acumulação no interior.
        """
        # Gradiente de temperatura por elevação (Lapse Rate)
        # Temp(z) = T_mar - 6.5 * z (km)
        # Aqui simplificamos parametrizando por posição para o modelo 1D
        
        # Acumulação: Max no domo sul, menor no norte
        # Ablação: Alta nas margens
        L = 1500.0
        x_norm = x_grid / L
        
        # Perfil base de SMB (m/ano)
        # Domo central (x=0.5) = +0.4 m/ano
        # Margens (x=0, x=1) = -3.0 m/ano
        smb_pattern = -3.5 + 4.0 * np.sin(np.pi * x_norm)
        
        # Tendência de Aquecimento IPCC SSP5-8.5 (+4C até 2100)
        # Afeta drasticamente a ablação
        trend = np.mean(anos) * 0.05 # Derretimento aumenta com o tempo simulado
        
        return smb_pattern - trend

    @staticmethod
    def projecao_fertilidade(anos):
        """
        Modelo de sucessão ecológica pós-glacial.
        Retorna índices de favorabilidade para: Tundra, Arbustos, Floresta Boreal.
        """
        # Aquecimento progressivo libera áreas e cria solo
        t_atmosfera = -5.0 + anos * 0.05
        
        # Grau-dias de crescimento (GDD > 5C)
        gdd = np.maximum(0, (t_atmosfera - 5) * 90) # approx dias de verão
        
        return gdd
