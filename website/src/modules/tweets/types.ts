export type TweetAuthor = {
  username: string;
  name: string;
  avatar: string;
}

export type TweetResponse = {
  commented: boolean;
  liked: boolean;
  likes_count: number;
  comments_count: number;
}

export type Tweet = {
  id: string;
  author: TweetAuthor;
  content: string;
  pictures: string;
  tags: string;
  responses: TweetResponse;
  created_at: string;
  updated_at: string;
}

export type TweetReplies = {
  id: string;
  tweet: string;
  author: TweetAuthor;
  pictures: string;
  content: string;
  created_at: string;
  updated_at: string;
}

// tweet store reply
export type StoreTweetReply = {
  replying: boolean;
  tweetId: string;
  picture: string;
  content: string;
  success: boolean;
  author: TweetAuthor;
}
