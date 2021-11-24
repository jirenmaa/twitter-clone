import axiosInstance from '@/services/axios'

import { stopEvent, formatNumWithAbbreviation } from '@/utils/helper'

function trueOrFalse (string: string): boolean {
  return string === 'true'
}

export async function responseLikeUnlineTweet (
  event: Event,
  element: Element,
  tweetId: string
): Promise<string> {
  stopEvent(event)
  // check object is exist
  const objectModel = element.children[2].children[0]
  if (element === undefined) return ''

  // get element like count
  let elementCount = Number(objectModel.getAttribute('data-count'))
  const elementLiked = trueOrFalse(
    objectModel.getAttribute('data-liked') as string
  )

  // tweet is not liked yet, so like it
  if (elementLiked === false) {
    await axiosInstance.put(`/tweets/like/${tweetId}`).then(() => {
      elementCount += 1
      objectModel.classList.add('liked')
    })
  }

  // tweet are already liked, so unlike it
  if (elementLiked === true) {
    await axiosInstance.delete(`/tweets/like/${tweetId}`).then(() => {
      elementCount -= 1
      objectModel.classList.remove('liked')
    })
  }

  // update data-count attribute
  objectModel.setAttribute('data-count', elementCount.toString());
  // update like count in html element
  (objectModel
    .children[1] as HTMLElement).innerText = formatNumWithAbbreviation(
    elementCount
  )

  return (!!elementLiked).toString()
}

export async function responseReplyTweet (element: Element): Promise<void> {
  // check object is exist
  const domReply = element?.children[0].children[0]
  if (domReply !== undefined) {
    const replyCount = Number(domReply.getAttribute('data-count'))

    domReply.setAttribute('data-count', (replyCount + 1).toString())
    domReply.children[1].innerHTML = formatNumWithAbbreviation(replyCount + 1)
  }
}

export async function responseReplyDetailTweet (
  element: Element
): Promise<void> {
  // check object is exist
  const domReply = element?.children[0]
  if (domReply !== undefined) {
    const replyCount = Number(domReply.getAttribute('data-count'))
    console.log('replyCount')
    console.log(replyCount)

    domReply.setAttribute('data-count', (replyCount + 1).toString())
    domReply.children[0].innerHTML = formatNumWithAbbreviation(replyCount + 1)
  }
}

const actionServices = {
  responseLikeUnlineTweet
}
export default actionServices
