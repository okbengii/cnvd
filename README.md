# 采集 cvnd 漏洞网站

1. cvnd 网站采用了反爬机制，使用js结合服务器返回的cookies生成新的cookies，再重新   发一次请求
2. 利用 fiddler 分析，发现 第一次请求 会返回 状态码 521，同时会返回 混淆的 生成c   ookies 的js 代码
3. 分析发现，js代码可能对 phantomjs 进行反爬，所以使用 selenium 驱动 firefox 浏    览器获取 cookies 
4. 但是 在你生成 headers 的时候，注意 headers 中的 user-agent 要和 你驱动的浏览    器一致

环境：

	python2.x selenium 3.x  firefox geckodriver.exe

	windows环境：将 firefox 的驱动配置到 path 环境变量下
	linux环境：还没尝试 
