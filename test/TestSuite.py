__author__ = 'Kyle Harrison'

import unittest
import subprocess
import os

DOCKER_IMAGE = 'mrkyle7/ansible-server:latest'
BREAK = "==============="
CWD = os.getcwd()


def run_process(run_command):
    process = subprocess.Popen(run_command, cwd='..', stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE)
    out, err = process.communicate()
    exit_code = process.returncode
    return out, err, exit_code


def setUpModule():
    """Ensure Boot2Docker is running and build the latest docker image to test"""
    print BREAK
    print "Starting boot2docker"
    start_command = ['boot2docker', 'start']
    start_out, start_err, exit_code = run_process(start_command)
    print 'stdout: ' + start_out
    print 'stderr: ' + start_err

    print BREAK
    print "Building docker image"
    build_command = ['boot2docker', 'ssh', 'cd', CWD + '/..', '&&', 'docker', 'build', '-t', DOCKER_IMAGE, '.']
    out, err, exit_code = run_process(build_command)
    print 'stdout: ' + out
    print 'stderr: ' + err

    print BREAK

def tearDownModule():
    """
    Shut down Boot2docker once complete
    :return: None
    """
    print BREAK
    print "Shutting down boot2docker"
    stop_command = ['boot2docker', 'stop']
    out, err, exit_code = run_process(stop_command)
    print 'stdout: ' + out
    print 'stderr: ' + err


class DockerFileTests(unittest.TestCase):

    def setUp(self):
        self.docker_cmd = ['boot2docker', 'ssh', 'cd', CWD + '/..', '&&', 'docker', 'run', '-t', DOCKER_IMAGE,
                           '/bin/sh', '-c']

    def test_can_start_docker_image(self):
        self.docker_cmd.append('id')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^uid=0\(root\) gid=0\(root\) groups=0\(root\)', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_ansible_is_installed(self):
        self.docker_cmd.append('\"ansible --version\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^ansible\s+[\d\.]+', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_git_is_installed(self):
        self.docker_cmd.append('\"git --version\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^git\s+version\s+[\d\.]+', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_rsa_key_is_present(self):
        self.docker_cmd.append('\"ls /root/.ssh/id_rsa\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^/root/.ssh/id_rsa', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_rsa_pub_key_is_present(self):
        self.docker_cmd.append('\"ls /root/.ssh/id_rsa.pub\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^/root/.ssh/id_rsa.pub', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_known_hosts_is_present(self):
        self.docker_cmd.append('\"ls /root/.ssh/known_hosts\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^/root/.ssh/known_hosts', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_rsa_key_has_correct_permissions(self):
        self.docker_cmd.append('\"ls -l /root/.ssh/id_rsa\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^\-r\-\-\-\-\-\-\-\-', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_setup_ansible_script_is_present(self):
        self.docker_cmd.append('\"ls /root/setup-ansible.sh\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^/root/setup-ansible.sh', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_bashrc_is_present(self):
        self.docker_cmd.append('\"ls /root/.bashrc\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^/root/.bashrc', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_setup_ansible_script_has_correct_permissions(self):
        self.docker_cmd.append('\"ls -l /root/setup-ansible.sh\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^\-rwxr\-xr\-x', msg='Stdout: ' + out + 'Stderr: ' + err)

    def test_etc_ansible_playbooks_dir_is_present(self):
        self.docker_cmd.append('\"ls -d /etc/ansible/playbooks\"')
        command = self.docker_cmd
        out, err, exit_code = run_process(command)
        self.assertRegexpMatches(out, '^/etc/ansible/playbooks', msg='Stdout: ' + out + 'Stderr: ' + err)

if __name__ == '__main__':
    unittest.main()
