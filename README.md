# Algorithmic-Trading

파이썬을 활용한 금융 데이터 분석 기초 학습 및 한국투자증권 API 기반 자동매매 시스템 구축 프로젝트입니다.

## 🚀 프로젝트 구성
본 프로젝트는 학습 단계와 실전 적용 단계로 나누어 진행하고 있습니다.

### 1. 학습 섹션 (Unit)
- **출처:** 조코딩/위키독스 금융 프로그래밍 가이드 기반 학습
- **내용:** - 파이썬 기초 문법 및 클래스/모듈 활용
  - `Pandas`를 이용한 시계열 데이터 처리
  - 기술적 지표(이동평균선, RSI 등) 계산 로직 구현 기초

### 2. 실전 섹션 
- **API:** 한국투자증권 KIS Developers API
- **내용:** `mojito` 라이브러리를 활용한 국내/미국 주식 실시간 시세 조회
  - 계좌 잔고 및 주문 현황 실시간 모니터링
  - 실제 계좌 연동을 통한 자동 매수/매도 시스템 구현

## 🛠 기술 스택
- **Language:** Python 3.x
- **Libraries:** `mojito`, `pandas`, `requests`, `python-dotenv`
- **IDE:** PyCharm
- **Version Control:** Git / GitHub

## 📋 주요 기능
- 실시간 국내 주식 시장 데이터 파싱
- 설정된 전략에 따른 자동 주문 (매수/매도)
- API Key 보안 관리 (`.env` 활용)

## ⚠️ 보안 주의사항
- API Key와 Secret은 `.env` 파일에서 관리하며, `.gitignore`를 통해 GitHub public 레포지토리에 노출되지 않도록 설정되어 있습니다.