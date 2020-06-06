#
# MIT License
#
# Copyright (c) 2020 Pablo Rodriguez Nava, @pablintino
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#


import os
import git
import base64

from app import Config


def get_ssh_command():
    git_ssh_cmd = '/usr/bin/ssh -i %s' % Config.SSH_IDENTITY if Config.SSH_IDENTITY else '/usr/bin/ssh'
    git_ssh_cmd = f'{git_ssh_cmd} -o "StrictHostKeyChecking=no"' if not Config.SSH_HOSTS_FILE else\
        f'{git_ssh_cmd} -o "UserKnownHostsFile={Config.SSH_HOSTS_FILE}"'
    return git_ssh_cmd


def create_file_in_repo(repo, file_name, encoded_data):
    file_content = base64.b64decode(encoded_data)
    abs_file_path = os.path.join(repo.working_dir, file_name)
    os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
    with open(abs_file_path, 'wb') as f:
        f.write(file_content)


def add_file_to_repo(file_name, encoded_data):
    repo = git.Repo(Config.REPO_PATH)
    git_ssh_cmd = get_ssh_command()
    with repo.git.custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
        repo.remotes.origin.fetch()
        repo.remotes.origin.pull()

        # Check if file already exists
        is_update = os.path.exists(file_name)

        create_file_in_repo(repo, file_name, encoded_data)
        repo.git.add(file_name)
        repo.index.commit('Auto commit to ' + ('add ' if not is_update else 'update ') + file_name)
        repo.remotes.origin.push(force=True)


def get_encoded_file_from_repo(file_name):
    abs_file_path = os.path.join(Config.REPO_PATH, file_name)
    with open(abs_file_path, "rb") as file:
        return base64.b64encode(file.read())
