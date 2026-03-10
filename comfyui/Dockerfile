FROM python:3.12
WORKDIR /app
ADD . .

RUN apt-get -y update && apt-get install -y git
RUN git clone https://github.com/comfyanonymous/ComfyUI.git
RUN pip install -r ComfyUI/requirements.txt
RUN git clone https://github.com/ltdrdata/ComfyUI-Manager ComfyUI/custom_nodes/comfyui-manager
RUN chmod +x move_models.sh && /bin/bash move_models.sh

EXPOSE 8188
CMD ["python", "ComfyUI/main.py", "--listen", "0.0.0.0", "--port", "8188"]