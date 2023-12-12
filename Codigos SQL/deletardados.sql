-- Remover registros de tabelas dependentes
DROP TABLE Livros_has_Autores;
DROP TABLE Livros_has_Usuarios;
DROP TABLE Professores_has_Cursos;

-- Remover registros de tabelas principais, utilizando CASCADE para resolver as dependências
DROP TABLE Alunos CASCADE;
DROP TABLE Bibliotecarios CASCADE;
DROP TABLE Professores CASCADE;
DROP TABLE Funcionarios CASCADE;
DROP TABLE Usuarios CASCADE;
DROP TABLE Cursos CASCADE;
DROP TABLE Livros CASCADE;
DROP TABLE Autores CASCADE;