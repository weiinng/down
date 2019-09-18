在本地读取图像文件加载进行头像显示



// 上传头像标签
<div class="form-group">
	<label class="col-sm-2 control-label">头像</label>
	<div class="col-sm-8">
		
		// 在上传文件的位置用一张图片覆盖住
		// 用label 标签的 for 方法将点击图片映射到 点击上传文件的 input 标签
		<label for="id_avatar">
		<img id="avatar-img" src="/static/img/default.png" alt="">		// 设置默认值作为默认头像
		</label>
		
		// 将真正的上传标签的input样式隐藏
		<input accept="image/*" type="file" name="avatar" id="id_avatar" style="display: none">
		
		// 错误信息的显示标签
		<span class="help-block"></span>
	</div>
</div>




//上传头像的大小稍微做下限制
#avatar-img {
    width: 80px;
    height: 80px;
}




// 找到头像的input标签绑定 change 事件 (值发生变化触发)
    $("#id_avatar").change(function () {
        // 1. 创建一个读取文件的对象
        var fileReader = new FileReader();
        // 取到当前选中的头像文件
        // console.log(this.files[0]);
        // 读取你选中的那个文件
        fileReader.readAsDataURL(this.files[0]);  // 读取文件是需要时间的
        fileReader.onload = function () {
            // 2. 等上一步读完文件之后才 把图片加载到img标签中
            $("#avatar-img").attr("src", fileReader.result);
        };
    });



