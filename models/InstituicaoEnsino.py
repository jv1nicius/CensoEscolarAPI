from marshmallow import Schema, fields, validate

#   Parametros das quantidades de matrículas
PARAMS_QT = {"allow_none": False, "strict": True, "dump_default": 0, "load_default": 0, "validate": validate.Range(min=0),
                                "error_messages": {"invalid": "Deve ser um número inteiro.", 
                                                "validator_failed": "A quantidade deve ser zero ou maior."}}

class InstituicaoEnsinoSchema(Schema):
    co_entidade = fields.Integer(required=True, error_messages={
                                 "required": "O Código da Entidade é obrigatório."})
    no_entidade = fields.String(validate=validate.Length(min=2, max=200),required=True, error_messages={
        "required": "O Nome da Entidade é obrigatório."})
    nu_ano_censo = fields.Integer(required=True, error_messages={"required": 
        "O Ano é obrigatório."})

    no_regiao = fields.String(required=True, error_messages={
        "required": "O Nome da Região é obrigatório."})
    co_regiao = fields.Integer(required=True, error_messages={
        "required": "Código da Região é obrigatório."})

    no_uf = fields.String(validate=validate.Length(min=2), required=True, error_messages={
        "required": "Nome da UF é obrigatório."})
    sg_uf = fields.String(validate=validate.Length(min=2, max=2), required=True, error_messages={
        "required": "Sigla da UF é obrigatória."})
    co_uf = fields.Integer(required=True, error_messages={
        "required": "Código da UF é obrigatório."})

    no_municipio = fields.String(required=True)
    co_municipio = fields.Integer(required=True)

    no_mesorregiao = fields.String(required=True)
    co_mesorregiao = fields.Integer(required=True)

    no_microrregiao = fields.String(required=True)
    co_microrregiao = fields.Integer(required=True)

    #-----------    MATRÍCULAS      -----------#
    qt_mat_bas = fields.Integer(**PARAMS_QT)
    qt_mat_eja = fields.Integer(**PARAMS_QT)
    qt_mat_esp = fields.Integer(**PARAMS_QT)
    qt_mat_fund = fields.Integer(**PARAMS_QT)
    qt_mat_inf = fields.Integer(**PARAMS_QT)
    qt_mat_med = fields.Integer(**PARAMS_QT)
    qt_mat_prof = fields.Integer(**PARAMS_QT)


class InstituicaoEnsino:
    def __init__(self, CO_ENTIDADE, NO_ENTIDADE, NU_ANO_CENSO, NO_REGIAO, CO_REGIAO, NO_UF, SG_UF, CO_UF, NO_MUNICIPIO, CO_MUNICIPIO,
                 NO_MESORREGIAO, CO_MESORREGIAO, NO_MICRORREGIAO, CO_MICRORREGIAO,
                 QT_MAT_BAS, QT_MAT_EJA, QT_MAT_ESP, QT_MAT_FUND, QT_MAT_INF, QT_MAT_MED, QT_MAT_PROF):
        
        self.co_entidade = CO_ENTIDADE
        self.no_entidade = NO_ENTIDADE
        self.nu_ano_censo = NU_ANO_CENSO
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
        self.qt_mat_bas = QT_MAT_BAS
        self.qt_mat_eja = QT_MAT_EJA
        self.qt_mat_esp = QT_MAT_ESP
        self.qt_mat_fund = QT_MAT_FUND
        self.qt_mat_inf = QT_MAT_INF
        self.qt_mat_med = QT_MAT_MED
        self.qt_mat_prof = QT_MAT_PROF

    def toDict(self):
        return {
            "co_entidade": self.co_entidade,
            "no_entidade": self.no_entidade,
            "ano": self.nu_ano_censo,
            "no_regiao": self.no_regiao,
            "co_regiao": self.co_regiao,
            "no_uf": self.no_uf,
            "sg_uf": self.sg_uf,
            "co_uf": self.co_uf,
            "no_municipio": self.no_municipio,
            "co_municipio": self.co_municipio,
            "no_mesorregiao": self.no_mesorregiao,
            "co_mesorregiao": self.co_mesorregiao,
            "no_microrregiao": self.no_microrregiao,
            "co_microrregiao": self.co_microrregiao,
            "qt_mat_bas": self.qt_mat_bas,
            "qt_mat_eja": self.qt_mat_eja,
            "qt_mat_esp": self.qt_mat_esp,
            "qt_mat_fund": self.qt_mat_fund,
            "qt_mat_inf": self.qt_mat_inf,
            "qt_mat_med": self.qt_mat_med,
            "qt_mat_prof": self.qt_mat_prof,
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