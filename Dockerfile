FROM node:18-alpine

WORKDIR /app

ARG APP_DIR=Image1

COPY ${APP_DIR}/package*.json ./

RUN npm install --omit=dev

COPY ${APP_DIR}/ ./

EXPOSE 3000

CMD ["npm", "start"]
