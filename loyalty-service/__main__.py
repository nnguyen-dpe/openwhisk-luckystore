def main(args):
    print('Invoked loyalty service')
    if args is None:
        return args
    print(args)
    return {
        'value': 'true'
    }