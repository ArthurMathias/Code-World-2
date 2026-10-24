from time import sleep
print('\n=== CADASTRO para entrar na Calculadora===')
print("-" * 20)
sleep(1)

# Cadastro do usuário
while True:
    usuario_cadastrado = input('Crie seu usuário: ')

    if not usuario_cadastrado.isalnum():
        print('Use apenas letras e números!')
    elif len(usuario_cadastrado) < 5:
        print('Nome muito curto! Mínimo de 5 caracteres.')
    else:
        print('Nome válido!')
        sleep(2)
        break

# Cadastro da senha
while True:
    senha_cadastrada = input('Crie sua senha: ')

    if not senha_cadastrada.isalnum():
        print('Use apenas letras e números!')
    elif len(senha_cadastrada) < 8:
        print('Senha muito curta! Mínimo de 8 caracteres.')
    else:
        print('Senha válida!')
        sleep(2)
        break

print('\nCadastro realizado com sucesso!')
print()

print('\n=== LOGIN ===')
sleep(2)
# Tentativas de login
tentativas = 3

while tentativas > 0:
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print('\nLogin realizado!')

        import calculadora
        break
    else:
        tentativas -= 1
        print(f'Usuário ou senha incorretos! Restam {tentativas} tentativa(s).')

if tentativas == 0:
    print('Número máximo de tentativas atingido!')
