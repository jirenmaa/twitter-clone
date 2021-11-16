import axiosInstance from '@/services/axios'
import { ErrorRegister } from '../types'

/**
 * user register service
 *
 * @param (string) email
 * @param (string) password
 */
export async function register (
  email: string,
  password: string
): Promise<ErrorRegister | null> {
  try {
    await axiosInstance
      .post('/auth/register/', {
        email: email,
        password: password
      })

    return null
  } catch (error: any) {
    return error.response.data.detail
  }
}

const registerService = { register }
export default registerService
