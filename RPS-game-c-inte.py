import tkinter as tk
import random 

# Funçao de escolha do PC

def get_computador_choice():
    choices = ['pedra', 'papel', 'tesoura']
    return random.choice(choices)


# Função Ganhador

def determine_winner(computador_choice, user_choice):
    if computador_choice == user_choice:
        return "Empate"
    elif (user_choice == 'pedra' and computador_choice == 'tesoura') or \
         (user_choice == 'papel' and computador_choice == 'pedra') or \
         (user_choice == 'tesoura' and computador_choice == 'papel'):
        return "Você venceu!"
    else:
        return "Você perdeu!"
    
# Função para Jogar

def play(user_choice):
    computador_choice = get_computador_choice()
    result = determine_winner(user_choice, computador_choice)
    user_choice_label.config(text=f'Você escolheu: {user_choice}')
    user_choice_label.config(text=f"O computador escolheu: {computador_choice}")
    result_label.config(text=result)


# Janela principal config

root = tk.Tk()
root.title('Pedra, Papel e Tesoura')

# Janela exibição de esolha e resultado

user_choice_label = tk.Label(root, text="Voce escolheu: ", font=("Helvetica", 14))
user_choice_label.pack(pady=10)


computador_choice_label = tk.Label(root, text='O computador escolheu: ', font=("Helvetica", 14))
computador_choice_label.pack(pady=10)


result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
result_label.pack(pady=20)


# Botãos para escolha

button_frame = tk.Frame(root)
button_frame.pack(pady=20)


pedra_button = tk.Button(button_frame, text="Pedra", width=10, command=lambda: play('Pedra'))
pedra_button.grid(row=0, column=0, padx=5)


papel_button = tk.Button(button_frame, text="Papel", width=10, command=lambda: play("papel"))
papel_button.grid(row=0, column=1, padx=5)


tesoura_button = tk.Button(button_frame, text="Tesoura", width=10, command=lambda: play("tesoura"))
tesoura_button.grid(row=0, column=2, padx=5)


# Iniciar a aplicação

root.mainloop()