# React build
FROM node:12-alpine as build

RUN mkdir /muse
WORKDIR /muse
COPY ./package.json .

RUN npm install

COPY . .
RUN npm run build


# NGINX serve
FROM nginx:1.20-alpine

COPY --from=build /muse/build /var/www/react
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

CMD ["nginx", "-g", "daemon off;"]
