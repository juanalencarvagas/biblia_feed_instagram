# PROMPT MESTRE — BÍBLIA FEED 4.0

## 1. Objetivo do projeto

Quero criar, manter e evoluir um aplicativo chamado **Bíblia Feed**, desenvolvido em Python, com uma interface web inspirada no Instagram.

O propósito é proporcionar uma experiência de leitura bíblica agradável, moderna e visualmente envolvente, simulando a navegação pelo feed do Instagram.

O usuário deve conseguir ler a Bíblia continuamente, rolando a página, encontrando publicações com layouts variados, como acontece em uma rede social.

**Importante:** o aplicativo não será uma rede social real. É um leitor bíblico individual que utiliza a aparência e alguns padrões de interação de um feed social.

## 2. Arquitetura e tecnologias

O aplicativo deve utilizar:

- Python 3 como servidor local.
- HTML5 para estruturar as páginas.
- CSS3 para layout, animações e responsividade.
- JavaScript puro para interações.
- LocalStorage para favoritos e preferências.
- JSON para armazenamento dos textos bíblicos.

Não utilizar Flask, Django, React ou bibliotecas externas obrigatórias.

O programa deve funcionar com o comando:

```bash
python3 app.py
```

O servidor deverá iniciar no endereço `http://127.0.0.1:8765` e abrir automaticamente no navegador.

Organização sugerida:

```text
biblia_feed/
├── app.py
├── index.html
├── style.css
├── app.js
├── README.md
├── assets/
│   ├── personagens/
│   ├── imagens/
│   └── backgrounds/
├── almeida-livre.json
└── kjv.json
```

Os arquivos JSON bíblicos podem ser baixados automaticamente na primeira execução.

## 3. Layout principal — Instagram Web

Utilizar um design dark mode, inspirado na organização visual do Instagram Web, mas com identidade própria.

### Menu lateral esquerdo

Barra fixa com o nome Bíblia Feed e as opções: Início, Explorar, Descobrir, Plano de leitura, Salvos e Minha leitura. Usar ícones modernos e indicar a seção selecionada.

### Feed central

Uma coluna centralizada com largura aproximada de 500 a 600 pixels. Os posts devem aparecer verticalmente, um após o outro, com espaçamento semelhante ao Instagram.

Cada publicação deve ter:

1. Cabeçalho com avatar, nome de perfil temático e identificação da leitura.
2. Card visual com texto bíblico em português.
3. Botões para curtir, compartilhar e salvar.
4. Legenda e referência bíblica.
5. Tradução KJV em inglês no rodapé.

Não utilizar cards ocupando toda a altura da tela.

### Barra lateral direita

Simular sugestões de perfis bíblicos: João (Discípulo amado), Pedro (Apóstolo de Jesus), Rute (Exemplo de lealdade), Isaías (Profeta do Senhor), Débora (Juíza e profetisa) e Timóteo (Jovem na fé). Exibir avatares ilustrativos e um botão para acessar uma passagem relacionada.

### Stories superiores

Exibir retratos circulares de Moisés, Davi, Ester, Paulo, Maria e Daniel, com bordas em gradiente rosa, laranja e roxo. Ao clicar, abrir passagem relacionada ao personagem. Retratos são representações artísticas, não imagens históricas.

## 4. Regra principal — variedade visual dos posts

**O feed NÃO deve apresentar uma sequência de cards praticamente idênticos apenas com cores diferentes.** A experiência deve lembrar uma navegação real pelo Instagram, com identidades visuais distintas.

Implementar pelo menos seis modelos:

### Modelo 1 — Fotografia com versículo

Fotografia de paisagem (deserto, montanhas, Jerusalém, mar, floresta ou pôr do sol), com versículo branco sobre camada escura para legibilidade.

### Modelo 2 — Card editorial

Visual de revista ou livro: fundos claros, bege ou branco, tipografia elegante, margens amplas e elementos gráficos discretos.

### Modelo 3 — Carrossel bíblico

Post com três slides realmente navegáveis, divisão contextual da passagem e indicadores de slides. Manter a sequência correta dos versículos.

### Modelo 4 — Retrato bíblico

Imagem ilustrativa de personagem relacionada à passagem, combinada com texto em duas colunas ou sobreposição. Não associar personagens arbitrariamente.

### Modelo 5 — Colagem visual

Estilo scrapbook/diário visual com fotografias, texturas e o texto bíblico em composição própria.

### Modelo 6 — Post de destaque

Publicação gráfica com gradientes, tipografia forte e efeitos modernos, como post de campanha ou reflexão, mas preservando o texto bíblico.

### Regras de todos os modelos

- Preservar integralmente o texto selecionado, sem resumos ou alterações.
- Exibir referência exata (livro, capítulo e versículos).
- Evitar texto cortado e barras de rolagem internas; permitir altura variável.
- Variar de verdade composição, proporções, tipografia, espaçamento e imagens.
- Não repetir a mesma imagem em todos os posts.
- Permitir imagens externas com fallback local.
- Priorizar a leitura sobre o ornamento.

## 5. Traduções bíblicas

**Português:** Almeida Livre, domínio público, como texto principal. Fonte de referência: https://github.com/midvash/bible-data

**Inglês:** King James Version (KJV), edição em domínio público, no rodapé de cada publicação.

Formato:

**English comparison — KJV**

Texto correspondente em inglês.

Referência: Mark 7:14–15.

A KJV deve corresponder exatamente ao mesmo livro, capítulo e intervalo de versículos. Não apresentar tradução automática como se fosse a KJV. Se indisponível, informar sem impedir a leitura em português.

## 6. Navegação e funcionalidades

- Seleção entre os 66 livros e seus capítulos.
- Leitura em grupos de 1, 3 ou 5 versículos.
- Rolagem vertical contínua dentro do capítulo.
- Busca por palavras ou expressões.
- Curtidas e favoritos locais.
- Compartilhamento ou cópia de passagens.
- Ajuste do tamanho da fonte.
- Preferências guardadas no navegador.
- Stories e sugestões clicáveis.
- Layout responsivo.

**Não implementar anotações pessoais nem campos para escrever reflexões abaixo dos posts.** Essa funcionalidade foi removida por decisão do usuário.

Não simular comentários públicos reais nem apresentar estatísticas fictícias como reais.

## 7. Responsividade

**Desktop:** três regiões (menu esquerdo, feed central, sugestões direitas).

**Tablet:** priorizar feed e ocultar sugestões quando faltar espaço.

**Celular:** feed ocupando largura disponível, stories no topo, navegação inferior, cards adaptados e texto legível sem rolagem horizontal.

## 8. Performance e funcionamento

- Carregamento progressivo de posts e imagens (lazy loading).
- Fallback quando imagem externa falhar.
- Cache local dos textos bíblicos para leitura offline.
- Sem dependências desnecessárias.
- Compatibilidade com macOS, Windows e Linux.

## 9. Qualidade e validação

Antes de entregar:

1. Verificar sintaxe Python e JavaScript.
2. Testar endpoints locais e carregamento da Bíblia.
3. Conferir alinhamento da KJV com o texto em português.
4. Testar interações reais dos cards, especialmente o carrossel.
5. Conferir se os seis modelos são visualmente distintos.
6. Garantir que os versículos não estejam cortados.
7. Testar diferentes tamanhos de tela quando possível.
8. Informar quais testes foram executados e quais exigem validação manual.

Não considerar algo implementado apenas porque aparece visualmente.

## 10. Entrega

Gerar arquivo ZIP completo com código-fonte, recursos locais e instruções. Deve executar localmente em Python 3. Não entregar só mockup, protótipo estático ou código parcial.

## 11. Instruções para futuras alterações

Ao receber uma mudança:

- Usar a versão mais recente como base.
- Alterar somente o necessário.
- Preservar estilo e funcionalidades não afetadas.
- Nunca modificar o texto das Escrituras.
- Não substituir funcionalidades reais por simulações visuais.
- Entregar novo ZIP funcional.
- Descrever objetivamente o que mudou.

### NOVA ALTERAÇÃO SOLICITADA

[Descreva aqui o que deseja alterar, corrigir ou adicionar.]

Implemente a alteração no projeto existente, valide o resultado e entregue a nova versão completa em ZIP.


### Atualização v5.1
Mostrar a versão do aplicativo discretamente na interface, no rodapé da navegação e na visualização móvel. Todo post precisa ter imagem relacionada a uma palavra ou imagem do texto bíblico; escolher por tema semântico e utilizar ilustrações SVG locais como fallback offline. Não ilustrar passagens com retratos de personagens bíblicos sem associação textual justificável.
