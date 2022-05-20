function todos() {
  return {
    tasks: [],
    taskTitle: '',
    message: '',
    loadTasks() {
      let self = this
      axios
        .get('http://127.0.0.1:8000/tasks/')
        .then(function (response) {
          self.tasks = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    addTask() {
      let self = this
      let params = new URLSearchParams()
      params.append('title', this.taskTitle)
      axios
        .post('http://127.0.0.1:8000/tasks/create/', params, {
          headers: { 'X-CSRFToken': '' },
        })
        .then(function (response) {
          self.tasks.push(response.data)
          self.taskTitle = ''
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deleteTask(taskId) {
      let self = this
      axios
        .delete(
          `http://127.0.0.1:8000/tasks/${taskId}/delete/`,
          {},
          {
            headers: { 'X-CSRFToken': '' },
          }
        )
        .then(function () {
          let removeIndex = self.tasks.map((task) => task.id).indexOf(taskId)
          ~removeIndex && self.tasks.splice(removeIndex, 1)
          self.message = 'Post is successfully deleted'
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateTask(task) {
      let self = this
      let params = new URLSearchParams()
      if (task.completed) {
        params.append('status', 0)
      } else {
        params.append('status', 1)
      }
      axios
        .post(`http://127.0.0.1:8000/tasks/${task.id}/update/`, params, {
          headers: { 'X-CSRFToken': '' },
        })
        .then(function () {
          task.completed = !task.completed
        })
        .catch((error) => console.log(error))
    },
  }
}
