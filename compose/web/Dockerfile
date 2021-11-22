FROM node:14.18-alpine

WORKDIR /usr/src

COPY website /usr/src

RUN yarn && yarn remove node-sass \
  && yarn add node-sass@^4.0.0 --sass-binary-name=linux-x64-83

CMD ["yarn", "serve"]
