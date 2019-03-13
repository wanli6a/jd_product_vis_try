###动机
>* 前些天阴雨连绵，太阳也去流浪了，内裤袜子销量上微博热搜，于是爬取下京东的内裤的销量前十的店铺名称、价格、销量以及好评率，并使用pyecharts作简单可视化分析。
主要还是获取销量排序时的url，销量按钮是js触发的，于是在network里找type为script的信息，发现在request headers里的referer（response URL的那个url并不是，
而且特别长）
