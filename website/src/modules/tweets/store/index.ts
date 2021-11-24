import { StoreOptions } from 'vuex'
import { StoreTweetReply, TweetAuthor } from '@/modules/tweets/types'

const resetState = (): StoreTweetReply => ({
  replying: false,
  tweetId: '',
  picture: '',
  content: '',
  author: {
    username: '',
    name: '',
    avatar: ''
  },
  success: false
})

const StoreTweetReply: StoreOptions<any> = {
  state: () => ({
    replying: null,
    tweetId: null,
    picture: null,
    content: null,
    author: null,
    success: null
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
    setSuccess (state: StoreTweetReply, success: boolean): void {
      state.success = success
    },
    setReplyState (state: StoreTweetReply, data: StoreTweetReply): void {
      state.replying = data.replying
      state.tweetId = data.tweetId
      state.author = data.author
      state.content = data.content
      state.picture = data.picture
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
