#! /usr/bin/env bash

# Let the DB start
sleep 1;



if [ -n "$APP_MIGRATIONS_ENABLED" ]; then
    # Run migrations
    echo "Running migrations scripts"
    flask db upgrade -d /app/migrations/
fi

if [ -z "$(ls -A "$REPO_PATH")" ] && [ "$NODE_TYPE" = "web" ]; then
  echo "Initialazing Git local repository"
  GIT_CMD="/usr/bin/ssh"

  if [ ! -z "$SSH_IDENTITY" ]; then
    GIT_CMD="${GIT_CMD} IdentitiesOnly=yes -i ${SSH_IDENTITY}"
  fi

  if [ -z "$SSH_HOSTS_FILE" ]; then
    GIT_CMD="${GIT_CMD} -o UserKnownHostsFile=${SSH_HOSTS_FILE}"
  else
    GIT_CMD="${GIT_CMD} -o StrictHostKeyChecking=no"
  fi
  if [ -z "$REPO_BRANCH" ]; then
    REPO_BRANCH="master"
  fi

  GIT_SSH_COMMAND="${GIT_CMD}" git clone --branch "$REPO_BRANCH" "$REPO_URL" "$REPO_PATH"
fi
