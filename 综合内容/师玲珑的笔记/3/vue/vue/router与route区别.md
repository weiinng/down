·����תʱ��
<router-link to="f">�����ת</router-link>

��ָ��������תʱ:
<router-link :to="{'name':'f',params:{'n':'qweersad'}}">�����ת</router-link>  ���˸�: !!!!!!!!!

��f.vue��������Ĵ���������

<$route.params.n>


��index.js��ҲҪ��
   {
      path: '/f/:n',
      name: 'f',
      component: f
    }



ָ������Ҫ��·��   ��Ҫָ�����ݴ�  ����ʱҲ�н��յĶ���  