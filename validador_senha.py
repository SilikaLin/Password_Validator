class ValidadorSenha:

def validar_senha(senha):
    if len(senha) < 8:
        return False, "A senha deve ter no mínimo 8 caracteres"

    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número"

    tem_maiuscula = any(char.isupper() for char in senha)
    if not tem_maiuscula:
        return False, "A senha deve conter pelo menos uma letra maiúscula"

    tem_minuscula = any(char.islower() for char in senha)
    if not tem_minuscula:
        return False, "A senha deve conter pelo menos uma letra minúscula"

    return True, "Senha válida"
