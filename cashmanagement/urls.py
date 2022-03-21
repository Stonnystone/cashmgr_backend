from rest_framework import routers
from .api import AccountViewSet, CategoryViewSet, BalanceViewSet, OutflowViewSet
from .api import InflowViewSet, SplitViewSet, TransactionViewSet, RecurringTransactionViewSet


router = routers.DefaultRouter()

router.register('accounts', AccountViewSet, 'accounts')
router.register('categories', CategoryViewSet, 'categories')
router.register('balances', BalanceViewSet, 'balances')
router.register('inflows', InflowViewSet, 'inflows')
router.register('outflows', OutflowViewSet, 'outflows')
router.register('splits', SplitViewSet, 'splits')
router.register('transactions', TransactionViewSet, 'transactions')
router.register('recurringtransactions', RecurringTransactionViewSet, 'recurringtransactions')

urlpatterns = router.urls