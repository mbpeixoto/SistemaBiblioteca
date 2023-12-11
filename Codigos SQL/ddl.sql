-- Tabela Livros
CREATE TABLE Livros (
    ISBN TEXT PRIMARY KEY,
    titulo VARCHAR(255),
    ano INT,
    editora VARCHAR(255),
    qtdCopias INT,
    categoria VARCHAR(255)
);

-- Tabela Autores
CREATE TABLE Autores (
    idAutores SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    cpf VARCHAR(14),
    nacionalidade VARCHAR(255)
);

-- Tabela Livros_has_Autores
CREATE TABLE Livros_has_Autores (
    Livros_ISBN TEXT,
    Autores_idAutores INT,
    PRIMARY KEY (Livros_ISBN, Autores_idAutores),
    FOREIGN KEY (Livros_ISBN) REFERENCES Livros(ISBN),
    FOREIGN KEY (Autores_idAutores) REFERENCES Autores(idAutores)
);

-- Tabela Usuarios
CREATE TABLE Usuarios (
    idUsuario SERIAL PRIMARY KEY,
    nickname VARCHAR(255),
    senha VARCHAR(255),
    tipo VARCHAR(255),
    grupo VARCHAR(255)
);

-- Tabela Livros_has_Usuarios
CREATE TABLE Livros_has_Usuarios (
    Livros_ISBN TEXT,
    Usuarios_idUsuario INT,
    PRIMARY KEY (Livros_ISBN, Usuarios_idUsuario),
    FOREIGN KEY (Livros_ISBN) REFERENCES Livros(ISBN),
    FOREIGN KEY (Usuarios_idUsuario) REFERENCES Usuarios(idUsuario)
);
-- Tabela Cursos
CREATE TABLE Cursos (
    idCurso SERIAL PRIMARY KEY,
    nome VARCHAR(255)
);

-- Tabela Alunos
CREATE TABLE Alunos (
    matriculaAluno TEXT PRIMARY KEY,
    nome VARCHAR(255),
    dataIngresso DATE,
    dataPrevisaoConclusao DATE,
    Curso_idCurso INT,
    Usuarios_idUsuario INT,
    FOREIGN KEY (Curso_idCurso) REFERENCES Cursos(idCurso),
    FOREIGN KEY (Usuarios_idUsuario) REFERENCES Usuarios(idUsuario)
);

-- Tabela Funcionarios
CREATE TABLE Funcionarios (
    matriculaFuncionario TEXT PRIMARY KEY,
    cargo VARCHAR(255),
    Usuarios_idUsuario INT,
    FOREIGN KEY (Usuarios_idUsuario) REFERENCES Usuarios(idUsuario)
);

-- Tabela Professores
CREATE TABLE Professores (
    idProfessor SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    dataContratacao DATE,
    regimeTrabalho VARCHAR(255),
    Funcionarios_matriculaFuncionario TEXT,
    FOREIGN KEY (Funcionarios_matriculaFuncionario) REFERENCES Funcionarios(matriculaFuncionario)
);

-- Tabela Bibliotecarios
CREATE TABLE Bibliotecarios (
    idBibliotecarios SERIAL PRIMARY KEY,
    dataContratacao DATE,
    Funcionarios_matriculaFuncionario TEXT,
    FOREIGN KEY (Funcionarios_matriculaFuncionario) REFERENCES Funcionarios(matriculaFuncionario)
);

-- Tabela Professores_has_Cursos
CREATE TABLE Professores_has_Cursos (
    Professores_idProfessor INT,
    Cursos_idCurso INT,
    PRIMARY KEY (Professores_idProfessor, Cursos_idCurso),
    FOREIGN KEY (Professores_idProfessor) REFERENCES Professores(idProfessor),
    FOREIGN KEY (Cursos_idCurso) REFERENCES Cursos(idCurso)
);