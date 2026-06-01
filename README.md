# NV3 SSD + Ultralytics Setup Guide

## 1. Go to NV3 drive

First, open terminal and navigate to the mount point:

```bash
cd /mnt/nvme
source ultralytics_env/bin/activate

mkdir -p /mnt/nvme/tmp
export TMPDIR=/mnt/nvme/tmp
