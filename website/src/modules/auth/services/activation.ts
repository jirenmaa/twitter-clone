import axiosInstance from '@/services/axios'

/**
 * user activation service
 */
export async function activate (key: string): Promise<boolean> {
  try {
    await axiosInstance.post('/auth/activate/', {
      signature: escape(key)
    })
    return true
  } catch (error: any) {
    return false
  }
}

export async function resetActivation (email: string): Promise<string | null> {
  try {
    await axiosInstance.post('/auth/reset_activation/', {
      email: email
    })
    return null
  } catch (error: any) {
    return error.response.data.detail
  }
}

const activationService = { activate, resetActivation }
export default activationService
