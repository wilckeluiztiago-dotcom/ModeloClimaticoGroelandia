# GRESM - Greenland Regional Earth System Model

**Architect:** Luiz Tiago Wilcke  
**Version:** 1.0

## Visão Geral
O **GRESM** é um modelo de 50 módulos projetado para simular a dinâmica do manto de gelo da Groenlândia e suas interações com o sistema terrestre regional. Este repositório contém a arquitetura modular completa, preparada para implementações de alta fidelidade (Full Stokes, Glen's Law, Termodinâmica Polifásica).

## Estrutura do Sistema

O sistema é dividido em 5 clusters principais:

1.  **Core Dynamics (`core_dynamics/`)**: 15 módulos responsáveis pela física do fluxo de gelo (Stokes, reologia, conservação de massa).
2.  **Surface Processes (`surface_processes/`)**: 10 módulos para balanço de massa superficial (SMB) e hidrologia.
3.  **Boundary Conditions (`boundary_conditions/`)**: 10 módulos de acoplamento oceano-atmosfera e forçantes climáticas.
4.  **Geosphere & Post-Glacial (`geosphere_postglacial/`)**: 8 módulos focados em Ajuste Isostático Glacial (GIA) e pedogênese.
5.  **Infrastructure (`infrastructure/`)**: 7 módulos de suporte (I/O, logs, controle de tempo).

## Instalação e Uso
O projeto é estruturado em Python para orquestração.
```bash
# Exemplo de execução (futura)
python3 -m GRESM.infrastructure.main_driver
```

## Status
Atualmente, apenas a arquitetura (scaffolding) e a documentação de design foram implementadas. Os módulos contêm interfaces definidas mas sem lógica de cálculo implementada.
