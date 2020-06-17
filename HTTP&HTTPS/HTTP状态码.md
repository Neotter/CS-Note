<!--
 * @Author: Nettor
 * @Date: 2020-06-17 11:51:34
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-17 12:43:51
 * @Description: file content
-->

# HTTP Status Code

## 五大类 HTTP 状态码

|     | 具体含义                                             | 常见状态码         |
| --- | ---------------------------------------------------- | ------------------ |
| 1xx | 提示，表示目前协议处理处于中间状态，还需要后续的操作 |
| 2xx | 成功，报文已经收到并被正确处理                       | 200，204，206      |
| 3xx | 重定向，资源位置发生变动，需要客户端重新发送请求     | 301,302,304        |
| 4xx | 客户端错误，请求有误，服务器无法处理                 | 400，403，404      |
| 5xx | 服务器错误，服务器在请求处理时内部发生了错误         | 500，501，502，503 |

### 2xx

- [200 OK] 成功

- [202 NoContent] 成功，但是木有 Body 数据

- [204 PartialContent] 成功，Body 数据太多需要下分块下载

### 3xx

- [301 MovePermanently] 链接永久重定向，说明请求资源不在了，重定向到新的 URL 进行访问

- [302 Found] 链接临时重定向，说明请求的资源还在，但是暂时用另一个 URL 访问

- [303 NotModified] 资源未修改，并且资源已缓存，所以重定向到已存在的缓存资源

### 4xx

- [400 BadRequest] Client 的请求报文有错误，

- [403 Forbidden] Server 禁止访问该资源，并不是 Client 的报文有错

- [404 NotFound] Server 找不到请求的资源，所以无法提供给 Client

#### 5xx

- [500 InternalServerError] Server 发生了错误，但是不告诉 Client

- [501 NoImplemented] Server 的功能尚未实现，类似于即将开业敬请期待

- [502 BadGateway] 通常用于网关服务器，表示 Server 本身正常，但是后面的 Server 出错了

- [503 ServiceUnavailable] "您拨的用户正忙，请稍后再试"
