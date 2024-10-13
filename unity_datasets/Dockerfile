# Rust Dockerfile

# 기본 이미지로 Rust를 사용합니다.
FROM rust:latest

# 작업 디렉토리를 생성하고 설정합니다.
WORKDIR /usr/src/rust_app

# Cargo.toml과 Cargo.lock을 복사합니다.
COPY Cargo.toml Cargo.lock ./

# Rust 소스 코드를 복사합니다.
COPY src ./src

# 의존성을 빌드하여 캐싱합니다.
RUN cargo build --release

# 실제로 사용할 소스 코드를 복사합니다.
COPY src ./src

# 빌드를 수행합니다.
RUN cargo build --release

# 실행할 바이너리 파일을 설정합니다.
CMD ["./target/release/rust_app"]
