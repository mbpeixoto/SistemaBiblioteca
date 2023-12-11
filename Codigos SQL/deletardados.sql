-- Deleção de dados das tabelas relacionadas
DELETE FROM Livros_has_Autores;
DELETE FROM Livros_has_Usuarios;
DELETE FROM Professores_has_Cursos;

-- Deleção de dados das tabelas principais
DELETE FROM Livros;
DELETE FROM Autores;
DELETE FROM Usuarios;
DELETE FROM Alunos;
DELETE FROM Cursos;
DELETE FROM Funcionarios;
DELETE FROM Professores;
DELETE FROM Bibliotecarios;
