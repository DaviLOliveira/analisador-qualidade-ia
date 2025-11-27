# 🔍 Analisador de Qualidade com Visão Computacional

Este projeto é uma aplicação Full Stack que utiliza Inteligência Artificial para detectar defeitos em materiais (como corrosão, trincas e fissuras) através de imagens.

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/AI-TensorFlow%20%7C%20Keras-orange)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)

## 📸 Demonstração

<img width="1079" height="1811" alt="screenshot" src="https://github.com/user-attachments/assets/be5f90a7-1ced-4e99-95a3-6cb96e3ef670" />



## 🚀 Funcionalidades

- **Upload de Imagem:** Interface amigável para envio de arquivos.
- **Preview em Tempo Real:** Visualização da imagem antes da análise.
- **Análise com IA:** Classificação automática utilizando Rede Neural Convolucional.
- **Feedback Visual:** Indicação clara de "Aprovado" (Verde) ou "Defeito" (Vermelho).
- **Múltiplas Classes:** Capaz de identificar: Limpo, Corrosão, Fissuras, Manchas, Trincas.

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla).
- **Backend:** Python, FastAPI.
- **IA/ML:** TensorFlow, Keras (Modelo treinado no Google Teachable Machine).
- **Processamento de Imagem:** Pillow, NumPy.

## 📦 Como rodar o projeto

### Pré-requisitos
- Python 3.11 instalado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/analisador-qualidade-ia.git](https://github.com/SEU-USUARIO/analisador-qualidade-ia.git)
   cd analisador-qualidade-ia
  
### 2. Crie e ative o ambiente virtual
É recomendável usar um ambiente virtual para isolar as dependências.

**No Windows:**
# Cria o ambiente usando Python 3.11
py -3.11 -m venv venv

# Ativa o ambiente
.\venv\Scripts\activate

3. Instale as dependências
Instale as versões exatas para evitar conflitos entre Numpy e TensorFlow.

Bash

pip install -r requirements.txt
4. Inicie o Backend (API)
Navegue até a pasta do servidor e inicie o Uvicorn.

Bash

cd backend
python -m uvicorn main:app --reload
O terminal deve exibir: ✅ Modelo carregado com sucesso! e o servidor rodará em http://127.0.0.1:8000.

5. Acesse o Frontend
Vá até a pasta frontend.

Dê um clique duplo no arquivo index.html para abrir no seu navegador padrão.

Envie uma imagem e teste!

🔧 Solução de Problemas Comuns
Erro ModuleNotFoundError: No module named 'tensorflow': Certifique-se de que está usando o Python 3.11. Versões mais recentes (3.12+) ainda podem ter incompatibilidade.

Erro de DLL: Se ocorrer erro de DLL ao importar o TensorFlow, instale o Microsoft Visual C++ Redistributable e reinicie o computador.

Conflito Keras/TensorFlow: Este projeto utiliza explicitamente a versão 2.15.0 para ambos os pacotes para garantir compatibilidade.
