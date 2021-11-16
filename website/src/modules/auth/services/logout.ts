import axiosInstance from '@/services/axios'
import store from '@/store'
import router from '@/routes'

export async function logout (): Promise<void> {
  try {
    const refresh = await store.getters.getRefreshToken

    await axiosInstance.post('/auth/logout/', {
      refresh: refresh
    })

    await store.commit('resetState')
    await localStorage.removeItem('storage')
    router.push({ name: 'login' })
  } catch (error: any) {
    return error.response.data.detail
  }
}

const logoutService = { logout }
export default logoutService
