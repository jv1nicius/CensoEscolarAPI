DROP TABLE IF EXISTS tb_uf;
DROP TABLE IF EXISTS tb_instituicao;
DROP TABLE IF EXISTS tb_Municipio;
DROP TABLE IF EXISTS tb_Microrregiao;
DROP TABLE IF EXISTS tb_Mesorregiao;

CREATE TABLE tb_uf (
    id INTEGER PRIMARY KEY,
    uf TEXT,
    nome TEXT,
    regiao TEXT
);

CREATE TABLE tb_mesorregiao (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idUf INTEGER,
    FOREIGN KEY (idUf) REFERENCES tb_uf(id)
);

CREATE TABLE tb_microrregiao (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idMes INTEGER,
    idUf INTEGER,
    regiao TEXT,
    FOREIGN KEY (idMes) REFERENCES tb_mesorregiao(id),
    FOREIGN KEY (idUf) REFERENCES tb_uf(id)
);

CREATE TABLE tb_municipio (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idMes INTEGER,
    idMicro INTEGER,
    idUf INTEGER,
    regiao TEXT,
    FOREIGN KEY (idMes) REFERENCES tb_mesorregiao(id),
    FOREIGN KEY (idMicro) REFERENCES tb_microrregiao(id),
    FOREIGN key (idUf) REFERENCES tb_uf(id)
);

CREATE TABLE tb_instituicao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    no_regiao TEXT NOT NULL,
    co_regiao INTEGER NOT NULL,
    no_uf TEXT NOT NULL,
    sg_uf TEXT NOT NULL,
    co_uf INTEGER NOT NULL,
    no_municipio TEXT NOT NULL,
    co_municipio INTEGER NOT NULL,
    no_mesorregiao TEXT NOT NULL,
    co_mesorregiao INTEGER NOT NULL,
    no_microrregiao TEXT NOT NULL,
    co_microrregiao INTEGER NOT NULL,
    no_entidade TEXT NOT NULL,
    co_entidade INTEGER NOT NULL,
    qt_mat_bas INTEGER NOT NULL,
    qt_mat_eja INTEGER NOT NULL,
    qt_mat_esp INTEGER NOT NULL,
    qt_mat_fund INTEGER NOT NULL,
    qt_mat_inf INTEGER NOT NULL,
    qt_mat_med INTEGER NOT NULL,
    qt_mat_prof INTEGER NOT NULL,
    FOREIGN KEY (co_uf) REFERENCES tb_uf(id),
    FOREIGN KEY (co_municipio) REFERENCES tb_municipio(id),
    FOREIGN KEY (co_mesorregiao) REFERENCES tb_mesorregiao(id),
    FOREIGN KEY (co_microrregiao) REFERENCES tb_microrregiao(id)
);
