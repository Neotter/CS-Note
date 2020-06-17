<!--
 * @Author: Nettor
 * @Date: 2020-06-17 13:03:06
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-17 13:15:17
 * @Description: file content
-->

# POST 和 GET

GET 只请求数据，并不改变 Server 上的内容，因此仅仅把请求的内容放在 URL 里面就已经足够了。

POST 则相反，他提交数据给 Server，比如登录需要提交账号和密码，上传文件需要提交相应的文件，因此需 POST 往往需要更大的体积存放内容，URL 的长度是不够用也不安全的，所以 POST 的数据需要存放在报文的 body 里面。

但 POST 和 GET 其实本质上是相同的，GET 也可以数据存在 body 里面，POST 也可以不在 body 里面存内容。因此他俩都是认为规定的一种格式而已。
