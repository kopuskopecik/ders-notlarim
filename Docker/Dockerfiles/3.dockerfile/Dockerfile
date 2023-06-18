FROM node:10
WORKDIR /usr/src/app
COPY package.json .
# Bu kismin ustte olmasi onemli
RUN npm install
COPY server.js .
EXPOSE 8080
CMD ["npm", "start"]