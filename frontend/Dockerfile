FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy app source
COPY . .

# Build Next.js app
RUN npm run build

# Expose Port
EXPOSE 3000

# Start app
CMD ["npm", "start"]
