# GRESM - Modelo do Sistema Terrestre Regional da Groenlândia

**Autor:** Luiz Tiago Wilcke   
**Versão:** 2.1.0

## Visão Geral
O **GRESM** (Greenland Regional Earth System Model) é um framework computacional avançado composto por 50 módulos independentes, projetado para simular a criosfera da Groenlândia com alta fidelidade física e numérica. O sistema integra dinâmica de fluxo de gelo (Full Stokes/SIA), balanço de massa superficial, hidrologia e geodinâmica (ajuste isostático glacial).

### 1. Conservação de Momento (Full Stokes)
A dinâmica do gelo é governada pelo equilíbrio de tensões (sendo $\sigma$ o tensor de tensão e $\mathbf{g}$ a gravidade):

![Eq. Stokes](https://latex.codecogs.com/png.latex?\nabla\cdot\sigma+\rho_i\mathbf{g}=0)

### 2. Lei Constitutiva (Reologia de Glen)
O gelo comporta-se como um fluido não-newtoniano seguindo a lei de potência:

![Eq. Glen](https://latex.codecogs.com/png.latex?\dot{\varepsilon}_{ij}=A(T)\tau^{n-1}\tau_{ij})

Onde $A(T)$ segue a relação de Arrhenius:

![Eq. Arrhenius](https://latex.codecogs.com/png.latex?A(T)=A_0e^{-Q/RT})

### 3. Conservação de Massa
A evolução da espessura do gelo ($H$) depende da divergência do fluxo ($\mathbf{u}$) e do balanço de massa superficial ($SMB$):

![Eq. Massa](https://latex.codecogs.com/png.latex?\frac{\partial%20H}{\partial%20t}+\nabla\cdot(H\mathbf{u})=SMB-BMB)

### 4. Termodinâmica
A evolução da temperatura ($T$) considera advecção, difusão e dissipação viscosa ($\Phi$):

![Eq. Energia](https://latex.codecogs.com/png.latex?\rho%20c_p(\frac{\partial%20T}{\partial%20t}+\mathbf{u}\cdot\nabla%20T)=\nabla\cdot(k\nabla%20T)+\Phi)

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
