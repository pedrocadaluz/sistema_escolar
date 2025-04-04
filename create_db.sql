-- Criação do banco de dados com charset UTF-8
CREATE DATABASE IF NOT EXISTS db_escola2 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

USE db_escola;

-- Tabela de tb_enderecos
CREATE TABLE tb_enderecos (
    cep VARCHAR(10) PRIMARY KEY,
    endereco VARCHAR(255) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Tabela de tb_carros
CREATE TABLE tb_carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fabricante VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    especificacao VARCHAR(255)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Tabela de tb_alunos
CREATE TABLE tb_alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_aluno VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    cep VARCHAR(10),
    carro_id INT,
    FOREIGN KEY (cep) REFERENCES tb_enderecos(cep),
    FOREIGN KEY (carro_id) REFERENCES tb_carros(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Tabela de tb_disciplinas
CREATE TABLE tb_disciplinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_disciplina VARCHAR(255) NOT NULL,
    carga INT NOT NULL,
    semestre INT NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Tabela de tb_notas
CREATE TABLE tb_notas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT NOT NULL,
    disciplina_id INT NOT NULL,
    nota DECIMAL(5, 2),
    FOREIGN KEY (aluno_id) REFERENCES tb_alunos(id),
    FOREIGN KEY (disciplina_id) REFERENCES tb_disciplinas(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Inserir carros iniciais
INSERT INTO tb_carros (fabricante, modelo, especificacao) VALUES
('Volkswagen', 'Gol', '1.0 Flex, 4 portas, Manual'),
('Chevrolet', 'Onix', '1.4 LT, Automático, Branco'),
('Fiat', 'Uno', '1.0 Fire, 2 portas, Vermelho'),
('Ford', 'Ka', '1.5 SE, Hatch, Cinza'),
('Hyundai', 'HB20', '1.0 Comfort, Azul'),
('Renault', 'Sandero', '1.6 Expression, Preto'),
('Toyota', 'Corolla', '2.0 Altis, Automático, Prata'),
('Honda', 'Civic', '2.0 Sport, CVT, Preto'),
('Jeep', 'Renegade', '1.8 Longitude, SUV, Branco'),
('Nissan', 'Kicks', '1.6 SL, Automático, Cinza'),
('Peugeot', '208', '1.2 Active, Manual, Azul'),
('Chevrolet', 'Celta', '1.0 Spirit, 3 portas, Prata'),
('Fiat', 'Palio', '1.0 Attractive, Vermelho'),
('Volkswagen', 'Fox', '1.6 Comfortline, Hatch, Preto'),
('Hyundai', 'Creta', '2.0 Prestige, SUV, Branco');


-- Inserir disciplinas iniciais
INSERT INTO tb_disciplinas (nome_disciplina, carga, semestre) VALUES
('Cálculo a uma Variável', 80, 1),
('Estatística para Análise de Dados', 80, 1),
('Ética e Legislação em Ciência de Dados', 80, 1),
('Ciência de Dados nos Negócios', 80, 1),
('Fundamentos de Economia', 80, 2),
('Inferência Estatística', 80, 2),
('Modelagem Computacional', 80, 2),
('Programação com Orientação a Objetos', 80, 2),
('Geometria Analítica e Álgebra Linear', 80, 2),
('Matemática Discreta', 80, 3),
('Desenvolvimento Web', 80, 3),
('Design Gráfico e User Experience', 80, 3),
('Inovação e Design Thinking', 80, 3),
('Projeto Front-End', 80, 3),
('Programação para Análise de Dados', 80, 4),
('Estrutura e Engenharia de Dados', 80, 4),
('Business Intelligence', 80, 4),
('Business Analytics', 80, 4),
('Projeto de Dashboard', 80, 4),
('Gestão do Conhecimento', 80, 5),
('Arquitetura de Data Warehouse e Data Marts', 80, 5),
('Extração e Preparação de Dados', 80, 5),
('Big Data e Cloud Computing', 80, 5),
('Projeto de ETL', 80, 5),
('Aprendizado de Máquina', 80, 6),
('Startups e Negócios Digitais', 80, 6),
('Aprendizagem por Reforço', 80, 6),
('PLN e Visão Computacional', 80, 6),
('Projeto de Machine Learning', 80, 6),
('Análise de Séries Temporais', 80, 7),
('Redes Neurais e Deep Learning', 80, 7),
('Projeto de Deep Learning', 80, 7),
('Eletiva I', 80, 7),
('Eletiva II', 80, 7),
('Métodos Ágeis de Desenvolvimento de Software', 80, 8),
('TIC na Estratégia Empresarial', 80, 8),
('Liderança Contemporânea', 80, 8),
('Eletiva III', 80, 8),
('Eletiva IV', 80, 8);