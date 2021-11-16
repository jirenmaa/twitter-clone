import axios from '@/services/axios'

import { Tweet, TweetReplies } from '@/modules/tweets/types'

export async function fetchPublicTweets (
  endpoint: string
): Promise<Array<Tweet>> {
  return axios.get(endpoint).then(response => {
    return response.data
  })
}

export async function fetchPublicDetailTweet (
  endpoint: string
): Promise<Array<Tweet>> {
  return axios.get(endpoint).then(response => {
    return [response.data]
  })
}

export async function fetchTweetDiscussion (
  endpoint: string
): Promise<Array<TweetReplies>> {
  return axios.get(endpoint).then(response => {
    return response.data
  })
}

const tweetServices = {
  fetchPublicTweets,
  fetchPublicDetailTweet,
  fetchTweetDiscussion
}
export default tweetServices
