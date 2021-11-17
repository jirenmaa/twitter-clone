import { StoreOptions } from 'vuex'
import { StoreTweetReply, TweetAuthor } from '../types'

const resetState = (): StoreTweetReply => ({
  replying: false,
  tweetId: '',
  picture: '',
  content: '',
  author: {
    username: '',
    name: '',
    avatar: ''
  }
})

const StoreTweetReply: StoreOptions<any> = {
  state: () => ({
    replying: null,
    tweetId: null,
    picture: null,
    content: null,
    author: null
  }),
  mutations: {
    setReplying (state: StoreTweetReply, replying: boolean): void {
      state.replying = replying
    },
    setTweetId (state: StoreTweetReply, tweetId: string): void {
      state.tweetId = tweetId
    },
    setAuthor (state: StoreTweetReply, author: TweetAuthor): void {
      state.author = author
    },
    setContent (state: StoreTweetReply, content: string): void {
      state.content = content
    },
    setPicture (state: StoreTweetReply, picture: string): void {
      state.picture = picture
    },
    setResetState (state: StoreTweetReply): void {
      Object.assign(state, resetState())
    }
  },
  getters: {
    getReplying (state: StoreTweetReply): StoreTweetReply {
      return state
    }
  }
}

export default StoreTweetReply
