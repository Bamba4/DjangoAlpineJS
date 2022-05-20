function getInitialStock() {
  return {
    stockinitial: {},
    initialQuantity: 0,
    loadInitialStocks() {
      let self = this
      axios
        .get('http://127.0.0.1:8000/stock/stock_initial/')
        .then(function (response) {
          self.stockinitial = response.data
          console.log(self.stockinitial)
        })
        .catch((error) => console.log(error))
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
  }
}
