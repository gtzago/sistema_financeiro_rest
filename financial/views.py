# -*- coding: utf-8 -*-

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets, generics

from financial.permissions import IsOwnerOrReadOnly
from financial.serializer import FinancialAccountSerializer, TransactionSerializer, UserSerializer

from .models import FinancialAccount, Transaction


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FinancialAccountViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = FinancialAccount.objects.all()
    serializer_class = FinancialAccountSerializer

    def perform_create(self, serializer):
        '''
         The user isn't sent as part of the serialized representation, but is
         instead a property of the incoming request. The way we deal with that
         is by overriding a .perform_create() method on our view, that
         allows us to modify how the instance save is managed, and handle any
         information that is implicit in the incoming request or requested URL.
        '''
        serializer.save(owner=self.request.user)
    # permission_classes = (permissions.AllowAny)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    # permission_classes = (permissions.AllowAny)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

#
#
# class IndexView(generic.CreateView):
#     template_name = 'financial/index.html'
#     context_object_name = 'accounts_list'
#     model = Account
#
#     form_class = AccountForm
#
#     def get_context_data(self, **kwargs):
#         '''
#             Adiciona parametros extras no template.
#         '''
#         context = super(IndexView, self).get_context_data(**kwargs)
#
#         context[self.context_object_name] = Account.objects.all()
#
#         return context
#
#     def get_success_url(self):
#         return reverse('financial:index')
#
#
# class TransactionCreateView(generic.CreateView):
#
#     '''
#         Esta classe eh utilizada para criar entradas na base de dados.
#     '''
#     model = Transaction
#     template_name = 'financial/create_transaction.html'
#     fields = ['date', 'description', 'acc_from', 'acc_to', 'value']
#     success_url = 'create'
#
#
# class TransactionUpdateView(generic.UpdateView):
#
#     '''
#         Esta classe eh utilizada para criar entradas na base de dados.
#     '''
#     model = Transaction
#     template_name = 'financial/update_transaction.html'
#     fields = ['date', 'description', 'acc_from', 'acc_to', 'value']
# success_url = '/financial'
#
#     def get_success_url(self):
#         return reverse('account_transactions')
#
#     def get_object(self, queryset=None):
#         obj = Transaction.objects.get(id=self.kwargs['pk'])
#         return obj
#
#
# class TransactionDeleteView(generic.DeleteView):
#
#     '''
#         Esta classe eh utilizada para deletar entradas da base de dados.
#     '''
#     model = Transaction
#
#     def get_success_url(self):
# retorna para a url com o parametro pk (id da conta)
#         return reverse('financial:account_transactions', kwargs={'pk': (self.kwargs.get('account_pk'))})
#
#     def get_context_data(self, **kwargs):
#         '''
#             Adiciona parametros extras no template.
#         '''
#         context = super(TransactionDeleteView, self).get_context_data(**kwargs)
# adiciona uma variavel chamada pk dentro de kwargs de acordo com o
# parametro passado na url ('pk').
#         context['account_pk'] = self.kwargs.get('account_pk')
#
#         return context
#
# def get(self, *args, **kwargs):
# return self.post(*args, **kwargs)
#
# def get_object(self, queryset=None):
# obj = Transaction.objects.get(id=self.kwargs['pk'])
# return obj
#
#
# class AccountDeleteView(generic.DeleteView):
#
#     '''
#         Esta classe eh utilizada para deletar entradas da base de dados.
#     '''
#     model = Account
#
#     def get_success_url(self):
#         return reverse('financial:index')
#
# def get(self, *args, **kwargs):
# return self.post(*args, **kwargs)
#
#
# class AccountDetailView(generic.CreateView):
#
#     '''
#         Esta classe eh utilizada para criar entradas na base de dados.
#     '''
#     model = Transaction
# formulario que esta sendo usado, descrito em outro arquivo (forms.py).
#     form_class = TransactionForm
#     template_name = 'financial/account_transactions.html'
# fields = ['date', 'description', 'acc_to', 'value'] # sao os campos
# utilizados no formulario. Caso eu nao apontasse qual form utilziar.
#     success_url = 'create'
#
#     def form_valid(self, form):
#         '''
#             Verifica erros entre os campos.
#         '''
#         transaction_form = form.save(
# commit=False)  # pega o formulario preenchido
#
# credit = form.cleaned_data.get("credit")  # pega o campo credito
# debit = form.cleaned_data.get("debit")  # pega o campo débito
#
# verifica se o usuário preencheu crédito ou débito e adequa os campos.
#         if debit:
#             transaction_form.acc_from = Account.objects.get(
#                 pk=self.kwargs.get('pk'))
#             transaction_form.acc_to = form.cleaned_data.get("acc_to")
#             transaction_form.value = debit
#         elif credit:
#             transaction_form.acc_to = Account.objects.get(
#                 pk=self.kwargs.get('pk'))
#             transaction_form.acc_from = form.cleaned_data.get("acc_to")
#             transaction_form.value = credit
#
# preciso verificar como levantar erros e não permitir que a conta
# debitada seja igual à conta creditada.
#         transaction_form.clean()
#         transaction_form.save()
#
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_context_data(self, **kwargs):
#         '''
#             Adiciona parametros extras no template.
#         '''
#         context = super(AccountDetailView, self).get_context_data(**kwargs)
# adiciona uma variavel chamada pk dentro de kwargs de acordo com o
# parametro passado na url ('pk').
#         context['object'] = Account.objects.get(pk=self.kwargs.get('pk'))
#
#         return context
#
#     def get_success_url(self):
# retorna para a url com o parametro pk (id da conta)
# return reverse('financial:account_transactions', kwargs={'pk':
# self.kwargs.get('pk')})
