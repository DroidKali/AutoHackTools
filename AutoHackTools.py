#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import wget
import json
import glob
import click
import shutil
import requests
from bs4 import BeautifulSoup
from art import text2art
banner = text2art("AutoHackTools")
print(banner)
print("\033[32m作者: \033[33m记忆里的纯真\033[0m")
print("\033[31mVersion: \033[34mv0.0.1\033[0m\n")

def download_and_extract_utils(output):
    try:
        wget.download("https://ghproxy.com/https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0-win-64bit-build1.zip", out=output)
    except Exception:
        print("Aria2下载失败！请检查网络连接。")
        sys.exit(0)
    if os.path.exists(os.path.join(output, "aria2-1.36.0-win-64bit-build1.zip")):
        shutil.unpack_archive(os.path.join(output, "aria2-1.36.0-win-64bit-build1.zip"), output)
        os.remove(os.path.join(output, "aria2-1.36.0-win-64bit-build1.zip"))
        print("\nAria2下载和解压缩完成。\n")
    try:
        # wget.download("https://mirrors.bfsu.edu.cn/github-release/cmderdev/cmder/LatestRelease/cmder.zip", out=output)
        os.system("{} {} -s 64 -d {}".format(os.path.join(output, r"aria2-1.36.0-win-64bit-build1\aria2c.exe"), "https://mirrors.bfsu.edu.cn/github-release/cmderdev/cmder/LatestRelease/cmder.zip", output))
    except Exception:
        print("Cmder最新版下载失败！请检查网络连接。")
        return
    if os.path.exists(os.path.join(output, "cmder.zip")):
        target_dir = os.path.join(output, "cmder")
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        shutil.unpack_archive(os.path.join(output, "cmder.zip"), os.path.join(output, "cmder"))
        os.remove(os.path.join(output, "cmder.zip"))
        print("\nCmder下载和解压缩完成。\n")

def download_and_extract_antsword(output):
    try:
        # wget.download("https://ghproxy.com/https://github.com/AntSwordProject/AntSword-Loader/releases/download/4.0.3/AntSword-Loader-v4.0.3-win32-x64.zip", out=output)
        os.system("{} {} -s 64 -d {}".format(os.path.join(output, r"aria2-1.36.0-win-64bit-build1\aria2c.exe"), "https://ghproxy.com/https://github.com/AntSwordProject/AntSword-Loader/releases/download/4.0.3/AntSword-Loader-v4.0.3-win32-x64.zip", output))
    except Exception as e:
        print("下载AntSword-Loader 失败！请检查网络连接。")
        return
    shutil.unpack_archive(os.path.join(output, "AntSword-Loader-v4.0.3-win32-x64.zip"), output)
    os.remove(os.path.join(output, "AntSword-Loader-v4.0.3-win32-x64.zip"))
    print("\nAntSword-Loader下载和解压缩完成。\n")

def download_and_extract_behinder(output, token):
    headers = {"Authorization": f"token {token}"} if token else None
    resp = requests.get("https://api.github.com/repos/rebeyond/Behinder/releases/latest", headers=headers)
    if resp.status_code != 200:
        print("获取 Behinder 最新版本信息失败！请检查网络连接和 token 设置。")
        return
    repo_json_obj = resp.json()
    tools_version = str(repo_json_obj["tag_name"])
    assets_lists = repo_json_obj["assets"]
    zipball_url = repo_json_obj["zipball_url"]
    if not tools_version or not assets_lists or not zipball_url:
        print(f"\n解析 Behinder 最新版本信息失败，请检查 GitHub API 返回数据。")
        return
    for assets in assets_lists:
        browser_download_url = assets["browser_download_url"]
        if "Behinder" in browser_download_url:
            try:
                filename = browser_download_url.split("/")[-1]
                url = "https://ghproxy.com/" + browser_download_url
                # wget.download(url, out=output)
                os.system("{} {} -s 64 -d {}".format(os.path.join(output, r"aria2-1.36.0-win-64bit-build1\aria2c.exe"), url, output))
            except Exception as e:
                print("下载 Behinder 最新版本失败！请检查网络连接。")
                return
    if os.path.exists(os.path.join(output, filename)):
        if not os.path.exists(os.path.join(output, "Behinder")):
            os.mkdir(os.path.join(output, "Behinder"))
        shutil.unpack_archive(os.path.join(output, filename), os.path.join(output, "Behinder"))
        os.remove(os.path.join(output, filename))
        print("\nBehinder下载和解压缩完成。\n")

def download_yakit(output):
    resp = requests.get("https://yaklang.oss-cn-beijing.aliyuncs.com/yak/latest/yakit-version.txt")
    if resp.status_code != 200:
        print("获取Yakit 最新版本信息失败！请检查网络连接。")
        return
    yakit_version = resp.text.replace("\n", "")
    try:
        # wget.download("https://yaklang.oss-cn-beijing.aliyuncs.com/yak/" + yakit_version + "/Yakit-" + yakit_version + "-windows-amd64.exe", out=output)
        os.system("{} {} -s 64 -d {}".format(os.path.join(output, r"aria2-1.36.0-win-64bit-build1\aria2c.exe"), "https://yaklang.oss-cn-beijing.aliyuncs.com/yak/" + yakit_version + "/Yakit-" + yakit_version + "-windows-amd64.exe", output))
    except Exception:
        print("下载Yakit最新版本失败！请检查网络连接。")
        return
    filename = "Yakit-" + yakit_version + "-windows-amd64.exe"
    if os.path.exists(os.path.join(output, filename)):
        print("\nYakit最新版本下载完成。")

def download_and_extract_goby(output):
    resp = requests.get("https://gobies.cn/api/version-list")
    if resp.status_code != 200:
        print("获取Goby最新版本信息失败！请检查网络连接。")
        return
    json_obj = json.loads(resp.text)
    json_str = json.dumps(json_obj)
    win_download_url = re.findall(r'"win_download_url": "(.+?)"', json_str)[0]
    try:
        # wget.download(win_download_url, out=os.path.join(output, "goby.zip"))
        os.system("{} {} -s 64 -d {}".format(os.path.join(output, r"aria2-1.36.0-win-64bit-build1\aria2c.exe"), '"' + win_download_url + '"', output))
    except Exception:
        print("下载Goby最新版本失败！请检查网络连接。")
        return
    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        if file.startswith('goby-win-x64-') and file.endswith('zip'):
            shutil.unpack_archive(os.path.join(output, file), output)
            os.remove(os.path.join(output, file))
            print("\nGoby下载和解压缩完成。\n")
    
@click.command()
@click.option("-o", "--output", required=True, type=click.Path(exists=False), help="请输入要安装的工具目录。")
@click.option("-t", "--token", type=str, help="请输入GitHub Token，用以突破GitHub API速率限制。")
def download_extract_hacktools(output, token=None):
    if not os.path.exists(output):
        os.mkdir(output)
    download_and_extract_utils(output)
    download_and_extract_antsword(output)
    download_and_extract_behinder(output, token)
    download_yakit(output)
    download_and_extract_goby(output)
    tools_list = [
        "https://github.com/projectdiscovery/dnsx",
        "https://github.com/projectdiscovery/naabu",
        "https://github.com/projectdiscovery/subfinder",
        "https://github.com/projectdiscovery/httpx",
        "https://github.com/projectdiscovery/katana",
        "https://github.com/projectdiscovery/uncover",
        "https://github.com/projectdiscovery/nuclei",
        "https://github.com/projectdiscovery/notify",
        "https://github.com/projectdiscovery/pdtm",
        "https://github.com/projectdiscovery/proxify",
        "https://github.com/ffuf/ffuf",
        "https://github.com/chaitin/xray"
    ]

    for url in tools_list:
        api_url = "https://api.github.com/repos/" + url.split("/")[-2] + "/" + url.split("/")[-1] + "/releases/latest"
        headers = {"Authorization": f"token {token}"} if token else None
        resp = requests.get(api_url, headers=headers)
        if resp.status_code != 200:
            print(f"\n获取 {url} 最新版本信息失败，状态码为 {resp.status_code}, 请检查网络连接和 token 设置。")
            continue 
        
        repos_json_obj = resp.json()
        tools_version = str(repos_json_obj["tag_name"])
        assets_lists = repos_json_obj["assets"]
        zipball_url = repos_json_obj["zipball_url"]
        if not tools_version or not assets_lists or not zipball_url:
            print(f"\n解析 {url} 最新版本信息失败，请检查 GitHub API 返回数据。")
            continue

        print(f"\n{url} 工具的版本为: \n{tools_version}")
        for assets in assets_lists:
            browser_download_url = assets["browser_download_url"]
            if "windows_amd64" in browser_download_url:
                if not os.path.exists(output):
                    os.mkdir(output)
                file_name = browser_download_url.split("/")[-1]
                file_path = os.path.join(output, file_name)
                if os.path.exists(file_path):
                    print(f"\n文件 {file_name} 已经存在，跳过下载。")
                    continue

                if not os.path.exists(file_path):
                    tools_download_url = "https://ghproxy.com/" + browser_download_url
                    print(f"\n正在下载 {url} 的 {tools_version} 版本...\n")
                    try:
                        # wget.download(tools_download_url, out=output)
                        os.system("{} {} -s 64 -d {}".format(os.path.join(output, r"aria2-1.36.0-win-64bit-build1\aria2c.exe"), tools_download_url, output))
                    except Exception as e:
                        print(f"\n下载 {url} 的 {tools_version} 版本失败: {str(e)}")
                
            for file in os.listdir(output):
                file_path = os.path.join(output, file)
                if os.path.isfile(file_path) and file.endswith(".zip"):
                    shutil.unpack_archive(file_path, output)

            zip_files = glob.glob(os.path.join(output, "*.zip"))
            md_files = glob.glob(os.path.join(output, "*.md"))
            license_files = glob.glob(os.path.join(output, "LICENSE"))
            files_to_delete = []
            files_to_delete.extend(zip_files)
            files_to_delete.extend(md_files)
            files_to_delete.extend(license_files)
            for file_path in files_to_delete:
                os.remove(file_path)

    git_source = [
        "https://github.com/sqlmapproject/sqlmap",
        "https://github.com/AntSwordProject/antSword",
        "https://github.com/shadow1ng/fscan",
        "https://github.com/pingc0y/URLFinder",
        "https://github.com/projectdiscovery/fuzzing-templates",
        "https://github.com/projectdiscovery/nuclei-templates",
        "https://github.com/maurosoria/dirsearch",
        "https://github.com/kelvinBen/AppInfoScanner",
        "https://github.com/rootclay/WMIHACKER",
        "https://github.com/XiaoliChan/wmiexec-Pro",
        "https://github.com/xmendez/wfuzz",
        "https://github.com/shmilylty/OneForAll"
    ]

    for url in git_source:
        url = "https://ghproxy.com/" + url
        git = os.path.join(output, r"cmder\vendor\git-for-windows\bin\git.exe")
        path = os.path.join(output, url.split("/")[-1])
        os.system("{} clone --depth=1 {} {}".format(git, url, path))
        
if __name__ == "__main__":
    download_extract_hacktools()
