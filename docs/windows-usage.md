# Windows 使用说明

仓颉技能的内容理解和方法提取由宿主中的模型完成，命令行工具负责环境自检、编译、校验和版本管理。使用前需要 Python 3.10 或以上版本及 PyYAML。安装技能时应保留 SKILL.md 和 scripts、schemas、methodology、extractors、templates、docs 等配套目录，单独复制 SKILL.md 无法运行完整流程。

Windows 中建议从仓库根目录运行 `python scripts/cangjie_windows.py doctor` 检查环境。这个入口将 UTF-8 设置传给主进程和后续子进程，并沿用当前 Python 解释器。普通入口与子进程采用不同编码时，中文校验输出可能出现解码错误，仅在主进程使用 -X utf8 参数不能保证子进程继承相同设置。这个入口保留原命令行参数和退出码，不修改系统编码设置。

第一次使用可提供一章教材、一份实验讲义或一篇方法说明，并明确说“使用 cangjie-skill，将这份资料中的方法提取成可复用技能，重点用于实验数据处理，先从一章开始，采用单入口模式。”同时提供作者或讲者、版本或发布时间及使用目的。视频和播客需要先获得字幕或转写稿，不应仅凭书名或模型记忆提取内容。

在完成来源核查、覆盖检查和实际任务输出测试后，可运行 `python scripts/cangjie_windows.py compile --bundle books/<slug>/.cangjie/capabilities --out dist/<slug> --output single` 生成单入口技能，也可将最后的 single 改为 pack。占位符需替换为实际目录名。auto 模式会给出建议，确认后可加 --yes 采用建议。未完成语义验收的示例编译只说明工具链能够运行，不能据此宣称技能内容可靠。

编译产物需要安装到宿主的技能发现目录才能被调用，具体目录按宿主和现有配置确定。不要同时安装同一份资料的 single 和 pack 两种产物。后续调用时给出一个新的实际任务，核对技能是否被正确加载、是否按来源方法完成工作，以及输出是否符合预期。
