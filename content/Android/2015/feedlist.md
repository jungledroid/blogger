Title: Android卡片新闻页优化实践
Category: Android
Tags: feed,listview
Date: 2015-11-8 23:00
Modified: 2015-11-8 23:00
Slug:feed-listview
Authors:Joe Zhang
Summary:本文分析了android新闻页ListView使用常见render的方式和拆分方式的实现过程
Status: published

以前的项目有展示Feed的需求，服务器端返回列表，有各种类型的Feed, 客户端根据返回的feed类型进行展示。
####常用的实现方法
###### MVP的方式
1. **Model**
   定义抽象Card，为每种Card定义一个Model，
2. **Presenter**
    定义基类CardPresenter,为每个Card定义一个Presenter，方法binderView(View convertView,ViewGroup parent)主要用于ListView 的getView调用，让数据和View绑定到一起。
3. **View**
   ListView,每一个Presenter代表一个item.
调用步骤：

    `ListView(Adapter getView)
    ->CardPresenter(binderView())
    -> View设置`

###### 问题：
- 加载比较慢,listview view 重用效率不高,Card较大时会出现卡顿
- 很多时候局部卡片要进行刷新不够流畅
- 某个卡片局部的显示和隐藏操作，会出现卡顿

最近又遇到相似的需求，于是决定使用不同的方式进行优化。google找到这篇博客https://code.facebook.com/posts/879498888759525/fast-rendering-news-feed-on-android/ 总结起来一句话：将逻辑单元拆分成多个视图单元。按这种思路重新实现了下，先上效果

![feedlist{1280x800}](http://7xo8z5.com1.z0.glb.clouddn.com/feedlist.gif)


###实现思路

###### Model
先定义一个接口Card代表所有的Card类型

        public interface Card {
            String getType();
        }
定义具体的**card**实体：

        public class ArticleCard implements Card{
            // ...

             public static String getTypeCode(){
                return "article";
            }
            // ...
        }

###### Presenter
这里由**FeedBinder**来担任这个角色.
**FeedPartDefine**代表一个Item视图单位：

    public interface FeedPartDefine {
        FeedBinder createBinder(Card card, FeedUpdateListener feedListener);
    }
每个不可拆分的FeedPartDefine内部定义了自己的binder,最终效果多个真正的Item,看起来属于一个Card, ListView的分割线我们定义成一个FeedPartDefine以方便控制，下面给出了一个代码：

    public class FeedGapSingleDefine implements FeedPartDefine {
        @Override
        public FeedBinder createBinder(Card card, FeedUpdateListener feedUpdateListener) {
            return new FeedGapBinder();
        }

        private static final class FeedGapBinder implements FeedBinder{
            @Override
            public void prepare() {}

            @Override
            public View bind(View convertView, ViewGroup parent) {
                int key = getViewResourceId();
                if(convertView == null){
                    convertView = LayoutInflater.from(parent.getContext()).inflate(key,parent,false);
                }
                return convertView;
            }

            @Override
            public void unbind() {}

            @Override
            public int getViewResourceId() {
                return R.layout.feed_gap;
            }
            
            @Override
            public View getView(int position,View convertView,ViewGroup parent) {
                return mFeedBinders.get(position).bind(convertView, parent);
            }
            @Override
            public int getViewType() {
                return 1;
            }
            // ...
        }
    }

parepare方法可以在解析完后做一些如String,span的初始化工作，unbind可以做一些释放和处理。
最终Adapter中getView:

         @Override
        public View getView(int position,View convertView,ViewGroup parent) {
            return mFeedBinders.get(position).bind(convertView, parent);
        }

另外， 常常一些Card需要展开和收起，听人说可以动态改变ListView的getCount大小，试了下效果不好，因为每次查找都需要循环计算需要跳过的Item数目，可以在Binder中持有一个隐藏的Binder,展开或收起去回调Adapter:

        @Override
        public void onChoiceChange(int checkPosition) {
            mIsExpand = !mIsExpand;
            if(mIsExpand){
                  mOnPollExpandListener.expandBinder(this, mResultBinder);
            }else{
                mOnPollExpandListener.collapseBinder(mResultBinder);
            }
        }

Adapter需要做的只是移除和添加该Binder:

    @Override
    public void expandBinder(FeedBinder choiceBinder, FeedBinder resultBinder) {
        mFeedBinders.add(mFeedBinders.indexOf(choiceBinder) + 1, resultBinder);
        notifyDataSetChanged();
    }

    @Override
    public void collapseBinder(FeedBinder resultBinder) {
        int removeIndex = mFeedBinders.indexOf(resultBinder);
        if(removeIndex != -1) {
            mFeedBinders.remove(removeIndex);
            mFeedBinders.get(removeIndex - 1).onRelativeBinderCollapse();
            notifyDataSetChanged();
        }
    }

总的来说效果还不错，比前面的方式流畅很多。代码地址https://github.com/jungledroid/feedlist， 如果你有别的思路  ，欢迎交流学习，本人邮箱fengyutubu@foxmail.com
