import sys
from getpass import getpass

# Função de derivação de chave usando PBKDF2
def derivar_chave(senha, salt):
    from hashlib import pbkdf2_hmac
    chave = pbkdf2_hmac('sha256', senha.encode(), salt.encode(), 100000)
    return chave

# Função para criptografar usando Rail Fence
def rail_fence_encrypt(text, num_rails):
    rails = [''] * num_rails
    rail = 0
    direction = 1  # Direção da escrita (para baixo ou para cima)

    # Preenchendo as rails
    for char in text:
        rails[rail] += char
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # A junção das rails gera o texto cifrado
    return ''.join(rails)

# Função para descriptografar usando Rail Fence
def rail_fence_decrypt(text, num_rails):
    # Recria as rails vazias
    rails = [''] * num_rails
    rail = 0
    direction = 1
    # Preenche as rails com os caracteres do texto cifrado
    for i in range(len(text)):
        rails[rail] += '*'
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # Coloca os caracteres na posição correta
    idx = 0
    for i in range(num_rails):
        for j in range(len(rails[i])):
            rails[i] = rails[i][:j] + text[idx] + rails[i][j+1:]
            idx += 1

    # Lê o texto da matriz desenhada para obter o texto original
    result = []
    rail = 0
    direction = 1
    for i in range(len(text)):
        result.append(rails[rail][0])
        rails[rail] = rails[rail][1:]
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        print("Uso: python main.py <arquivo.txt> <chave> <criptografar|decriptografar>")
        sys.exit(1)

    arquivo = sys.argv[1]
    chave = sys.argv[2]
    acao = sys.argv[3].lower()

    # Validando ação
    if acao not in ['criptografar', 'decriptografar']:
        print("Ação inválida. Use 'criptografar' ou 'decriptografar'.")
        sys.exit(1)

    # Lê o conteúdo do arquivo
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            texto = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        sys.exit(1)

    # Deriva a chave e o salt
    salt = "somesaltvalue"  # O salt pode ser fixo ou aleatório
    chave_gerada = derivar_chave(chave, salt)

    # Criptografar ou descriptografar dependendo da ação
    if acao == 'criptografar':
        resultado = rail_fence_encrypt(texto, 3)  # Aqui 3 é o número de rails
        novo_nome = arquivo.replace(".txt", "_cifrado.txt")
    elif acao == 'decriptografar':
        resultado = rail_fence_decrypt(texto, 3)
        novo_nome = arquivo.replace("_cifrado.txt", "_decifrado.txt")

    # Salva o resultado no novo arquivo
    try:
        with open(novo_nome, 'w', encoding='utf-8') as file:
            file.write(resultado)
        print(f"Arquivo '{novo_nome}' salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    main()
