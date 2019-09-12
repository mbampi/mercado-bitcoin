# Mercado Bitcoin API Client for Python

API Client in Python for Mercado Bitcoin

## Installation

Run the following to install:
```python
    pip install mercado-bitcoin
```

## Usage

### Data API
```python
from mercado-bitcoin import DataAPI
import json

resp = DataAPI.day_summary('BTC', 2019, 9, 11).json()
print(json.dumps(resp, indent=2))
```
Response:
```json
{
  "date": "2019-09-11",
  "opening": 41772.12033,
  "closing": 41496.86984,
  "lowest": 41200,
  "highest": 41955.55,
  "volume": 11179626.56206287,
  "quantity": 269.18932163,
  "amount": 7917,
  "avg_price": 41530.72081153
}
```

### Trade API
```python
from mercado-bitcoin import TradeAPI
import json

TAPI_ID = <your_tapi_id>
TAPI_SECRET = <your_tapi_secret>
tapi = TradeAPI(TAPI_ID, TAPI_SECRET)

info = tapi.get_account_info()
print(json.dumps(info, indent=2))
```
Response
```json
{
  "response_data": {
    "balance": {
      "brl": {
        "available": "0.00000000",
        "total": "0.00000000"
      },
      "btc": {
        "available": "0.00000000",
        "total": "0.00000000",
        "amount_open_orders": 0
      },
      "ltc": {
        "available": "0.00000000",
        "total": "0.00000000",
        "amount_open_orders": 0
      },
      "bch": {
        "available": "0.00000000",
        "total": "0.00000000",
        "amount_open_orders": 0
      },
      "xrp": {
        "available": "0.00000000",
        "total": "0.00000000",
        "amount_open_orders": 0
      },
      "eth": {
        "available": "0.00000000",
        "total": "0.00000000",
        "amount_open_orders": 0
      }
    },
    "withdrawal_limits": {
      "brl": {
        "available": "20000.00",
        "total": "20000.00"
      },
      "btc": {
        "available": "10.00000000",
        "total": "10.00000000"
      },
      "ltc": {
        "available": "500.00000000",
        "total": "500.00000000"
      },
      "bch": {
        "available": "25.00000000",
        "total": "25.00000000"
      },
      "xrp": {
        "available": "20000.00000000",
        "total": "20000.00000000"
      },
      "eth": {
        "available": "70.00000000",
        "total": "70.00000000"
      }
    }
  },
  "status_code": 100,
  "server_unix_timestamp": "1568299534"
}
```

## Data API (API de Dados)

O acesso à API de Dados é público, não é necessário criar uma conta tampouco autenticar.

| Method | Description |
| ----- | ------------ |
| ticker | Retorna informações com o resumo das últimas 24 horas de negociações. |
| orderbook | Livro de ofertas é composto por duas listas: (1) uma lista com as ofertas de compras ordenadas pelo maior valor; (2) uma lista com as ofertas de venda ordenadas pelo menor valor. O livro mostra até 1000 ofertas de compra e até 1000 ofertas de venda. Uma oferta é constituída por uma ou mais ordens, sendo assim, a quantidade da oferta é o resultado da soma das quantidades das ordens de mesmo preço unitário. Caso uma oferta represente mais de uma ordem, a prioridade de execução se dá com base na data de criação da ordem, da mais antiga para a mais nova. |
| trades | Histórico de negociações realizadas. |
| day-summary | Retorna resumo diário de negociações realizadas. |

### Trade API (API de Negociacao)

- Para utilizar a API de negociações do Mercado Bitcoin são necessários: 
    - Criar uma conta
    - Gerar o PIN de Segurança
    - Gerar uma chave da API
    
 - O acesso à API é limitado por padrão ao máximo de 60 requisições a cada 60 segundos, por usuário e não por chave

| Method | Description |
| ----- | ------------ |
| list_system_messages | Método para comunicação de eventos do sistema relativos à TAPÌ, entre eles bugs, correções, manutenção programada e novas funcionalidades e versões. O conteúdo muda a medida que os eventos ocorrem. A comunicação externa, feita via Twitter e e-mail aos usuários da TAPI, continuará ocorrendo. Entretanto, essa forma permite ao desenvolvedor tratar as informações juntamente ao seus logs ou até mesmo automatizar comportamentos. |
| get_account_info | Retorna dados da conta, como saldos das moedas (Real, BCash, Bitcoin, Ethereum, Litecoin e XRP), saldos considerando retenção em ordens abertas, quantidades de ordens abertas por moeda digital, limites de saque/transferências das moedas. |
| get_order | Retorna os dados da ordem de acordo com o ID informado. Dentre os dados estão as informações das Operações executadas dessa ordem. Apenas ordens que pertencem ao proprietário da chave da TAPI pode ser consultadas. Erros específicos são retornados para os casos onde o order_id informado não seja de uma ordem válida ou pertença a outro usuário. |
| list_orders | Retorna uma lista de até 200 ordens, de acordo com os filtros informados, ordenadas pela data de última atualização. As operações executadas de cada ordem também são retornadas. Apenas ordens que pertencem ao proprietário da chave da TAPI são retornadas. Caso nenhuma ordem seja encontrada, é retornada uma lista vazia. |
| list_orderbook | Retorna informações do livro de negociações (orderbook) do Mercado Bitcoin para o par de moedas (coin_pair) informado. Diferente do método orderbook público descrito em /api-doc/#method_trade_api_orderbook, aqui são fornecidas informações importantes para facilitar a tomada de ação de clientes TAPI e sincronia das chamadas. Dentre elas, o número da última ordem contemplada (latest_order_id) e número das ordens do livro (order_id), descritos abaixo. Importante salientar que nesse método ordens de mesmo preço não são agrupadas como feito no método público. |
| place_buy_order | Abre uma ordem de compra (buy ou bid) do par de moedas, quantidade de moeda digital e preço unitário limite informados. A criação contempla o processo de confrontamento da ordem com o livro de negociações. Assim, a resposta pode informar se a ordem foi executada (parcialmente ou não) imediatamente após sua criação e, assim, se segue ou não aberta e ativa no livro. |
| place_sell_order | Abre uma ordem de venda (sell ou ask) do par de moedas, quantidade de moeda digital e preço unitário limite informados. A criação contempla o processo de confrontamento da ordem com o livro de negociações. Assim, a resposta pode informar se a ordem foi executada (parcialmente ou não) imediatamente após sua criação e, assim, se segue ou não aberta e ativa no livro. |
| place_market_buy_order | Abre uma ordem de compra (buy ou bid) do par de moedas com volume em reais limite informado. A criação contempla o processo de bloqueio do saldo para execução da ordem e confrontamento da ordem com o livro de negociações. Assim, a resposta pode informar se a ordem foi executada (parcialmente ou não) imediatamente após sua criação. Caso não seja possível executá-la totalmente por restrições no saldo disponível do usuário, o montante não executado é cancelado.|
| place_market_sell_order | Abre uma ordem de venda (sell ou ask) do par de moeda com quantidade da moeda digital informado. A criação contempla o processo de confrontamento da ordem com o livro de negociações. Assim, a resposta pode informar se a ordem foi executada (parcialmente ou não) imediatamente após sua criação. |
| cancel_order | Cancela uma ordem, de venda ou compra, de acordo com o ID e par de moedas informado. O retorno contempla o sucesso ou não do cancelamento, bem como os dados e status atuais da ordem. Somente ordens pertencentes ao próprio usuário podem ser canceladas. |
| get_withdrawal | Retorna os dados de uma transferência de moeda digital ou de um saque de Real (BRL). |
| withdraw_coin | Requisita pedido de transferência de moeda digital ou saque de Real. Assim, caso o valor de coin seja BRL, então realiza um saque para a conta bancária informada. Caso o valor seja uma criptomoeda, realiza uma transação para o endereço de moeda digital informado. |