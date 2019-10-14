## RediSearch资料整理

###### 简介

RediSearch是一个高性能的全文搜索引擎，可作为一个Redis Module 运行在Redis上，是由RedisLabs团队开发的。

特点是：Faster, in-memory, highly available full text search

项目地址：https://github.com/RedisLabsModules/RediSearch

官网：http://redisearch.io

***

###### 官方描述

```python
Redisearch implements a search engine on top of redis, but unlike other redis search libraries, it does not use internal data structures like sorted sets.
Inverted indexes are stored as a special compressed data type that allows for fast indexing and search speed, and low memory footprint.
This also enables more advanced features, like exact phrase matching and numeric filtering for text queries, that are not possible or efficient with traditional redis search approaches.

# redisearch在redis之上实现了一个搜索引擎，但与其他redis搜索库不同，它不使用内部数据结构，如排 # 序集。
# 反向索引存储为一种特殊的压缩数据类型，允许快速索引和搜索速度，以及低内存占用。
# 这还支持更高级的功能，例如精确的短语匹配和文本查询的数字过滤，这些功能在传统的redis搜索方法中 # 是不可能或不高效的。
```

***

###### 主要特点

高性能的全文搜索引擎（Faster, in-memory, highly available full text search），可作为Redis Module运行在Redis上。但是它与其他Redis搜索库不同的是，它不使用Redis内部数据结构，例如：集合、排序集（ps.后面会写一篇基于Redis的数据结构来设计搜索引擎），Redis原声的搜索还是有很大的局限性，简单的分词搜索是可以满足，但是应用到复杂的场景就不太适合。

- Full-Text indexing of multiple fields in documents.
- Incremental indexing without performance loss.
- Document ranking (provided manually by the user at index time).
- Field weights.
- Complex boolean queries with AND, OR, NOT operators between sub-queries.
- Prefix matching in full-text queries.
- Auto-complete suggestions (with fuzzy prefix suggestions)
- Exact Phrase Search.
- Stemming based query expansion in many languages (using Snowball).
- Support for logographic (Chinese, etc.) tokenization and querying (using Friso)
- Limiting searches to specific document fields (up to 128 fields supported).
- Numeric filters and ranges.
- Geographical search utilizing redis’ own GEO commands.
- Supports any utf-8 encoded text.
- Retrieve full document content or just ids.
- Automatically index existing HASH keys as documents.
- Document Deletion (Update can be done by deletion and then re-insertion).
- Sortable properties (i.e. sorting users by age or name).

下面是中文版本

- 多个字段的文档的全文索引。
- 没有性能损失增量索引。
- 文档排名(由用户提供手动指数时间)。
- 字段权重。
- 在子查询之间使用AND，OR，NOT运算符进行复杂的布尔查询。
- 前缀匹配全文查询。
- 自动完成建议以模糊前缀(建议)
- 准确短语搜索。
- 阻止基于查询扩展多种语言(使用Snowball)。
- 支持语标的(中国等)标记和查询(使用Friso)
- 将搜索限制在特定的文档字段(128字段支持)。
- 数字过滤器和范围。
- 利用redis自己的GEO命令进行地理搜索。
- 支持任何utf-8编码的文本。
- 获取完整的文档内容或者只是id。
- 自动索引现有HASH keys文件。
- 文档删除(更新可以通过删除然后re-insertion)。
- 可排序属性（即按年龄或名称对用户进行排序）。

***

###### 缺陷

+ 暂不支持拼写更正
+ 暂不支持集合

+++

###### 性能比较

**吞吐率比较**

![1](D:\学习文件\python第八月\笔记\RediSearch\1.jpg)

**多个单词搜索延迟**

![2](D:\学习文件\python第八月\笔记\RediSearch\2.jpg)

**两个单词搜索**

![3](D:\学习文件\python第八月\笔记\RediSearch\3.jpg)

***

###### 总结

从数据上看，使用RediSearch的吞吐量高、延迟低，但是相比于ElasticSearch和Solr支持的特性上还有些欠缺比如：中文的模糊搜索支持的不是很好，但是其性能很高在某些场景是可以作为搜索引擎的替代方案来试用。 