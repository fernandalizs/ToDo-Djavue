import axios from "axios";
export default {
  getTasks: (callback) => {
    axios.get("http://localhost:8000/tasks/list").then((response) => {
      callback(response.data);
    });
  },
  createTask: (task, callback) => {
    const formData = new FormData();
    for (const k of Object.keys(task)) {
      formData.append(k, task[k]);
    }
    axios
      .post("http://localhost:8000/tasks/create/", formData)
      .then((response) => callback(response.data));
  },
  deleteTask: (task, callback) => {
    axios
      .delete(`http://localhost:8000/${task}`)
      .then((response) => callback(response.data));
  },
};
