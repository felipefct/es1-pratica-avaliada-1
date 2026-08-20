import hashlib
from typing import List, Optional

class Usuario:
    """Classe de usuário simplificada (Princípio YAGNI)"""
    
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)
    
    def _hash_senha(self, senha: str) -> str:
        """Hash da senha mantido por segurança básica"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def validar_senha(self, senha: str) -> bool:
        """Valida senha do usuário"""
        return self._hash_senha(senha) == self.senha

class GerenciadorUsuarios:
    """Gerencia coleção de usuários focada apenas nos requisitos atuais"""
    
    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.indice_email = {}
    
    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra novo usuário garantindo que o email não seja duplicado"""
        if email in self.indice_email:
            raise ValueError("Email já cadastrado")
        
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        self.indice_email[email] = usuario
        return usuario
    
    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """Realiza login validando email e senha"""
        usuario = self.indice_email.get(email)
        if usuario and usuario.validar_senha(senha):
            return usuario
        return None
    
    def listar_todos(self) -> List[Usuario]:
        """Lista todos os usuários"""
        return self.usuarios