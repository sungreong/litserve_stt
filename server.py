import os
import time
import whisper

import os
import time
import whisper
import litserve as ls


class WhisperLitAPI(ls.LitAPI):
    def __init__(self, model_size="turbo"):
        super().__init__()
        self.model_size = model_size

    def setup(self, device):
        # Load the OpenAI Whisper model. You can specify other models like "base", "small", etc.
        print(f"Loading Whisper model: {self.model_size} on {device}")
        self.model = whisper.load_model(self.model_size, device=device, download_root="/app/tmp")

    def decode_request(self, request):
        # Read the audio file from the request and save to disk
        path = f"tmp/{time.time()}"
        file = open(path, "wb")
        file.write(request["content"].file.read())
        file.close()
        return path

    def predict(self, audio_path):
        # Process the audio file and return the transcription result
        # options = whisper.DecodingOptions(language="ko", without_timestamps=True)
        result = self.model.transcribe(audio_path, temperature=0.1, language="ko")
        os.remove(audio_path)
        return result

    def encode_response(self, output):
        # Return the transcription text
        return {"transcription": output["text"]}


# 환경 변수 설정
PORT = int(os.environ.get("PORT", 9000))
HOST = os.environ.get("HOST", "0.0.0.0")
MODEL_SIZE = os.environ.get("MODEL_SIZE", "tiny")  # 기본 모델 크기는 large

# API 생성 및 서빙
if __name__ == "__main__":
    server = ls.LitServer(
        WhisperLitAPI(model_size=MODEL_SIZE),
        accelerator="cpu",
        #   spec=ls.OpenAISpec()
    )
    server.run(port=PORT, host=HOST)
