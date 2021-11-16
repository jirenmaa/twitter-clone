import createPersistedState from 'vuex-persistedstate'

const stateAuth = createPersistedState({
  paths: ['auth'],
  key: 'storage',
  storage: window.sessionStorage
})

export default stateAuth
