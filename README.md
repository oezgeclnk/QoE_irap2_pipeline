# QoE_irap2_pipeline

For usage and detailed information see "Requirements_pipeline.docx"

Files in this repository:

youtube_framework_mp_008.py: The main pipeline code

tcpdump_capture.sh: you can access/modify the tcpdump capture options in this file

config.py: You can define/modify some parameters related to the pipeline (see documentation)

models folder: This is where you can find the available ML models. You can use both of them in the ML-module of the pipeline, you just have to change the name of the model file and the name of the scaler that belongs to the model in the pipeline code.

scalers folder: This is where you can find the scalers that is matching both models. Make sure that you use the ones that are matching.

emulation.py: This script is used for emulating bad network conditions during the operation. (see documentation)

QTSapp folder: Manuals for QTS App & Portal, as well as the apk file to install the app
