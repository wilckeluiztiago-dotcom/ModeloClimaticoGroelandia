
import sys
import os
import numpy as np
import logging

# Configurar logger global para reduzir spam
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("GRESM")
logger.setLevel(logging.ERROR)

# Adicionar diretorio atual ao path
sys.path.append(os.getcwd())

# Importar Modulos (Caminhos em Português)
from GRESM.dinamica_central.solvedor_stokes import SolvedorStokes
from GRESM.dinamica_central.conservacao_massa import ConservacaoMassa
from GRESM.dinamica_central.reologia_glen import ReologiaGlen
from GRESM.dinamica_central.calculadora_viscosidade import CalculadoraViscosidade
from GRESM.processos_superficie.smb_acumulo import SmbAcumulo
from GRESM.processos_superficie.smb_ablacao import SmbAblacao
from GRESM.condicoes_contorno.acoplador_atmosfera import AcopladorAtmosfera
from GRESM.condicoes_contorno.leitor_topografia import LeitorTopografia
from GRESM.condicoes_contorno.forcante_nivel_mar import ForcanteNivelMar
from GRESM.geosfera_posglacial.gia_viscoelastico import GiaViscoelastico

class SimulacaoGRESM:
    def __init__(self):
        self.tempo_total = 200 # anos
        self.dt = 1.0 # passo de tempo
        self.anos = np.arange(0, self.tempo_total, self.dt)
        
        # Inicializacao
        self.topo = LeitorTopografia()
        self.x, self.leito, self.superficie = self.topo.carregar_dados()
        self.espessura = self.superficie - self.leito
        
        # Sistemas
        self.stokes = SolvedorStokes()
        self.mass = ConservacaoMassa()
        self.glen = ReologiaGlen()
        self.visc = CalculadoraViscosidade()
        
        self.smb_acc = SmbAcumulo()
        self.smb_abl = SmbAblacao()
        self.atmos = AcopladorAtmosfera()
        self.gia = GiaViscoelastico()
        self.sl = ForcanteNivelMar()

        # Armazenamento de Resultados
        self.historico = {
            'ano': [], 'vol_total': [], 'sl_contrib': [], 'temp_atmos': [], 
            'smb_medio': [], 'gia_max': [], 'vel_max': [], 'leito_medio': []
        }
        self.perfis_finais = {}

    def rodar(self):
        print("Iniciando Simulação GRESM (Arquitetura em Português)...")
        
        for t in self.anos:
            # 1. Forcantes Climáticos
            temp_ar = self.atmos.obter_temp_atmosfera(t, cenario_aquecimento=2.0)
            nivel_mar = self.sl.nivel_eustatico(t)
            
            # 2. SMB (Balanço de Massa)
            precip = self.smb_acc.calcular_precipitacao(t)
            # Ajuste simples de temperatura por altitude
            lapse_rate = 0.0065
            temp_local = temp_ar - lapse_rate * self.superficie
            derretimento = np.array([self.smb_abl.calcular_derretimento(tmp) for tmp in temp_local])
            balanco = precip - derretimento
            
            # 3. Dinâmica do Gelo
            # Gradiente de superificie
            declividade = np.gradient(self.superficie, self.x)
            # Velocidade (SIA)
            velocidade = self.stokes.resolver_velocidade(self.espessura, declividade)
            fluxo = velocidade * self.espessura
            div_fluxo = np.gradient(fluxo, self.x)
            
            # Evolução da massa
            self.espessura = self.mass.evoluir_espessura(self.espessura, div_fluxo, balanco, self.dt)
            self.superficie = self.leito + self.espessura
            
            # 4. Geossfera (GIA)
            carga = np.mean(self.espessura) * 917.0 * 9.81
            erguimento = self.gia.calcular_erguimento(t, carga)
            self.leito += erguimento * 1e-4 # Efeito pequeno incremental
            
            # Log
            self.historico['ano'].append(t)
            self.historico['vol_total'].append(np.sum(self.espessura) * (self.x[1]-self.x[0]))
            self.historico['temp_atmos'].append(temp_ar)
            self.historico['smb_medio'].append(np.mean(balanco))
            self.historico['gia_max'].append(erguimento)
            self.historico['vel_max'].append(np.max(np.abs(velocidade)))
            self.historico['leito_medio'].append(np.mean(self.leito))
            
            if int(t) % 20 == 0:
                print(f"Ano {int(t)}: Vol={self.historico['vol_total'][-1]:.2e} m2")

        # Salvar estado final
        self.perfis_finais = {
            'x': self.x,
            'superficie': self.superficie,
            'leito': self.leito,
            'espessura': self.espessura,
            'velocidade': velocidade,
            'smb': balanco
        }
        
        np.savez("resultados_gresm.npz", 
                 historico=self.historico, 
                 perfis_finais=self.perfis_finais)
        print("Simulação concluída. Dados salvos em 'resultados_gresm.npz'.")

if __name__ == "__main__":
    sim = SimulacaoGRESM()
    sim.rodar()
