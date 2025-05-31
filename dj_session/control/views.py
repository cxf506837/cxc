# cbv/views.py
import logging
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction
from django.db.models import F
from .models import Product, Order

logger = logging.getLogger(__name__)

class SeckillView(View):
    template_name = 'seckill.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})

    def post(self, request):
        product_id = request.POST.get('product_id')
        username = request.POST.get('username', '匿名用户')

        try:
            with transaction.atomic():
                product = Product.objects.select_for_update().get(id=product_id)
                if product.stock <= 0:
                    return HttpResponse("库存不足", status=400)
                if not product.is_on_sale:
                    return HttpResponse("商品未开启秒杀", status=400)

                # 减少库存
                product.stock = F('stock') - 1
                product.save(update_fields=['stock'])

                # 创建订单
                Order.objects.create(
                    product=product,
                    user=username,
                    quantity=1
                )

                return HttpResponse("秒杀成功！")
        except Product.DoesNotExist:
            return HttpResponse("商品不存在", status=404)
        except Exception as e:
            logger.error(f"秒杀失败: {e}")
            return HttpResponse("系统错误，请稍后再试", status=500)