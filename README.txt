CRIPTOGRAFIA COM RAIL FENCE

Este script usa o algoritmo RAIL FENCE para cifrar (proteger) e decifrar (desproteger) arquivos de texto. A criptografia transforma seu arquivo em um formato seguro, e a decifração reverte isso, recuperando o conteúdo original.

======================================================

O QUE VOCÊ VAI PRECISAR:

1. Python: Você precisa ter o Python instalado no seu computador. Caso não tenha, pode baixar e instalar a partir de https://www.python.org/downloads/.
   
2. Arquivo de Texto: O arquivo que você deseja cifrar ou decifrar deve ser um arquivo de texto simples, com a extensão '.txt' (por exemplo: 'meuarquivo.txt').

======================================================

PASSO A PASSO

======================================================
1. Baixando e Configurando o Script
======================================================

- Baixe o script main.py do repositório onde ele está salvo.
- Salve o arquivo do script em uma pasta de fácil acesso no seu computador.

======================================================
2. Preparando o Arquivo para Cifrar ou Decifrar
======================================================

- Tenha o arquivo de texto pronto (exemplo: 'meuarquivo.txt').
- Caso queira cifrar um arquivo, ele deve ser no formato '.txt'.
- Caso queira decifrar um arquivo, ele também deve ser no formato '.txt', mas ele precisa ter sido cifrado com o mesmo script.

======================================================
3. Rodando o Script
======================================================
Abra o terminal ou prompt de comando no seu computador (dependendo do sistema operacional que você usa).

1. Para Cifrar um Arquivo:
   - No terminal, navegue até a pasta onde o script e o arquivo estão.
   - Digite o seguinte comando, substituindo os valores:

     python main.py nome_arquivo.txt sua_chave criptografar

     - 'nome_arquivo.txt': Nome do arquivo que você quer cifrar (não se esqueça de usar a extensão '.txt').
     - 'sua_chave': Chave que você vai usar para cifrar o arquivo (pode ser qualquer palavra ou sequência de texto).
     - 'criptografar': Diga ao script que você quer criptografar o arquivo.

     Exemplo:
     
     python main.py texto.txt minhaSenha criptografar
     

     Isso criará um novo arquivo chamado 'texto_cifrado.txt'.

2. Para Decifrar um Arquivo:
   - Se você tiver um arquivo cifrado e quiser voltar ao formato original, use o seguinte comando:
     
     python main.py nome_arquivo_cifrado.txt sua_chave decriptografar
     
     - 'nome_arquivo_cifrado.txt': O arquivo que foi cifrado anteriormente (gerado pelo processo de criptografia).
     - 'sua_chave': A mesma chave que foi usada para cifrar o arquivo.
     - 'decriptografar': Diga ao script que você quer decifrar o arquivo.

     Exemplo:
     
     python main.py texto_cifrado.txt minhaSenha decriptografar
     

     Isso criará um novo arquivo chamado 'texto_decifrado.txt'.

======================================================
4. O Que Acontece Com os Arquivos?
======================================================
- Cifrar: Quando você cifrar um arquivo, ele será transformado em um formato que não pode ser lido facilmente, e o script cria um novo arquivo com o sufixo '_cifrado'.
  
- Decifrar: Quando você decifrar o arquivo, o conteúdo será restaurado para o formato original, e o script cria um novo arquivo com o sufixo '_decifrado'.

======================================================
5. O Que Você Precisa Saber?
======================================================

- Arquivo de Texto: O script funciona com arquivos de texto com a extensão'.txt'.
- Chave: A chave é uma sequência de texto que você escolhe. Ela deve ser a mesma tanto para cifrar quanto para decifrar.
- Sufixos dos Arquivos: O script cria novos arquivos com sufixos '_cifrado' ou '_decifrado' dependendo da operação realizada.

======================================================
6. Como Funciona a Criptografia?
======================================================

A criptografia Rail Fence é um método de transposição, que organiza o texto em várias "linhas" e depois lê o texto linha por linha para gerar a versão cifrada. Ao decifrar, o processo é revertido, usando a chave para reconstruir as linhas e recuperar o texto original.


======================================================

Problemas Comuns

- Arquivo não encontrado: Se você receber um erro de "arquivo não encontrado", verifique se o nome do arquivo e a extensão '.txt' estão corretos.
- Entrada inválida: Se o comando estiver errado (por exemplo, se não passar os parâmetros corretos), o script não funcionará. Certifique-se de seguir o formato correto de entrada.

