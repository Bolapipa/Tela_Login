import customtkinter as ctk

# -----Aparencia inicial-----
ctk.set_appearance_mode('dark')  # Padrão ao abrir
tema_escuro = True  # Flag de controle

# -----Criação das funções de funcionalidades-----


def validar_login():
    campo_usuario.get()
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'Arthur' and senha == '123456':
        resultado_login.configure(
            text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login Incorreto', text_color='red')

# -----Função mostrar/oocultar senha-----


def toggle_senha():
    # se o campo senha está com *, troca para vazio. senão põe *
    mostrar = campo_senha.cget('show') == '*'
    campo_senha.configure(show='' if mostrar else '*')
    botao_toggle.configure(text='🙈' if mostrar else '🙉')  # ícone opcionl

# -----Função alteração de tema-----


def toggle_tema():
    global tema_escuro
    tema_escuro = not tema_escuro
    ctk.set_appearance_mode('dark' if tema_escuro else 'light')
    botao_tema.configure(text='White' if tema_escuro else 'Dark')


# -----Criação da janela principal-----
app = ctk.CTk()
app.title('Área de Login')
app.geometry('500x500')

# -----Criação dos campos-----
# Label
label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

# Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text=('Digite seu usuário'))
campo_usuario.pack(pady=10)

# Label
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

# Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

# -----Mostrar ocultar senha-----
botao_toggle = ctk.CTkButton(app, text='🙉', width=40, command=toggle_senha)
botao_toggle.pack(pady=(0, 10))

# Button
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

# Campo feddback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

# -----Botão alteração de tema-----
botao_tema = ctk.CTkButton(app, text='White', width=70, command=toggle_tema)
botao_tema.pack(pady=20)


app.mainloop()

# -----FIM-----
