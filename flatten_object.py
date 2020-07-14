# modified from https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10
# add ignore option, remove array flatten
def flatten_json(y, ignore=[]):
    out = {}
    def flatten(x, name=''):
        if name[:-1] in ignore:
            out[name[:-1]] = x
            return

        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# test

import json


def test1():
    a = {"a": {"b": 1}}
    result = flatten_json(a)
    assert json.dumps(result) == json.dumps({"a_b": 1})

def test2():
    a = {"a": {"b": 1}}
    result = flatten_json(a,["a"])
    assert json.dumps(result) == json.dumps({"a": {"b": 1}})

def test3():
    a = {"a": {"b": 1, "c": {"c1" : 1}}}
    result = flatten_json(a)
    assert json.dumps(result) == json.dumps({"a_b": 1, "a_c_c1" : 1})

def test4():
    a = {"a": {"b": 1, "c": {"c1" : 1}}}
    result = flatten_json(a,["a_c"])
    assert json.dumps(result) == json.dumps({"a_b": 1, "a_c" : {"c1" : 1}})
def test5():
    a = {"a": {"b": 1, "c": {"c1": 1}} , "b": {"b": 1, "c": {"c1": 1}} }
    result = flatten_json({"a": a["a"]}, ["a_c"])
    del a["a"]
    a.update(result)
    assert json.dumps(a) == json.dumps({"b": {"b": 1, "c": {"c1": 1}},"a_b": 1, "a_c" : {"c1" : 1} })



test1()
test2()
test3()
test4()
test5()
