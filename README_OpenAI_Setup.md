# 🚀 Como Hospedar seu Assistente de Pitch no GitHub Pages

## 📋 O que você tem agora:
- ✅ Site modificado para usar a **OpenAI API** ao invés do Gemini
- ✅ Arquivo: `factorial-pitch-assistant.html`
- ✅ Funciona perfeitamente no GitHub Pages

## 🔧 Passo a Passo para Configurar:

### 1. **Configurar sua Chave da OpenAI**
1. Abra o arquivo `factorial-pitch-assistant.html`
2. Encontre a linha 239: `const apiKey = "SUA_CHAVE_OPENAI_AQUI";`
3. Substitua `SUA_CHAVE_OPENAI_AQUI` pela sua chave real da OpenAI
4. Salve o arquivo

### 2. **Criar Repositório no GitHub**
1. Vá para [github.com](https://github.com) e faça login
2. Clique em **"New repository"** (botão verde)
3. Nome do repositório: `factorial-pitch-assistant` (ou qualquer nome que quiser)
4. Marque **"Public"** (importante para GitHub Pages gratuito)
5. Clique **"Create repository"**

### 3. **Fazer Upload do Arquivo**
1. No seu repositório novo, clique em **"uploading an existing file"**
2. Arraste o arquivo `factorial-pitch-assistant.html` para a área de upload
3. Renomeie o arquivo para `index.html` (importante!)
4. Clique **"Commit changes"**

### 4. **Ativar GitHub Pages**
1. No seu repositório, vá em **"Settings"** (aba no topo)
2. Role para baixo até **"Pages"** (menu lateral esquerdo)
3. Em **"Source"**, escolha **"Deploy from a branch"**
4. Em **"Branch"**, escolha **"main"** e **"/ (root)"**
5. Clique **"Save"**
6. Aguarde alguns minutos para o site ficar online

### 5. **Acessar seu Site**
- Seu site estará disponível em: `https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO`
- Exemplo: `https://victo.github.io/factorial-pitch-assistant`

## 🔒 Segurança da API Key:

**⚠️ ATENÇÃO:** Sua chave da OpenAI ficará visível no código!

### Opções para proteger:
1. **Usar variáveis de ambiente** (mais avançado)
2. **Criar um backend** que esconda a chave
3. **Para testes simples:** Deixar como está (não recomendado para produção)

## 🎯 Como Usar:
1. Acesse seu site no GitHub Pages
2. Digite um tópico de pitch na caixa de texto
3. Escolha o tom desejado
4. Clique em **"Gerar Pitch ✨"**
5. A IA da OpenAI criará conteúdo personalizado!

## 🛠️ Personalizações Possíveis:
- Mudar cores e design
- Adicionar mais campos de entrada
- Modificar o prompt da IA
- Adicionar mais funcionalidades

## ❓ Precisa de Ajuda?
Se tiver dúvidas em qualquer passo, me avise! Estou aqui para ajudar. 😊
