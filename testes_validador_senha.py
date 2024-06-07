import unittest

def validar_senha(senha):
    # Verificar o comprimento da senha
    if len(senha) < 8:
        return False

    # Verificar se a senha contém pelo menos um número
    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        return False

    # Verificar se a senha contém pelo menos uma letra maiúscula
    tem_maiuscula = any(char.isupper() for char in senha)
    if not tem_maiuscula:
        return False

    # Verificar se a senha contém pelo menos uma letra minúscula
    tem_minuscula = any(char.islower() for char in senha)
    if not tem_minuscula:
        return False

    # Se a senha passar por todas as verificações, é válida
    return True


class TestValidadorSenha(unittest.TestCase):
    
    def test_comprimento_minimo(self):
        self.assertFalse(validar_senha("abc12"))  # Senha com menos de 8 caracteres
        self.assertTrue(validar_senha("Abc12345"))  # Senha com 8 caracteres
    
    def test_pelo_menos_um_numero(self):
        self.assertFalse(validar_senha("SenhaSemNumero"))  # Senha sem números
        self.assertTrue(validar_senha("SenhaComNumero1"))  # Senha com número
    
    def test_pelo_menos_uma_letra_maiuscula(self):
        self.assertFalse(validar_senha("senha_minuscula123"))  # Senha sem letra maiúscula
        self.assertTrue(validar_senha("Senha_Maiuscula123"))  # Senha com letra maiúscula
    
    def test_pelo_menos_uma_letra_minuscula(self):
        self.assertFalse(validar_senha("SENHA_MAISCULA123"))  # Senha sem letra minúscula
        self.assertTrue(validar_senha("Senha_Minuscula123"))  # Senha com letra minúscula


if __name__ == '__main__':
    unittest.main()
