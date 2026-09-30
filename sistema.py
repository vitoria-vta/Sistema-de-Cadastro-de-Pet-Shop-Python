import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


donos = []
animais = []
servicos = []




def cpf_existe(cpf):
    """Verifica se o CPF já está cadastrado na lista de donos."""
    for dono in donos:
        if dono["cpf"] == cpf:
            return True
    return False

def mensagem_status(texto):
    """Função utilitária para exibir mensagens de status no campo de texto."""
    textbox_relatorio.delete("1.0", ctk.END)
    textbox_relatorio.insert("1.0", f" STATUS: {texto}\n")




def cadastrar_dono():
    nome = entry_dono_nome.get().strip()
    cpf = entry_dono_cpf.get().strip()

    if not nome or not cpf:
        mensagem_status("Preencha todos os campos do dono!")
        return

    if cpf_existe(cpf):
        mensagem_status("Erro: CPF já cadastrado!")
        return

    donos.append({"nome": nome, "cpf": cpf})
    mensagem_status(f"Dono '{nome}' cadastrado com sucesso!")
    
    # Limpa os campos
    entry_dono_nome.delete(0, ctk.END)
    entry_dono_cpf.delete(0, ctk.END)

def cadastrar_animal():
    nome_animal = entry_animal_nome.get().strip()
    especie = entry_animal_especie.get().strip()
    nome_dono = entry_animal_dono.get().strip()

    if not nome_animal or not especie or not nome_dono:
        mensagem_status("Preencha todos os campos do animal!")
        return

    animais.append({"nome": nome_animal, "especie": especie, "dono": nome_dono})
    mensagem_status(f"Animal '{nome_animal}' cadastrado com sucesso!")

    # Limpa os campos
    entry_animal_nome.delete(0, ctk.END)
    entry_animal_especie.delete(0, ctk.END)
    entry_animal_dono.delete(0, ctk.END)

def cadastrar_servico():
    nome_animal = entry_servico_animal.get().strip()
    servico_nome = entry_servico_nome.get().strip()
    valor_str = entry_servico_valor.get().strip()

    if not nome_animal or not servico_nome or not valor_str:
        mensagem_status("Preencha todos os campos do serviço!")
        return

    try:
        valor = float(valor_str)
    except ValueError:
        mensagem_status("Erro: O valor deve ser um número (ex: 50.00)!")
        return

    servicos.append({"animal": nome_animal, "servico": servico_nome, "valor": valor})
    mensagem_status(f"Serviço '{servico_nome}' registrado para {nome_animal}!")

    # Limpa os campos
    entry_servico_animal.delete(0, ctk.END)
    entry_servico_nome.delete(0, ctk.END)
    entry_servico_valor.delete(0, ctk.END)

def listar_donos():
    textbox_relatorio.delete("1.0", ctk.END)
    textbox_relatorio.insert("1.0", "=== LISTA DE DONOS ===\n\n")
    if not donos:
        textbox_relatorio.insert(ctk.END, "Nenhum dono cadastrado.\n")
        return
    for d in donos:
        textbox_relatorio.insert(ctk.END, f"• Nome: {d['nome']} | CPF: {d['cpf']}\n")

def listar_animais():
    textbox_relatorio.delete("1.0", ctk.END)
    textbox_relatorio.insert("1.0", "=== LISTA DE ANIMAIS ===\n\n")
    if not animais:
        textbox_relatorio.insert(ctk.END, "Nenhum animal cadastrado.\n")
        return
    for a in animais:
        textbox_relatorio.insert(ctk.END, f"• Animal: {a['nome']} | Espécie: {a['especie']} | Dono: {a['dono']}\n")

def listar_servicos():
    textbox_relatorio.delete("1.0", ctk.END)
    textbox_relatorio.insert("1.0", "=== LISTA DE SERVIÇOS ===\n\n")
    if not servicos:
        textbox_relatorio.insert(ctk.END, "Nenhum serviço registrado.\n")
        return
    for s in servicos:
        textbox_relatorio.insert(ctk.END, f"• Animal: {s['animal']} | Serviço: {s['servico']} | Valor: R$ {s['valor']:.2f}\n")




def total_gasto_por_animal():
    textbox_relatorio.delete("1.0", ctk.END)
    textbox_relatorio.insert("1.0", "=== TOTAL GASTO POR ANIMAL ===\n\n")
    if not servicos:
        textbox_relatorio.insert(ctk.END, "Nenhum serviço registrado ainda.\n")
        return

    # Acumula o valor gasto por cada animal
    totais = {}
    for s in servicos:
        nome_animal = s["animal"]
        totais[nome_animal] = totais.get(nome_animal, 0.0) + s["valor"]

    for animal, total in totais.items():
        textbox_relatorio.insert(ctk.END, f"• Animal: {animal} | Total Gasto: R$ {total:.2f}\n")




app = ctk.CTk()
app.title("Sistema Simples de Pet Shop")
app.geometry("700x750")
app.resizable(False, False)


ctk.CTkLabel(app, text="Pet Shop - Painel de Controle", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)


ctk.CTkLabel(app, text="1. Cadastrar Dono", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20)
entry_dono_nome = ctk.CTkEntry(app, placeholder_text="Nome do Dono", width=300)
entry_dono_nome.pack(pady=2)
entry_dono_cpf = ctk.CTkEntry(app, placeholder_text="CPF", width=300)
entry_dono_cpf.pack(pady=2)
ctk.CTkButton(app, text="Salvar Dono", command=cadastrar_dono).pack(pady=5)


ctk.CTkLabel(app, text="2. Cadastrar Animal", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20)
entry_animal_nome = ctk.CTkEntry(app, placeholder_text="Nome do Animal", width=300)
entry_animal_nome.pack(pady=2)
entry_animal_especie = ctk.CTkEntry(app, placeholder_text="Espécie (Ex: Cão, Gato)", width=300)
entry_animal_especie.pack(pady=2)
entry_animal_dono = ctk.CTkEntry(app, placeholder_text="Nome do Dono", width=300)
entry_animal_dono.pack(pady=2)
ctk.CTkButton(app, text="Salvar Animal", command=cadastrar_animal).pack(pady=5)


ctk.CTkLabel(app, text="3. Registrar Serviço", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20)
entry_servico_animal = ctk.CTkEntry(app, placeholder_text="Nome do Animal", width=300)
entry_servico_animal.pack(pady=2)
entry_servico_nome = ctk.CTkEntry(app, placeholder_text="Serviço (Ex: Banho, Tosa)", width=300)
entry_servico_nome.pack(pady=2)
entry_servico_valor = ctk.CTkEntry(app, placeholder_text="Valor (R$)", width=300)
entry_servico_valor.pack(pady=2)
ctk.CTkButton(app, text="Salvar Serviço", command=cadastrar_servico).pack(pady=5)


ctk.CTkLabel(app, text="4. Consultas e Relatórios", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20, pady=(10, 0))

ctk.CTkButton(app, text="Listar Donos", command=listar_donos, width=150).pack(pady=2)
ctk.CTkButton(app, text="Listar Animais", command=listar_animais, width=150).pack(pady=2)
ctk.CTkButton(app, text="Listar Serviços", command=listar_servicos, width=150).pack(pady=2)
ctk.CTkButton(app, text="Total Gasto por Animal (Extra)", command=total_gasto_por_animal, width=200, fg_color="green", hover_color="darkgreen").pack(pady=5)


textbox_relatorio = ctk.CTkTextbox(app, width=650, height=150)
textbox_relatorio.pack(padx=20, pady=10)

app.mainloop()