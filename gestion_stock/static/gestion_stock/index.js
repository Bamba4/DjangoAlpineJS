function getInitialStock() {
  return {
    activeTab: 1,
    stockinitial: {},
    initialQuantity: 0,
    designation: '',
    quantity: '',
    stocks: [],
    loadInitialStocks() {
      let self = this
      axios
        .get('http://127.0.0.1:8000/stock/stock_initial/')
        .then(function (response) {
          self.stockinitial = response.data
          console.log(self.stockinitial)
        })
        .catch((error) => console.log(error))
      axios.get('http://127.0.0.1:8000/stock/stock_initial/all_commands').then(function (response) {
        self.stocks = response.data
      })
    },
    addInitialStock() {
      let self = this
      let params = new URLSearchParams()
      params.append('stockInitial', this.initialQuantity)
      axios
        .post('http://127.0.0.1:8000/stock/stock_initial/create/', params)
        .then(function (response) {
          self.stockinitial = response.data
          self.initialQuantity = 0
        })
        .catch((error) => console.log(error))
    },
    addStock() {
      let self = this
      let params = new URLSearchParams()
      params.append('designation', this.designation)
      params.append('quantity', this.quantity)
      axios
        .post('http://127.0.0.1:8000/stock/stock_initial/create/stock/', params)
        .then(function (response) {
          self.stocks.push(response.data)
          self.designation = ''
          self.quantity = 0
          console.log(self.stocks)
        })
        .catch((error) => console.log(error))
    },
    deleteStock(stockId) {
      let self = this
      axios
        .delete(`http://127.0.0.1:8000/stock/stock_initial/all_commands/${stockId}/delete`)
        .then(function () {
          console.log('Successfully deleted')

          let removeIndex = self.stocks.map((s) => s.id).indexOf(stockId)
          ~removeIndex && self.stocks.splice(removeIndex, 1)
          self.message = 'Stock is successfully deleted'
        })
        .catch((error) => {
          console.log(error)
        })
    },
  }
}
