# FIAP IA4Devs - Tech Challenge 5 - Detecção de materiais cortantes

![YOLOv11 Detecção de Facas](https://img.shields.io/badge/YOLOv11-Detecção_de_Facas-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv11-green)

## Grupo 23

### Integrantes

- **Gabriel Milanezi Teixeira** - RM 357208
- **João Vitor Marostica Mamprin** - RM 357209
- **Josenildo Camilo da Silva Junior** - RM 357563
- **Rogerio Luis Rocamoras Alves** - RM 357764

## Sobre o Projeto

Este projeto implementa um sistema de detecção de materiais cortantes (facas) em imagens e vídeos utilizando o modelo YOLOv11. O sistema é capaz de identificar facas em tempo real, gerar relatórios detalhados das detecções e enviar alertas quando facas são identificadas.

O sistema foi desenvolvido como solução para o Tech Challenge 5 da pós-graduação FIAP IA4Devs, com foco em aplicações práticas de visão computacional para segurança.

## Características Principais

- **Detecção de Facas:** Utiliza o modelo YOLOv11 treinado especificamente para identificar facas em imagens e vídeos
- **Processamento em Tempo Real:** Capacidade de analisar vídeos e imagens com alta performance
- **Sistema de Alertas:** Envia notificações quando facas são detectadas
- **Relatórios Detalhados:** Gera summaries completos das detecções tanto para imagens quanto para vídeos

## Estrutura do Projeto

```
.
├── dataset/                  # Dataset para treinamento e teste
│   ├── data.yaml             # Configuração do dataset
│   ├── test/                 # Imagens e labels de teste
│   ├── train/                # Imagens e labels de treinamento
│   └── valid/                # Imagens e labels de validação
├── videos/                   # Vídeos para análise
├── output_videos/            # Vídeos processados com detecções
├── runs/                     # Artefatos de treinamento e detecção
├── modelv11.ipynb            # Notebook principal com todo o código
├── yolo11n.pt                # Modelo pré-treinado do YOLOv11
├── summary_test_images.txt   # Resumo de detecções nas imagens de teste
└── summary_videos.txt        # Resumo de detecções nos vídeos
```

## Pré-requisitos

- Python 3.8 ou superior
- CUDA compatível (recomendado para aceleração por GPU)
- Dependências listadas abaixo

### Dependências

```
torch>=2.0.0
torchvision>=0.15.0
ultralytics>=0.8.0
numpy>=1.24.0
matplotlib>=3.7.0
requests>=2.31.0
Pillow>=9.5.0
```

Para instalar o PyTorch com suporte a CUDA:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Para as demais dependências:

```bash
pip install ultralytics numpy matplotlib requests Pillow
```

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd <nome-pasta>
   ```

2. **Descompacte o dataset:**

   Antes de executar o projeto, é necessário descompactar o arquivo `dataset.zip` na pasta raiz do projeto. Isso disponibilizará a estrutura completa de dados necessária para treinamento e teste.

   ```bash
   unzip dataset.zip
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

   Ou instale manualmente conforme seção de dependências acima.

4. **Preparação do ambiente:**
   - Certifique-se que o dataset está disponível na pasta `dataset/`
   - Coloque os vídeos para análise na pasta `videos/`
   - Garanta que o modelo pré-treinado YOLOv11 (`yolo11n.pt`) está no diretório raiz

5. **Execute o notebook:**
   - Abra o notebook `modelv11.ipynb` em um ambiente Jupyter
   - Execute as células sequencialmente

6. **Para treinar o modelo:**
   - Execute as células relacionadas ao treinamento para personalizar o modelo
   - O modelo treinado será salvo em `runs/train/yolov11_knife_detection/weights/best.pt`

7. **Para testar em imagens e vídeos:**
   - Execute as células de teste com imagens para visualizar as detecções
   - Execute as células de processamento de vídeo para análise de vídeos

8. **Para gerar relatórios:**
   - Execute a célula final para gerar os relatórios `summary_test_images.txt` e `summary_videos.txt`

9. **Sistema de alertas:**
   - Configure o e-mail de destino e a URL do webhook na célula apropriada
   - Descomente a linha de envio de alerta para ativar o sistema

## Estrutura dos Relatórios

### Relatório de Vídeos (summary_videos.txt)

Para cada vídeo processado, o relatório inclui:

```
Video 1: nome-do-video.mp4
- Número de frames analisados: X
- Número de frames onde facas foram detectadas: Y
- Número de frames sem facas: Z
- Número total de facas detectadas: W
```

### Relatório de Imagens (summary_test_images.txt)

Para o conjunto de imagens de teste:

```
Das X imagens testadas, foram encontradas facas em Y imagens, totalizando Z facas detectadas.
Em W imagens, nenhuma faca foi encontrada.
```

## Resultados

O modelo treinado atinge métricas competitivas na detecção de facas:

- Precision (Precisão): Capacidade do modelo de evitar falsos positivos
- Recall (Revocação): Capacidade do modelo de encontrar todas as facas
- mAP@0.5: Mean Average Precision com limiar de IoU (Intersection over Union) de 0.5
- mAP@0.5-0.95: Mean Average Precision com limiar de IoU variando de 0.5 a 0.95
