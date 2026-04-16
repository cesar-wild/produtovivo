FROM node:20-alpine

WORKDIR /app

# Install dependencies
COPY package.json ./
RUN npm install --production

# Copy application code
COPY src/ ./src/
COPY public/ ./public/
COPY product/ ./product/

EXPOSE 8082

ARG GIT_SHA=unknown
ARG BUILT_AT=unknown
ENV GIT_SHA=${GIT_SHA}
ENV BUILT_AT=${BUILT_AT}
ENV PORT=8082
ENV NODE_ENV=production

CMD ["node", "src/index.js"]
