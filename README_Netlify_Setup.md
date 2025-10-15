# 🚀 Como Hospedar no Netlify (Solução CORS)

## 📋 **Arquivos Criados:**
- ✅ `netlify.toml` - Configuração do Netlify
- ✅ `netlify/functions/openai-proxy.js` - Função serverless para OpenAI
- ✅ `index.html` - Site modificado para usar Netlify

## 🔧 **Passo a Passo para Deploy:**

### 1. **Criar Conta no Netlify**
1. Vá para [netlify.com](https://netlify.com)
2. Clique em **"Sign up"**
3. Escolha **"Sign up with GitHub"** (mais fácil)
4. Autorize o Netlify a acessar seus repositórios

### 2. **Fazer Deploy do Repositório**
1. No Netlify, clique em **"New site from Git"**
2. Escolha **"GitHub"**
3. Selecione o repositório **"factorialfinance"**
4. Clique **"Deploy site"**

### 3. **Configurar Variáveis de Ambiente (Opcional)**
1. No Netlify, vá em **"Site settings"**
2. Clique em **"Environment variables"**
3. Adicione: `OPENAI_API_KEY` = sua chave da OpenAI
4. (Isso esconde a chave do código)

### 4. **Acessar seu Site**
- Seu site estará em: `https://SEU_SITE_NAME.netlify.app`
- Exemplo: `https://factorialfinance.netlify.app`

## 🎯 **Vantagens do Netlify:**
- ✅ **Resolve CORS** automaticamente
- ✅ **Gratuito** para projetos pessoais
- ✅ **Deploy automático** quando você faz push no GitHub
- ✅ **HTTPS** automático
- ✅ **CDN global** (site rápido no mundo todo)

## 🔒 **Segurança:**
- A chave da OpenAI está **no código** (não ideal para produção)
- Para produção, use **variáveis de ambiente** do Netlify
- Ou crie uma chave específica para este projeto

## 🚀 **Deploy Automático:**
- Toda vez que você fizer `git push` no GitHub
- O Netlify **automaticamente** atualiza o site
- Sem necessidade de fazer upload manual

## ❓ **Precisa de Ajuda?**
Se tiver dúvidas em qualquer passo, me avise! 😊
