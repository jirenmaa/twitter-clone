import axios from 'axios'
import store from '@/store'

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/',
  headers: {
    'Content-Type': 'application/json;charset=UTF-8'
  }
})

axiosInstance.interceptors.request.use(
  async config => {
    const token = await store.getters.getAccessToken
    // set authorization header
    if (config.headers && token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    Promise.reject(error)
  }
)

export default axiosInstance
