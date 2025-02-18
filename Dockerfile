FROM clamav/clamav:1.4

RUN apk update && apk add --no-cache curl