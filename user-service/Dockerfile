FROM golang:alpine

WORKDIR /user

COPY . .

RUN go mod tidy

RUN go build .

CMD ["go","run","main.go"]