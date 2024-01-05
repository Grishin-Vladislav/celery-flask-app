import os

import cv2
from cv2 import dnn_superres
from celery import Celery

celery = Celery('upscaler',
                broker='redis://localhost:6377/0',
                backend='redis://localhost:6377/1',
                broker_connection_retry_on_startup=True)


@celery.task
def upscale(input_path: str,
            output_path: str,
            model_path: str = 'EDSR_x2.pb') -> None:
    """
    :param input_path: путь к изображению для апскейла
    :param output_path:  путь к выходному файлу
    :param model_path: путь к ИИ модели
    :return:
    """

    scaler = dnn_superres.DnnSuperResImpl_create()
    scaler.readModel(model_path)
    scaler.setModel("edsr", 2)
    image = cv2.imread(input_path)
    result = scaler.upsample(image)
    cv2.imwrite(output_path, result)
