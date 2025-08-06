from helpers.application import app, api
from helpers.CORS import cors

from resources.IndexResource import IndexResource
from resources.CensoEscolarResource import CensoEscolarResource
from resources.EstadosResource import EstadosResource
from resources.InstituicaoResource import InstituicaoResource
from resources.InstituicoesResource import InstituicoesResource

cors.init_app(app)

api.add_resource(IndexResource, "/")
api.add_resource(EstadosResource, "/estados")
api.add_resource(CensoEscolarResource, "/censoescolar")
api.add_resource(InstituicoesResource, "/instituicoes")
api.add_resource(InstituicaoResource, "/instituicoes/<int:co_entidade>/<int:nu_ano_censo>")

if __name__ == "__main__":
    app.run(debug=True)
