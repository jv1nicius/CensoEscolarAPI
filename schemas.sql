DROP TABLE IF EXISTS tb_uf;
DROP TABLE IF EXISTS tb_mesorregiao;
DROP TABLE IF EXISTS tb_microrregiao;
DROP TABLE IF EXISTS tb_municipio;
DROP TABLE IF EXISTS tb_instituicao;

CREATE TABLE tb_uf (
    id INTEGER PRIMARY KEY,
    uf VARCHAR(3) NOT NULL,
    nome TEXT NOT NULL,
    regiao TEXT NOT NULL
);

CREATE TABLE tb_mesorregiao (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idUf INTEGER NOT NULL,
    FOREIGN KEY (idUf) REFERENCES tb_uf(id)
);

CREATE TABLE tb_microrregiao (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idMes INTEGER NOT NULL,
    idUf INTEGER NOT NULL,
    FOREIGN KEY (idMes) REFERENCES tb_mesorregiao(id),
    FOREIGN KEY (idUf) REFERENCES tb_uf(id)
);

CREATE TABLE tb_municipio (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idMes INTEGER NOT NULL,
    idMicro INTEGER NOT NULL,
    idUf INTEGER NOT NULL,
    FOREIGN KEY (idMes) REFERENCES tb_mesorregiao(id),
    FOREIGN KEY (idMicro) REFERENCES tb_microrregiao(id),
    FOREIGN KEY (idUf) REFERENCES tb_uf(id)
);

CREATE TABLE tb_instituicao (
    co_entidade INTEGER PRIMARY KEY,
    no_entidade VARCHAR(200),
    nu_ano_censo INTEGER NOT NULL,
    no_regiao VARCHAR(100) NOT NULL,
    co_regiao INTEGER NOT NULL,
    no_uf TEXT NOT NULL,
    sg_uf VARCHAR(3) NOT NULL,
    co_uf INTEGER NOT NULL,
    no_municipio VARCHAR(100) NOT NULL,
    co_municipio INTEGER NOT NULL,
    no_mesorregiao VARCHAR(100),
    co_mesorregiao INTEGER,
    no_microrregiao VARCHAR(100),
    co_microrregiao INTEGER,
    qt_mat_bas INTEGER,
    qt_mat_eja INTEGER,
    qt_mat_esp INTEGER,
    qt_mat_fund INTEGER,
    qt_mat_inf INTEGER,
    qt_mat_med INTEGER,
    qt_mat_prof INTEGER,
    FOREIGN KEY (co_municipio) REFERENCES tb_municipio(id),
    FOREIGN KEY (co_mesorregiao) REFERENCES tb_mesorregiao(id),
    FOREIGN KEY (co_microrregiao) REFERENCES tb_microrregiao(id),
    FOREIGN KEY (co_uf) REFERENCES tb_uf(id)
);
