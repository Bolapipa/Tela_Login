***Antes de começar o projeto lembre-se de ir ao CMD e digitar pip install customtkinter***
Este projeto demonstra como criar uma interface gráfica de login usando a biblioteca CustomTkinter, que oferece uma aparência moderna e personalizável.
Funcionalidades:
- Login básico: Verifica usuário e senha (valores fixos).
- Mostrar/ocultar senha: Permite alternar a visualização do campo de senha com um clique.
- Modo claro/escuro: Troca dinâmica entre temas com um botão.
- Feedback visual: Mensagens coloridas informam se o login foi bem-sucedido ou não.
É um ótimo exemplo para iniciantes que queiram aprender:
- Manipulação de eventos com botões;
- Interação com campos de entrada (Entry);
- Troca de temas e elementos gráficos.



![image](https://github.com/user-attachments/assets/80d120cc-8959-4b3a-94b6-106d6a5c5aef)


![image](https://github.com/user-attachments/assets/ab61ae94-06bf-417b-aea9-cdca31fbad93)













# Explicação do Código - Interface de Login com CustomTkinter

```python
import customtkinter as ctk              # Importa a biblioteca CustomTkinter para criar interfaces gráficas modernas
```

## Aparência inicial

```python
ctk.set_appearance_mode('dark')          # Define o tema inicial da interface como escuro (dark mode)
tema_escuro = True                       # Variável booleana para controlar o estado do tema
```

## Funções

### Validação do Login

```python
def validar_login():
    campo_usuario.get()                 # Captura o texto digitado no campo do usuário (linha redundante)
    usuario = campo_usuario.get()       # Armazena o valor digitado no campo de usuário
    senha = campo_senha.get()           # Armazena o valor digitado no campo de senha

    if usuario == 'Arthur' and senha == '123456':   # Verifica se os dados correspondem
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')  # Mensagem de sucesso
    else:
        resultado_login.configure(text='Login Incorreto', text_color='red')             # Mensagem de erro
```

### Mostrar/Ocultar Senha

```python
def toggle_senha():
    mostrar = campo_senha.cget('show') == '*'         # Verifica se o campo de senha está oculto com '*'
    campo_senha.configure(show='' if mostrar else '*')  # Alterna entre mostrar e ocultar a senha
    botao_toggle.configure(text='🙈' if mostrar else '🙉')  # Atualiza o ícone do botão
```

### Alterar Tema

```python
def toggle_tema():
    global tema_escuro                              # Usa a variável global para controle
    tema_escuro = not tema_escuro                   # Alterna o estado do tema
    ctk.set_appearance_mode('dark' if tema_escuro else 'light')  # Aplica o tema
    botao_tema.configure(text='White' if tema_escuro else 'Dark')  # Atualiza o texto do botão
```

## Janela Principal

```python
app = ctk.CTk()                        # Cria a janela principal da aplicação
app.title('Área de Login')            # Define o título da janela
app.geometry('500x500')               # Define o tamanho da janela
```

## Campos de Entrada

```python
label_usuario = ctk.CTkLabel(app, text='Usuário')  # Label para o campo do usuário
label_usuario.pack(pady=10)                        # Adiciona espaçamento ao redor

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')  # Campo para digitar o usuário
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text='Senha')      # Label para o campo de senha
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')  # Campo de senha com ocultação
campo_senha.pack(pady=10)
```

## Botão para Mostrar/Ocultar Senha

```python
botao_toggle = ctk.CTkButton(app, text='🙉', width=40, command=toggle_senha)  # Botão que alterna visibilidade da senha
botao_toggle.pack(pady=(0,10))
```

## Botão de Login

```python
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)  # Botão para efetuar login
botao_login.pack(pady=10)
```

## Feedback de Login

```python
resultado_login = ctk.CTkLabel(app, text='')     # Label que exibe o resultado do login (sucesso ou erro)
resultado_login.pack(pady=10)
```

## Botão de Alteração de Tema

```python
botao_tema = ctk.CTkButton(app, text='White', width=70, command=toggle_tema)  # Botão para mudar o tema (escuro/claro)
botao_tema.pack(pady=20)
```

## Execução da Janela

```python
app.mainloop()          # Mantém a janela aberta, aguardando interações do usuário
```
