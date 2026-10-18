# 参与维护

欢迎补充论文、阅读笔记与可核查的复现实验。

## 新增或修改论文

1. 先通过 Issue 提供完整题目、原文入口、研究方向与推荐理由。代码链接请说明是作者实现、演示还是第三方复现。
2. 编辑 `data/papers.json`；已有编号保持不变，新论文按下一编号追加。`data/source-titles.json` 保留首批 37 篇的原清单顺序。
3. 使用 Python 3.11 或更新版本运行：

   ```sh
   python3 scripts/build.py
   python3 scripts/check.py
   ```

4. 将数据与生成的 Markdown 一起提交 Pull Request。不要直接修改生成的论文卡片；阅读笔记可新增独立页面，并从相应卡片关联。

## 阅读笔记与实验

方法与结论注明原文位置。实验附上 [复现规范](wiki/Reproduction-Guide.md) 中的字段，说明是环境检查、方法演示还是论文实验。请不要上传数据凭据、未获分享授权的数据或论文全文。

## 发布 GitHub Wiki

主仓库保存可审阅的 Markdown 来源。维护者更新后运行 `python3 scripts/sync_wiki.py --push` 同步到 GitHub Wiki；这需要当前 `gh` 账号拥有目标仓库的写权限，并已在网页创建 Wiki 首页。该命令只更新本导航生成的同名页面，保留其他 Wiki 页面。
