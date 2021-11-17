import axios from '@/services/axios'

import { UserInfo } from '../types'

export async function fetchUserInfo (username: string): Promise<UserInfo> {
  return axios.get(username).then(response => {
    return response.data
  })
}

const userServices = {
  fetchUserInfo
}
export default userServices
