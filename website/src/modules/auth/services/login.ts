import axiosInstance from '@/services/axios'
import store from '@/store'

import { StateUser, StateToken } from '@/modules/auth/types'

/**
 * user login service
 *
 * @param (string) email
 * @param (string) password
 */
export async function authenticate (
  email: string,
  password: string
): Promise<string | null> {
  try {
    await axiosInstance
      .post('/auth/login/', {
        email: email,
        password: password
      })
      .then((res: any) => {
        const user: StateUser = res.data.user
        const token: StateToken = {
          refresh: res.data.refresh,
          access: res.data.access
        }

        store.commit('setUser', user)
        store.commit('setToken', token)
        store.commit('setisAuthenticated', true)
      })
    return null
  } catch (error: any) {
    return error.response.data.detail
  }
}

const loginService = { authenticate }
export default loginService
