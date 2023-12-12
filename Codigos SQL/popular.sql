-- Inserção de Autores
INSERT INTO Autores (nome, cpf, nacionalidade) VALUES
    ('Autor 1', '111.111.111-11', 'Nacionalidade 1'),
    ('Autor 2', '222.222.222-22', 'Nacionalidade 2'),
    ('Autor 3', '333.333.333-33', 'Nacionalidade 3'),
    ('Autor 4', '444.444.444-44', 'Nacionalidade 4'),
    ('Autor 5', '555.555.555-55', 'Nacionalidade 5'),
    ('Autor 6', '666.666.666-66', 'Nacionalidade 6'),
    ('Autor 7', '777.777.777-77', 'Nacionalidade 7'),
    ('Autor 8', '888.888.888-88', 'Nacionalidade 8'),
    ('Autor 9', '999.999.999-99', 'Nacionalidade 9'),
    ('Autor 10', '101.101.101-10', 'Nacionalidade 10');

-- Inserção de Livros
INSERT INTO Livros (ISBN, titulo, ano, editora, qtdCopias, categoria) VALUES
    ('ISBN-1', 'Livro 1', 2020, 'Editora 1', 5, 'Categoria 1'),
    ('ISBN-2', 'Livro 2', 2021, 'Editora 2', 3, 'Categoria 2'),
    ('ISBN-3', 'Livro 3', 2019, 'Editora 3', 7, 'Categoria 1'),
    ('ISBN-4', 'Livro 4', 2022, 'Editora 4', 10, 'Categoria 3'),
    ('ISBN-5', 'Livro 5', 2018, 'Editora 5', 2, 'Categoria 2'),
    ('ISBN-6', 'Livro 6', 2020, 'Editora 1', 4, 'Categoria 3'),
    ('ISBN-7', 'Livro 7', 2021, 'Editora 2', 8, 'Categoria 1'),
    ('ISBN-8', 'Livro 8', 2019, 'Editora 3', 6, 'Categoria 2'),
    ('ISBN-9', 'Livro 9', 2022, 'Editora 4', 3, 'Categoria 3'),
    ('ISBN-10', 'Livro 10', 2018, 'Editora 5', 9, 'Categoria 1'),
    ('ISBN-11', 'Livro 11', 2020, 'Editora 1', 5, 'Categoria 2'),
    ('ISBN-12', 'Livro 12', 2021, 'Editora 2', 3, 'Categoria 3'),
    ('ISBN-13', 'Livro 13', 2019, 'Editora 3', 7, 'Categoria 1'),
    ('ISBN-14', 'Livro 14', 2022, 'Editora 4', 10, 'Categoria 2'),
    ('ISBN-15', 'Livro 15', 2018, 'Editora 5', 2, 'Categoria 3'),
    ('ISBN-16', 'Livro 16', 2020, 'Editora 1', 4, 'Categoria 1'),
    ('ISBN-17', 'Livro 17', 2021, 'Editora 2', 8, 'Categoria 2'),
    ('ISBN-18', 'Livro 18', 2019, 'Editora 3', 6, 'Categoria 3'),
    ('ISBN-19', 'Livro 19', 2022, 'Editora 4', 3, 'Categoria 1'),
    ('ISBN-20', 'Livro 20', 2018, 'Editora 5', 9, 'Categoria 2'),
    ('ISBN-21', 'Livro 21', 2020, 'Editora 1', 5, 'Categoria 3'),
    ('ISBN-22', 'Livro 22', 2021, 'Editora 2', 3, 'Categoria 1'),
    ('ISBN-23', 'Livro 23', 2019, 'Editora 3', 7, 'Categoria 2'),
    ('ISBN-24', 'Livro 24', 2022, 'Editora 4', 10, 'Categoria 3'),
    ('ISBN-25', 'Livro 25', 2018, 'Editora 5', 2, 'Categoria 1');

-- Inserção de Livros_has_Autores
INSERT INTO Livros_has_Autores (Livros_ISBN, Autores_idAutores) VALUES
    ('ISBN-1', 1),
    ('ISBN-2', 2),
    ('ISBN-3', 3),
    ('ISBN-4', 4),
    ('ISBN-5', 5),
    ('ISBN-6', 6),
    ('ISBN-7', 7),
    ('ISBN-8', 8),
    ('ISBN-9', 9),
    ('ISBN-10', 10),
    ('ISBN-11', 1),
    ('ISBN-12', 2),
    ('ISBN-13', 3),
    ('ISBN-14', 4),
    ('ISBN-15', 5),
    ('ISBN-16', 6),
    ('ISBN-17', 7),
    ('ISBN-18', 8),
    ('ISBN-19', 9),
    ('ISBN-20', 10),
    ('ISBN-21', 1),
    ('ISBN-22', 2),
    ('ISBN-23', 3),
    ('ISBN-24', 4),
    ('ISBN-25', 5);

-- Inserção de Usuarios
INSERT INTO Usuarios (nickname, senha, tipo, grupo) VALUES
    ('Usuario1', 'senha1', 'autenticado', 'aluno'),
    ('Usuario2', 'senha2', 'autenticado', 'aluno'),
    ('Usuario3', 'senha3', 'autenticado', 'aluno'),
    ('Usuario4', 'senha4', 'autenticado', 'aluno'),
    ('Usuario5', 'senha5', 'autenticado', 'aluno'),
    ('Usuario6', 'senha6', 'autenticado', 'professor'),
    ('Usuario7', 'senha7', 'autenticado', 'professor'),
    ('Usuario8', 'senha8', 'autenticado', 'professor'),
    ('Usuario9', 'senha9', 'bibliotecario', 'bibliotecario'),
    ('Usuario10', 'senha10', 'administrador', 'gerente');

-- Inserção de Cursos
INSERT INTO Cursos (nome) VALUES
    ('Engenharia de Software'),
    ('Ciência da Computação');

-- Inserção de Alunos
INSERT INTO Alunos (matriculaAluno, nome, dataIngresso, dataPrevisaoConclusao, Curso_idCurso, Usuarios_idUsuario) VALUES
    ('Matricula1', 'Aluno 1', '2020-01-01', '2024-12-31', 1, 1),
    ('Matricula2', 'Aluno 2', '2020-02-01', '2025-12-31', 2, 2),
    ('Matricula3', 'Aluno 3', '2020-03-01', '2024-12-31', 1, 3),
    ('Matricula4', 'Aluno 4', '2020-04-01', '2025-12-31', 2, 4),
    ('Matricula5', 'Aluno 5', '2020-05-01', '2024-12-31', 1, 5),
    ('Matricula6', 'Aluno 6', '2020-06-01', '2024-12-31', 1, NULL);

-- Inserção de Funcionarios
INSERT INTO Funcionarios (matriculaFuncionario, cargo, Usuarios_idUsuario) VALUES
    ('MatriculaFunc1', 'Professor', 6),
    ('MatriculaFunc2', 'Professor', 7),
    ('MatriculaFunc3', 'Professor', 8),
    ('MatriculaFunc4', 'Bibliotecario', 9),
    ('MatriculaFunc5', 'Gerente', 10),
    ('MatriculaFunc6', 'Gerente Auxiliar', NULL);

-- Inserção de Professores
INSERT INTO Professores (nome, dataContratacao, regimeTrabalho, Funcionarios_matriculaFuncionario) VALUES
    ('Professor1', '2020-01-01', 'Regime1', 'MatriculaFunc1'),
    ('Professor2', '2020-02-01', 'Regime2', 'MatriculaFunc2'),
    ('Professor3', '2020-03-01', 'Regime3', 'MatriculaFunc3');

-- Inserção de Bibliotecarios
INSERT INTO Bibliotecarios (dataContratacao, Funcionarios_matriculaFuncionario) VALUES
    ('2020-01-01', 'MatriculaFunc4');

-- Inserção de Livros_has_Usuarios (Empréstimos)
INSERT INTO Livros_has_Usuarios (Livros_ISBN, Usuarios_idUsuario) VALUES
    ('ISBN-1', 1),
    ('ISBN-2', 1),
    ('ISBN-3', 2),
    ('ISBN-4', 3),
    ('ISBN-5', 4),
    ('ISBN-6', 5),
    ('ISBN-7', 6),
    ('ISBN-8', 7),
    ('ISBN-9', 8),
    ('ISBN-10', 8);

-- Inserção de Professores_has_Cursos
INSERT INTO Professores_has_Cursos (Professores_idProfessor, Cursos_idCurso) VALUES
    (1, 1),
    (2, 2),
    (3, 1),
    (1, 2),
    (2, 1),
    (3, 2);
