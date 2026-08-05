import tkinter as tk
from tkinter import messagebox, ttk

# ==============================================================================
# CADASTRO INICIAL DOS PRODUTOS (Variáveis Globais)
# ==============================================================================

p1_nome = "Pomada Modeladora"
p1_estoque = 50
p1_preco = 29.90
p1_validade = "10/12/2027"
p1_descricao = "Pomada para modelar cabelos com efeito fosco."

p2_nome = "Óleo para Barba"
p2_estoque = 30
p2_preco = 39.90
p2_validade = "15/11/2027"
p2_descricao = "Óleo hidratante para barba."

p3_nome = "Shampoo Masculino"
p3_estoque = 40
p3_preco = 24.90
p3_validade = "20/10/2027"
p3_descricao = "Shampoo masculino para limpeza profunda."

faturamento_total = 0.0

# ==============================================================================
# FUNÇÕES DE LÓGICA DO SISTEMA
# ==============================================================================


def atualizar_exibicao():
    """Atualiza a lista visual de produtos na interface."""
    txt_lista.config(state="normal")
    txt_lista.delete("1.0", tk.END)

    if p1_nome == "" and p2_nome == "" and p3_nome == "":
        txt_lista.insert(tk.END, "Nenhum produto cadastrado.")
    else:
        if p1_nome != "":
            txt_lista.insert(
                tk.END,
                f" VAGA 1\nNome: {p1_nome}\nPreço: R$ {p1_preco:.2f}\nEstoque: {p1_estoque} unidades\nValidade: {p1_validade}\nDescrição: {p1_descricao}\n",
            )
            txt_lista.insert(tk.END, "✂️" * 40 + "\n")

        if p2_nome != "":
            txt_lista.insert(
                tk.END,
                f" VAGA 2\nNome: {p2_nome}\nPreço: R$ {p2_preco:.2f}\nEstoque: {p2_estoque} unidades\nValidade: {p2_validade}\nDescrição: {p2_descricao}\n",
            )
            txt_lista.insert(tk.END, "✂️" * 40 + "\n")

        if p3_nome != "":
            txt_lista.insert(
                tk.END,
                f" VAGA 3\nNome: {p3_nome}\nPreço: R$ {p3_preco:.2f}\nEstoque: {p3_estoque} unidades\nValidade: {p3_validade}\nDescrição: {p3_descricao}\n",
            )
            txt_lista.insert(tk.END, "✂️" * 40 + "\n")

    txt_lista.config(state="disabled")


def cadastrar_produto():
    global p1_nome, p1_estoque, p1_preco, p1_validade, p1_descricao
    global p2_nome, p2_estoque, p2_preco, p2_validade, p2_descricao
    global p3_nome, p3_estoque, p3_preco, p3_validade, p3_descricao

    nome = ent_nome.get().strip()
    if not nome:
        messagebox.showwarning("Aviso", "O nome do produto é obrigatório!")
        return

    try:
        estoque = int(ent_estoque.get())
        preco = float(ent_preco.get())
    except ValueError:
        messagebox.showerror(
            "Erro", "Estoque deve ser inteiro e Preço deve ser numérico!"
        )
        return

    validade = ent_validade.get()
    descricao = ent_descricao.get()

    if p1_nome == "":
        p1_nome, p1_estoque, p1_preco, p1_validade, p1_descricao = (
            nome,
            estoque,
            preco,
            validade,
            descricao,
        )
        messagebox.showinfo(
            "Sucesso", f'Produto "{nome}" cadastrado na vaga 1!'
        )
    elif p2_nome == "":
        p2_nome, p2_estoque, p2_preco, p2_validade, p2_descricao = (
            nome,
            estoque,
            preco,
            validade,
            descricao,
        )
        messagebox.showinfo(
            "Sucesso", f'Produto "{nome}" cadastrado na vaga 2!'
        )
    elif p3_nome == "":
        p3_nome, p3_estoque, p3_preco, p3_validade, p3_descricao = (
            nome,
            estoque,
            preco,
            validade,
            descricao,
        )
        messagebox.showinfo(
            "Sucesso", f'Produto "{nome}" cadastrado na vaga 3!'
        )
    else:
        messagebox.showerror(
            "Erro", "Sistema cheio! Limite de 3 produtos atingido."
        )

    # Limpar campos após cadastro
    ent_nome.delete(0, tk.END)
    ent_estoque.delete(0, tk.END)
    ent_preco.delete(0, tk.END)
    ent_validade.delete(0, tk.END)
    ent_descricao.delete(0, tk.END)
    atualizar_exibicao()


def realizar_venda():
    global p1_estoque, p2_estoque, p3_estoque, faturamento_total
    nome_venda = ent_acao_nome.get().strip().lower()
    qtd_str = ent_acao_qtd.get().strip()

    if not nome_venda or not qtd_str:
        messagebox.showwarning(
            "Aviso", "Preencha o Nome do Produto e a Quantidade!"
        )
        return

    try:
        qtd = int(qtd_str)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro!")
        return

    if nome_venda == p1_nome.lower() and p1_nome != "":
        if qtd <= p1_estoque:
            p1_estoque -= qtd
            total = qtd * p1_preco
            faturamento_total += total
            messagebox.showinfo(
                "Venda realizada",
                f"✅ Venda realizada!\nTotal: R$ {total:.2f}\nEstoque atual: {p1_estoque}",
            )
        else:
            messagebox.showerror("Erro", "❌ Estoque insuficiente!")
    elif nome_venda == p2_nome.lower() and p2_nome != "":
        if qtd <= p2_estoque:
            p2_estoque -= qtd
            total = qtd * p2_preco
            faturamento_total += total
            messagebox.showinfo(
                "Venda realizada",
                f"✅ Venda realizada!\nTotal: R$ {total:.2f}\nEstoque atual: {p2_estoque}",
            )
        else:
            messagebox.showerror("Erro", "❌ Estoque insuficiente!")
    elif nome_venda == p3_nome.lower() and p3_nome != "":
        if qtd <= p3_estoque:
            p3_estoque -= qtd
            total = qtd * p3_preco
            faturamento_total += total
            messagebox.showinfo(
                "Venda realizada",
                f"✅ Venda realizada!\nTotal: R$ {total:.2f}\nEstoque atual: {p3_estoque}",
            )
        else:
            messagebox.showerror("Erro", "❌ Estoque insuficiente!")
    else:
        messagebox.showerror("Erro", "❌ Produto não encontrado!")

    atualizar_exibicao()


def remover_produto():
    global p1_nome, p2_nome, p3_nome
    nome_remover = ent_acao_nome.get().strip().lower()

    if not nome_remover:
        messagebox.showwarning(
            "Aviso", "Digite o nome do produto no campo de ações!"
        )
        return

    if nome_remover == p1_nome.lower() and p1_nome != "":
        p1_nome = ""
        messagebox.showinfo(
            "Removido", "🗑️ Produto 1 removido com sucesso! Vaga 1 liberada."
        )
    elif nome_remover == p2_nome.lower() and p2_nome != "":
        p2_nome = ""
        messagebox.showinfo(
            "Removido", "🗑️ Produto 2 removido com sucesso! Vaga 2 liberada."
        )
    elif nome_remover == p3_nome.lower() and p3_nome != "":
        p3_nome = ""
        messagebox.showinfo(
            "Removido", "🗑️ Produto 3 removido com sucesso! Vaga 3 liberada."
        )
    else:
        messagebox.showerror("Erro", "❌ Produto não encontrado.")

    atualizar_exibicao()


def atualizar_preco():
    global p1_preco, p2_preco, p3_preco
    nome_preco = ent_acao_nome.get().strip().lower()
    novo_valor_str = ent_acao_qtd.get().strip()

    if not nome_preco or not novo_valor_str:
        messagebox.showwarning(
            "Aviso", "Preencha o Nome do Produto e o Novo Preço (no campo Qtd)!"
        )
        return

    try:
        novo_preco = float(novo_valor_str)
    except ValueError:
        messagebox.showerror("Erro", "Preço deve ser um valor numérico!")
        return

    if nome_preco == p1_nome.lower() and p1_nome != "":
        p1_preco = novo_preco
        messagebox.showinfo("Sucesso", "💵 Preço atualizado com sucesso!")
    elif nome_preco == p2_nome.lower() and p2_nome != "":
        p2_preco = novo_preco
        messagebox.showinfo("Sucesso", "💵 Preço atualizado com sucesso!")
    elif nome_preco == p3_nome.lower() and p3_nome != "":
        p3_preco = novo_preco
        messagebox.showinfo("Sucesso", "💵 Preço updated com sucesso!")
    else:
        messagebox.showerror("Erro", "❌ Produto não encontrado.")

    atualizar_exibicao()


def adicionar_estoque():
    global p1_estoque, p2_estoque, p3_estoque
    nome_estoque = ent_acao_nome.get().strip().lower()
    qtd_add_str = ent_acao_qtd.get().strip()

    if not nome_estoque or not qtd_add_str:
        messagebox.showwarning(
            "Aviso", "Preencha o Nome do Produto e a Quantidade a adicionar!"
        )
        return

    try:
        qtd_add = int(qtd_add_str)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um inteiro!")
        return

    if nome_estoque == p1_nome.lower() and p1_nome != "":
        p1_estoque += qtd_add
        messagebox.showinfo(
            "Sucesso",
            f"📦 Estoque atualizado! Novo estoque de {p1_nome}: {p1_estoque}",
        )
    elif nome_estoque == p2_nome.lower() and p2_nome != "":
        p2_estoque += qtd_add
        messagebox.showinfo(
            "Sucesso",
            f"📦 Estoque atualizado! Novo estoque de {p2_nome}: {p2_estoque}",
        )
    elif nome_estoque == p3_nome.lower() and p3_nome != "":
        p3_estoque += qtd_add
        messagebox.showinfo(
            "Sucesso",
            f"📦 Estoque atualizado! Novo estoque de {p3_nome}: {p3_estoque}",
        )
    else:
        messagebox.showerror("Erro", "❌ Produto não encontrado.")

    atualizar_exibicao()


def relatorio_faturamento():
    messagebox.showinfo(
        "📊 Faturamento",
        f"📊 RELATÓRIO DE FATURAMENTO 📊\n\nTotal arrecadado em vendas: R$ {faturamento_total:.2f}",
    )


def buscar_produto():
    nome_busca = ent_acao_nome.get().strip().lower()

    if not nome_busca:
        messagebox.showwarning(
            "Aviso", "Digite o nome do produto para buscar!"
        )
        return

    if nome_busca == p1_nome.lower() and p1_nome != "":
        messagebox.showinfo(
            "🔍 Encontrado",
            f"Vaga 1:\nNome: {p1_nome}\nPreço: R$ {p1_preco:.2f}\nEstoque: {p1_estoque}\nDescrição: {p1_descricao}",
        )
    elif nome_busca == p2_nome.lower() and p2_nome != "":
        messagebox.showinfo(
            "🔍 Encontrado",
            f"Vaga 2:\nNome: {p2_nome}\nPreço: R$ {p2_preco:.2f}\nEstoque: {p2_estoque}\nDescrição: {p2_descricao}",
        )
    elif nome_busca == p3_nome.lower() and p3_nome != "":
        messagebox.showinfo(
            "🔍 Encontrado",
            f"Vaga 3:\nNome: {p3_nome}\nPreço: R$ {p3_preco:.2f}\nEstoque: {p3_estoque}\nDescrição: {p3_descricao}",
        )
    else:
        messagebox.showerror("Erro", "❌ Produto não encontrado.")


def aplicar_desconto():
    global p1_preco, p2_preco, p3_preco
    nome_desconto = ent_acao_nome.get().strip().lower()
    porcentagem_str = ent_acao_qtd.get().strip()

    if not nome_desconto or not porcentagem_str:
        messagebox.showwarning(
            "Aviso",
            "Preencha o Nome do Produto e a Porcentagem de desconto (no campo Qtd)!",
        )
        return

    try:
        porcentagem = float(porcentagem_str)
    except ValueError:
        messagebox.showerror("Erro", "Porcentagem deve ser um número!")
        return

    if nome_desconto == p1_nome.lower() and p1_nome != "":
        p1_preco -= p1_preco * (porcentagem / 100)
        messagebox.showinfo(
            "Sucesso",
            f"📉 Desconto aplicado! Novo preço do(a) {p1_nome}: R$ {p1_preco:.2f}",
        )
    elif nome_desconto == p2_nome.lower() and p2_nome != "":
        p2_preco -= p2_preco * (porcentagem / 100)
        messagebox.showinfo(
            "Sucesso",
            f"📉 Desconto aplicado! Novo preço do(a) {p2_nome}: R$ {p2_preco:.2f}",
        )
    elif nome_desconto == p3_nome.lower() and p3_nome != "":
        p3_preco -= p3_preco * (porcentagem / 100)
        messagebox.showinfo(
            "Sucesso",
            f"📉 Desconto aplicado! Novo preço do(a) {p3_nome}: R$ {p3_preco:.2f}",
        )
    else:
        messagebox.showerror("Erro", "❌ Produto não encontrado.")

    atualizar_exibicao()


# ==============================================================================
# CONFIGURAÇÃO DA INTERFACE GRÁFICA (TKINTER)
# ==============================================================================

janela = tk.Tk()
janela.title("Sistema de Vendas - Barbearia")
janela.geometry("800x650")
janela.resizable(False, False)

# Estilo para os componentes
estilo = ttk.Style()
estilo.theme_use("clam")

# Título Principal
lbl_titulo = tk.Label(
    janela,
    text="💈 Barbearia - Sistema de Vendas 💈",
    font=("Helvetica", 16, "bold"),
    pady=10,
)
lbl_titulo.pack()

# --- FRAME 1: FORMULÁRIO DE CADASTRO (Opção 1) ---
frame_cadastro = tk.LabelFrame(
    janela, text=" 1. Cadastrar Novo Produto ", font=("Helvetica", 10, "bold")
)
frame_cadastro.pack(fill="x", padx=15, pady=5)

tk.Label(frame_cadastro, text="Nome:").grid(row=0, column=0, padx=5, pady=2)
ent_nome = tk.Entry(frame_cadastro, width=20)
ent_nome.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_cadastro, text="Estoque:").grid(row=0, column=2, padx=5, pady=2)
ent_estoque = tk.Entry(frame_cadastro, width=8)
ent_estoque.grid(row=0, column=3, padx=5, pady=2)

tk.Label(frame_cadastro, text="Preço: R$").grid(
    row=0, column=4, padx=5, pady=2
)
ent_preco = tk.Entry(frame_cadastro, width=8)
ent_preco.grid(row=0, column=5, padx=5, pady=2)

tk.Label(frame_cadastro, text="Validade:").grid(row=1, column=0, padx=5, pady=2)
ent_validade = tk.Entry(frame_cadastro, width=20)
ent_validade.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame_cadastro, text="Descrição:").grid(
    row=1, column=2, padx=5, pady=2
)
ent_descricao = tk.Entry(frame_cadastro, width=25)
ent_descricao.grid(row=1, column=3, columnspan=3, padx=5, pady=2, sticky="we")

btn_cadastrar = tk.Button(
    frame_cadastro,
    text="Cadastrar Produto",
    command=cadastrar_produto,
    bg="#4CAF50",
    fg="white",
)
btn_cadastrar.grid(row=0, column=6, rowspan=2, padx=15, pady=5, sticky="ns")

# --- FRAME 2: PAINEL DE AÇÕES (Opções 3, 4, 5, 6, 8, 9) ---
frame_acoes = tk.LabelFrame(
    janela,
    text=" Painel de Operações (Selecione o Produto pelo Nome) ",
    font=("Helvetica", 10, "bold"),
)
frame_acoes.pack(fill="x", padx=15, pady=5)

tk.Label(frame_acoes, text="Produto Alvo:").grid(
    row=0, column=0, padx=5, pady=5
)
ent_acao_nome = tk.Entry(frame_acoes, width=25)
ent_acao_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_acoes, text="Qtd / Novo Preço / % Desconto:").grid(
    row=0, column=2, padx=5, pady=5
)
ent_acao_qtd = tk.Entry(frame_acoes, width=12)
ent_acao_qtd.grid(row=0, column=3, padx=5, pady=5)

# Sub-frame para os botões de ação organizados em grade
frame_botoes = tk.Frame(frame_acoes)
frame_botoes.grid(row=1, column=0, columnspan=4, pady=5)

btn_venda = tk.Button(
    frame_botoes,
    text="3. Realizar Venda",
    width=18,
    command=realizar_venda,
    bg="#2196F3",
    fg="white",
)
btn_venda.grid(row=0, column=0, padx=4, pady=2)

btn_remover = tk.Button(
    frame_botoes,
    text="4. Remover Produto",
    width=18,
    command=remover_produto,
    bg="#f44336",
    fg="white",
)
btn_remover.grid(row=0, column=1, padx=4, pady=2)

btn_up_preco = tk.Button(
    frame_botoes,
    text="5. Atualizar Preço",
    width=18,
    command=atualizar_preco,
)
btn_up_preco.grid(row=0, column=2, padx=4, pady=2)

btn_add_est = tk.Button(
    frame_botoes,
    text="6. Repor Estoque",
    width=18,
    command=adicionar_estoque,
)
btn_add_est.grid(row=1, column=0, padx=4, pady=2)

btn_buscar = tk.Button(
    frame_botoes, text="8. Buscar por Nome", width=18, command=buscar_produto
)
btn_buscar.grid(row=1, column=1, padx=4, pady=2)

btn_desconto = tk.Button(
    frame_botoes,
    text="9. Aplicar Desconto",
    width=18,
    command=aplicar_desconto,
)
btn_desconto.grid(row=1, column=2, padx=4, pady=2)

# --- FRAME 3: RELATÓRIOS E FECHAMENTO (Opção 7 e 0) ---
frame_auxiliar = tk.Frame(janela)
frame_auxiliar.pack(fill="x", padx=15, pady=5)

btn_faturamento = tk.Button(
    frame_auxiliar,
    text="📊 7. Ver Faturamento Total",
    font=("Helvetica", 10, "bold"),
    command=relatorio_faturamento,
    bg="#FF9800",
    fg="white",
)
btn_faturamento.pack(side="left", padx=5)

btn_sair = tk.Button(
    frame_auxiliar,
    text="🚪 0. Sair",
    font=("Helvetica", 10, "bold"),
    command=janela.quit,
    bg="#9E9E9E",
    fg="white",
)
btn_sair.pack(side="right", padx=5)

# --- FRAME 4: LISTAGEM VISUAL EM TEMPO REAL (Opção 2) ---
frame_lista = tk.LabelFrame(
    janela,
    text=" 2. Monitor de Produtos Cadastrados ",
    font=("Helvetica", 10, "bold"),
)
frame_lista.pack(fill="both", expand=True, padx=15, pady=10)

txt_lista = tk.Text(frame_lista, wrap="word", font=("Courier New", 10))
txt_lista.pack(fill="both", expand=True, padx=5, pady=5)

# Inicializa o monitor exibindo os 3 produtos mockados do seu escopo inicial
atualizar_exibicao()

# Inicializa a Janela Principal
janela.mainloop()