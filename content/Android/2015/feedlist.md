Title: Android卡片新闻页优化实践
Category: Android
Tags: feed,listview
Date: 2015-11-8 23:00
Modified: 2015-11-8 23:00
Slug:feed-listview
Authors:Joe Zhang
Summary: summary of metadata test
Status: published

以前的项目有展示Feed的需求，服务器端返回列表，有各种类型的Feed, 客户端根据返回的feed类型进行展示。
####常用的实现方法
###### MVP的方式
1. Model
   定义抽象Card，为每种Card定义一个Model，
2. Presenter
    定义基类CardPresenter,为每个Card定义一个Presenter，方法binderView(View convertView,ViewGroup parent)主要用于ListView 的getView调用，让数据和View绑定到一起。
3. View
   ListView,每一个Presenter代表一个item.
调用步骤：

`ListView(Adapter getView)
->CardPresenter(binderView())
-> View设置`

###### 问题：
- 加载比较慢,listview view 重用效率不高,Card较大时会出现卡顿
- 很多时候局部卡片要进行刷新不够流畅
- 某个卡片局部的显示和隐藏操作，会出现卡顿

最近又遇到相似的需求，于是决定使用不同的方式进行优化。google找到这篇博客https://code.facebook.com/posts/879498888759525/fast-rendering-news-feed-on-android/ 总结起来一句话：将逻辑单元拆分成多个视图单元。按这种思路重新实现了下，效果还不错。

###实现思路
###### Model
先定义一个接口Card代表所有的Card类型
        public interface Card {
            String getType();
        }
定义具体的card实体：
        public class ArticleCard implements Card{
            // ...

             public static String getTypeCode(){
                return "article";
            }
            // ...
        }

###### Presenter
