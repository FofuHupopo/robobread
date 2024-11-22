
FROM node:alpine

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

RUN yarn build

CMD ["yarn", "preview", "--host", "0.0.0.0", "--port", "3000"]