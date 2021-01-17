# version_int = int(''.join(input().split('.')))) + 1
# new_version = '.'.join(str(version_int))


nums = int(input().replace(".", ""))

new_version = nums + 1

print('.'.join(list(str(new_version))))