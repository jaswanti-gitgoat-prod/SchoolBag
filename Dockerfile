FROM node:18-alpine

WORKDIR /app

ARG APP_DIR=Image1

COPY ${APP_DIR}/package*.json ./

RUN npm install --omit=dev

COPY ${APP_DIR}/ ./

EXPOSE 3000

CMD ["npm", "start"]

# ================ ARNICA SECURITY ANNOTATION BLOCK START ================
LABEL org.opencontainers.image.source="https://github.com/jaswanti-gitgoat-prod/SchoolBag"
LABEL org.opencontainers.image.path="Dockerfile"
# These automated labels, added by the security team, enhance traceability and security.
# For more details, see: https://docs.arnica.io/arnica-documentation/developers/adding-oci-tags-to-docker-images.
# To exclude this file, please replace this change with: #arnica-ignore followed by the dismissal reason.
# ================ ARNICA SECURITY ANNOTATION BLOCK END ================
