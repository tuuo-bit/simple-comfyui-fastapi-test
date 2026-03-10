# Simple ComfyUI + FastAPI Test

A basic, containerized implementaion to run ComfyUI alongside a FastAPI backend using Docker Compose.

## 📁 Repository Structure

* **`comfyui/`** - Contains the Dockerfile and necessary scripts to build and run the ComfyUI container.
* **`fastapi/`** - Contains the FastAPI application (`main.py`) and its Dockerfile. This acts as the custom backend/API.
* **`docker-compose.yml`** - The orchestration file that links the `ui` (ComfyUI) and `api` (FastAPI) services together.

## 📋 Prerequisites

To run this project, you need:
1. **Docker & Docker Compose** installed on your machine.
2. **NVIDIA GPU** with up-to-date drivers.
3. **NVIDIA Container Toolkit**
4. **Place your ComfyUI workflows and models in /fastapi/workflows and /comfyui/models/{type} directories respectively**

## 🚀 Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/tuuo-bit/simple-comfyui-fastapi-test.git
   cd simple-comfyui-fastapi-test
   ```

2. **Build and start the services:**
    ```
    docker compose up --build
    ```

3. **Access the Web Interfaces:**
    - ComfyUI:http://localhost:8188
    - FastAPI Interactive (Swagger): http://localhost:5000/docs