Q补充：
		con = {
			"id":1,
			"age__gt":9,
			"name__lt": 8
			"name__lt": 8
		}

		# 构造AND
		models.User.objects.filter(**con)

		# 构造复杂（条件写死）
		con = Q(Q(account=request.auth.user) & Q(status=0)) | Q(coupon__valid_begin_date__lte=ctime)
		models.User.objects.filter(con)


		# 构造负责（条件动态）
		q1 = Q()
		q1.connector = 'OR'
		for k,v in con.items():
			q1.children.append((k,v,))
		models.User.objects.filter(q1)