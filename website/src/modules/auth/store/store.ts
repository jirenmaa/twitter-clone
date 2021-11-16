import { StoreOptions } from 'vuex'
import { StateUser, StateToken, StateAuthen } from '../types'

const authentication: StoreOptions<any> = {
  state: () => ({
    user: null,
    token: null,
    authenticated: false
  }),
  mutations: {
    setUser (state: StateAuthen, user: StateUser): void {
      state.user = user
    },
    setToken (state: StateAuthen, token: StateToken): void {
      state.token = token
    },
    setisAuthenticated (state: StateAuthen, authenticated: boolean): void {
      state.authenticated = authenticated
    },
    resetState (state: StateAuthen): void {
      Object.assign(state, () => {
        return {
          user: {
            username: '',
            avatar: ''
          },
          token: {
            refresh: '',
            access: ''
          },
          authenticated: false
        }
      })
    }
  },
  getters: {
    getUser (state: StateAuthen): StateUser {
      return state.user
    },
    getAccessToken (state: StateAuthen): string {
      return state.token?.access
    },
    getRefreshToken (state: StateAuthen): string {
      return state.token?.refresh
    },
    getIsAuthenticated (state: StateAuthen): boolean {
      return state.authenticated
    }
  }
}

export default authentication
