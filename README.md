# GRESM - Modelo do Sistema Terrestre Regional da Groenlândia

**Autor:** Luiz Tiago Wilcke   
**Versão:** 2.1.0

## Visão Geral
O **GRESM** (Greenland Regional Earth System Model) é um framework computacional avançado composto por 50 módulos independentes, projetado para simular a criosfera da Groenlândia com alta fidelidade física e numérica. O sistema integra dinâmica de fluxo de gelo (Full Stokes/SIA), balanço de massa superficial, hidrologia e geodinâmica (ajuste isostático glacial).

## Equações Governantes (Modelo Físico)

O núcleo do GRESM resolve as equações fundamentais da glaciologia e geofísica utilizando métodos numéricos avançados.

### 1. Conservação de Momento (Full Stokes)
A dinâmica do gelo é governada pelo equilíbrio de tensões (sendo $\sigma$ o tensor de tensão e $\mathbf{g}$ a gravidade):
$$ \nabla \cdot \sigma + \rho_i \mathbf{g} = 0 $$

### 2. Lei Constitutiva (Reologia de Glen)
O gelo comporta-se como um fluido não-newtoniano seguindo a lei de potência:
$$ \dot{\varepsilon}_{ij} = A(T) \tau^{n-1} \tau_{ij} $$
Onde $A(T)$ segue a relação de Arrhenius:
$$ A(T) = A_0 e^{-Q/RT} $$

### 3. Conservação de Massa
A evolução da espessura do gelo ($H$) depende da divergência do fluxo ($\mathbf{u}$) e do balanço de massa superficial ($SMB$):
$$ \frac{\partial H}{\partial t} + \nabla \cdot (H \mathbf{u}) = SMB - BMB $$

### 4. Termodinâmica
A evolução da temperatura ($T$) considera advecção, difusão e dissipação viscosa ($\Phi$):
$$ \rho c_p (\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T) = \nabla \cdot (k \nabla T) + \Phi $$

## Execução
Para rodar a simulação principal e gerar os produtos de saída:
```bash
python3 main_simulacao.py
```
Isso produzirá o arquivo de resultados `resultados_gresm.npz`.

## Visualização
Para gerar os 30 gráficos científicos e o Mapa da Groenlândia:
```bash
python3 gerador_graficos_30.py
```
Os arquivos serão salvos em `graficos_finais/`.
