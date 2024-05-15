# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install
RUN npm install axios
RUN npm install react-router-dom 

# Copy the rest of the application code to the container
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to start serving the React application
CMD ["npm", "start"]

