<!--
 * @Author: Nettor
 * @Date: 2020-06-08 17:09:21
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-08 17:27:50
 * @Description: file content
-->

# How to merge two difference repository

The basic principle is to fake a remote RepoB repository for a branch of RepoA, fatch down and merge the RepoB branch to RepoA.

There are two difference repository: RepoA and RepoB in the same dir.

    ..
    |-- RepoA
    |-- RepoB

Now we want to merge RepoB to RepoA.

    cd RepoA
    git remote add other ../RepoB
    git fetch other
    git checkout -b RepoB other/master
    git checkout master
    git merge RepoB

If you meet error like:

    fatal: refusing to merge unrelated histories

Add `--allow-unrelated-histories` to the last command.

    git merge RepoB --allow-unrelated-histories
