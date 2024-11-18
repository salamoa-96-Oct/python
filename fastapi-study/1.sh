#!/bin/bash

# 백엔드 디렉토리 생성
mkdir -p backend/app/api/v1/dependencies
mkdir -p backend/app/api/v1/endpoints
mkdir -p backend/app/api/v1/utils
mkdir -p backend/app/api/v2
mkdir -p backend/app/core
mkdir -p backend/app/crud
mkdir -p backend/app/db
mkdir -p backend/app/models
mkdir -p backend/app/schemas
mkdir -p backend/mysql-init

# 백엔드 파일 생성
touch backend/app/api/v1/__init__.py
touch backend/app/api/v1/endpoints/user.py
touch backend/app/api/v1/routers.py
touch backend/app/api/v1/utils/pagination.py
touch backend/app/core/config.py
touch backend/app/core/security.py
touch backend/app/crud/user.py
touch backend/app/db/base.py
touch backend/app/db/base_class.py
touch backend/app/db/session.py
touch backend/app/main.py
touch backend/app/models/__init__.py
touch backend/app/models/post.py
touch backend/app/models/user.py
touch backend/app/schemas/user.py
touch backend/docker-compose.yml
touch backend/mysql-init/init.sql
touch backend/requirements.txt

# 프론트엔드 디렉토리 생성
mkdir -p frontend/public
mkdir -p frontend/src/components

# 프론트엔드 파일 생성
touch frontend/README.md
touch frontend/package-lock.json
touch frontend/package.json
touch frontend/public/favicon.ico
touch frontend/public/index.html
touch frontend/public/logo192.png
touch frontend/public/logo512.png
touch frontend/public/manifest.json
touch frontend/public/robots.txt
touch frontend/src/App.css
touch frontend/src/App.js
touch frontend/src/App.test.js
touch frontend/src/components/PostForm.js
touch frontend/src/components/PostList.js
touch frontend/src/components/UserForm.js
touch frontend/src/components/UserList.js
touch frontend/src/index.css
touch frontend/src/index.js
touch frontend/src/logo.svg
touch frontend/src/reportWebVitals.js
touch frontend/src/setupTests.js

echo "프로젝트 디렉토리 구조가 생성되었습니다."