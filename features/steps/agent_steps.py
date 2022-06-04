from behave import *
from unrival_serverless import gen_key

@given('a public key')
def step_impl(context):
    assert gen_key() == "this is a public key"

@given('a domain has been created by the holder of this public key')
def step_impl(context):
    assert context.failed is False

@given(u'a child of this domain has the name name')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a child of this domain has the name name')


@given(u'I promise to have a name. is a promise made by this child')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I promise to have a name. is a promise made by this child')


@given(u'the child owner has one entity, the address of which is the public key used to create this domain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the child owner has one entity, the address of which is the public key used to create this domain')


@given(u'this domain has no name')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given this domain has no name')


@given(u'this domain has no parents')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given this domain has no parents')


@given(u'this domain makes the promise "I will keep any promise I make."')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given this domain makes the promise "I will keep any promise I make."')


@given(u'this domain makes the promise "If one of my ancestors makes a promise, then I also make that promise."')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given this domain makes the promise "If one of my ancestors makes a promise, then I also make that promise."')


@given(u'a child of this domain has the name promise')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a child of this domain has the name promise')


@given(u'I promise to have a status. is a promise made by this child')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I promise to have a status. is a promise made by this child')


@given(u'I promise to be fulfillable. is a promise made by this child')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I promise to be fulfillable. is a promise made by this child')


@given(u'a child of this domain has the name assessment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a child of this domain has the name assessment')


@given(u'I promise to be assessable. is a promise made by this child')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I promise to be assessable. is a promise made by this child')


@given(u'a child of this domain has the name owner')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a child of this domain has the name owner')


@given(u'I promise to assess honestly. is a promise made by this child')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I promise to assess honestly. is a promise made by this child')


@given(u'I promise to only own entities that keep their promises. is a promise made by this child')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I promise to only own entities that keep their promises. is a promise made by this child')


@given(u'a child domain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a child domain')


@given(u'a domain has one stakeholder')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a domain has one stakeholder')
