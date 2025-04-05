# Whisper Speech-to-Text API with LitServe

이 프로젝트는 OpenAI의 Whisper 모델을 사용하여 음성 인식(STT) API를 제공합니다. LitServe를 통해 쉽게 배포할 수 있습니다.

## 기능

- 음성 파일을 텍스트로 변환
- 다양한 언어 지원
- 쉬운 배포 및 확장

## 시작하기

### 필수 요구사항

- Docker
- FFmpeg (Docker 이미지에 포함됨)

### 도커로 실행하기

1. 이미지 빌드

```bash
docker build -t whisper-api .
```

2. 컨테이너 실행

```bash
docker run -p 9000:9000 whisper-api
```

이제 http://localhost:9000에서 API를 사용할 수 있습니다.

### 환경 변수

다음 환경 변수를 사용하여 설정을 변경할 수 있습니다:

- `PORT`: API 서버 포트 (기본값: 9000)
- `HOST`: API 서버 호스트 (기본값: 0.0.0.0)
- `MODEL_SIZE`: Whisper 모델 크기 (tiny, base, small, medium, large) (기본값: large)

예:
```bash
docker run -p 9000:9000 -e MODEL_SIZE=medium whisper-api
```

이 버전은 CPU만 사용하도록 설정되어 있습니다. 더 작은 모델(tiny, base, small)을 사용하면 처리 속도를 높일 수 있습니다.

## API 사용법

### 음성 인식 요청

POST 요청을 `/predict` 엔드포인트로 보내면 됩니다:

```javascript
const formData = new FormData();
formData.append("content", audioBlob);  // 오디오 파일 또는 Blob

fetch("http://localhost:9000/predict", {
  method: "POST",
  headers: {
    'Accept': 'application/json',
  },
  body: formData,
})
.then(response => response.json())
.then(data => {
  console.log(data.transcription);  // 변환된 텍스트
})
.catch(error => console.error(error));
```

## 라이센스

이 프로젝트는 MIT 라이센스 하에 있습니다. 