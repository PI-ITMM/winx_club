import axios from 'axios'

// Default settings
axios.defaults.baseURL = 'http://localhost:8000'

// Response interceptor
axios.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (
      error.response &&
      error.response.status === 401
    ) {
      return
    }
    throw error
  }
)
