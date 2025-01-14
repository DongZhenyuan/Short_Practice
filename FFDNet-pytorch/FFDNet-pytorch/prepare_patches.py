"""
构建 训练 和 验证 数据库
"""
import argparse
from dataset import prepare_data

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Building the training patch database")
	parser.add_argument("--gray", action='store_true', help='prepare grayscale database instead of RGB')

	# 预处理参数
	parser.add_argument("--patch_size", "--p", type=int, default=44, help="Patch size")
	parser.add_argument("--stride", "--s", type=int, default=20, help="Size of stride")
	parser.add_argument("--max_number_patches", "--m", type=int, default=None, help="Maximum number of patches")
	parser.add_argument("--aug_times", "--a", type=int, default=1, help="How many times to perform data augmentation")

	# Dir
	parser.add_argument("--trainset_dir", type=str, default=None, help='path of trainset')
	parser.add_argument("--valset_dir", type=str, default=None, help='path of validation set')
	args = parser.parse_args()

	if args.gray:
		if args.trainset_dir is None:
			args.trainset_dir = 'data/gray/train'
		if args.valset_dir is None:
			args.valset_dir = 'data/gray/Set12'
	else:
		if args.trainset_dir is None:
			args.trainset_dir = 'data/rgb/CImageNet_expl'
		if args.valset_dir is None:
			args.valset_dir = 'data/rgb/Kodak24'

	print("\n### Building databases ###")
	print("> Parameters:")
	for p, v in zip(args.__dict__.keys(), args.__dict__.values()):
		print('\t{}: {}'.format(p, v))
	print('\n')

	prepare_data(args.trainset_dir, args.valset_dir, args.patch_size, args.stride, args.max_number_patches, aug_times=args.aug_times, gray_mode=args.gray)
