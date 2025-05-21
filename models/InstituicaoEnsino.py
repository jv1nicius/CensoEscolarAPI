from marshmallow import Schema, fields, validate

class InstituicaoEnsinoSchema(Schema):
    id = fields.Integer(required=True, error_messages={"required": "ID é obrigatório."})
    no_entidade = fields.String(validate=validate.Length(min=2, max=100),
                                required=True, error_messages={"required": "Nome da Entidade é obrigatório."})
    co_entidade = fields.Integer(required=True, error_messages={
                                 "required": "Código da Entidade é obrigatório."})
    qt_mat_bas = fields.Integer(required=True, error_messages={
        "required": "Quantidade de Matrículas Básicas é obrigatória."})
    qt_mat_eja = fields.Integer(required=True, error_messages={
        "required": "Quantidade de Matrículas EJA é obrigatória."})
    qt_mat_esp = fields.Integer(required=True, error_messages={
        "required": "Quantidade de Matrículas Especiais é obrigatória."})
    qt_mat_fund = fields.Integer(required=True, error_messages={
        "required": "Quantidade de Matrículas do Fundamental é obrigatória."})
    qt_mat_inf = fields.Integer(required=True, error_messages={
        "required": "Quantidade de Matrículas da Educação Infantil é obrigatória."})
    qt_mat_med = fields.Integer(required=True, error_messages={
        "required": "Quantidade de Matrículas do Médio é obrigatória."})
    qt_mat_prof = fields.Integer(required=True, error_messages={
        "required": "Quantidade de Professores é obrigatória."})
    no_regiao = fields.String(required=True, error_messages={
        "required": "Nome da Região é obrigatório."})
    co_regiao = fields.Integer(required=True, error_messages={
        "required": "Código da Região é obrigatório."})
    no_uf = fields.String(validate=validate.Length(min=2, max=2), required=True, error_messages={
        "required": "Nome da UF é obrigatório."})
    sg_uf = fields.String(validate=validate.Length(min=2, max=2), required=True, error_messages={
        "required": "Sigla da UF é obrigatória."})
    co_uf = fields.Integer(required=True, error_messages={
        "required": "Código da UF é obrigatório."})


class InstituicaoEnsino:
    def __init__(self, ID, NO_ENTIDADE, CO_ENTIDADE, QT_MAT_BAS, QT_MAT_EJA, QT_MAT_ESP, QT_MAT_FUND, QT_MAT_INF, QT_MAT_MED, QT_MAT_PROF, NO_REGIAO, CO_REGIAO, NO_UF, SG_UF, CO_UF, NO_MUNICIPIO, CO_MUNICIPIO, NO_MESORREGIAO, CO_MESORREGIAO, NO_MICRORREGIAO, CO_MICRORREGIAO):
        self.id = ID
        self.no_entidade = NO_ENTIDADE
        self.co_entidade = CO_ENTIDADE
        self.qt_mat_bas = QT_MAT_BAS
        self.qt_mat_eja = QT_MAT_EJA
        self.qt_mat_esp = QT_MAT_ESP
        self.qt_mat_fund = QT_MAT_FUND
        self.qt_mat_inf = QT_MAT_INF
        self.qt_mat_med = QT_MAT_MED
        self.qt_mat_prof = QT_MAT_PROF
        self.no_regiao = NO_REGIAO
        self.co_regiao = CO_REGIAO
        self.no_uf = NO_UF
        self.sg_uf = SG_UF
        self.co_uf = CO_UF
        self.no_municipio = NO_MUNICIPIO
        self.co_municipio = CO_MUNICIPIO
        self.no_mesorregiao = NO_MESORREGIAO
        self.co_mesorregiao = CO_MESORREGIAO
        self.no_microrregiao = NO_MICRORREGIAO
        self.co_microrregiao = CO_MICRORREGIAO

    def toDict(self):
        return {
            "ID": self.id,
            "NO_ENTIDADE": self.no_entidade,
            "CO_ENTIDADE": self.co_entidade,
            "QT_MAT_BAS": self.qt_mat_bas,
            "QT_MAT_EJA": self.qt_mat_eja,
            "QT_MAT_ESP": self.qt_mat_esp,
            "QT_MAT_FUND": self.qt_mat_fund,
            "QT_MAT_INF": self.qt_mat_inf,
            "QT_MAT_MED": self.qt_mat_med,
            "QT_MAT_PROF": self.qt_mat_prof,
            "NO_REGIAO": self.no_regiao,
            "CO_REGIAO": self.co_regiao,
            "NO_UF": self.no_uf,
            "SG_UF": self.sg_uf,
            "CO_UF": self.co_uf,
            "NO_MUNICIPIO": self.no_municipio,
            "CO_MUNICIPIO": self.co_municipio,
            "NO_MESORREGIAO": self.no_mesorregiao,
            "CO_MESORREGIAO": self.co_mesorregiao,
            "NO_MICRORREGIAO": self.no_microrregiao,
            "CO_MICRORREGIAO": self.co_microrregiao
        }


class UfSchema(Schema):
    pass

class Uf:
    def __init__(self,):
        pass
    def toDict(self):
        pass
    pass

class MunicipioSchema(Schema):
    pass

class Municipio:
    def __init__(self,):
        pass
    def toDict(self):
        pass
    pass

class MicrorregiaoSchema(Schema):
    pass

class Microrregiao:
    def __init__(self,):
        pass
    def toDict(self):
        pass
    pass

class MesorregiaoSchema(Schema):
    pass

class Mesorregiao:
    def __init__(self,):
        pass
    def toDict(self):
        pass
    pass