# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os
import sys
sys.path.append("../../")

from libs.models.detectors.retinenet import build_whole_network
from tools.test_dota_base import TestDOTA
from libs.configs import cfgs
from libs.configs.DOTA.retinanet import cfgs_res50_dota_v15
from libs.configs.DOTA.retinanet import cfgs_res50_dota_v4



class TestDOTARetinaNet(TestDOTA):

    def eval(self):
        txt_name = '{}.txt'.format(self.cfgs.VERSION)
        real_test_img_list = self.get_test_image()

        retinanet = build_whole_network.DetectionNetworkRetinaNet(cfgs=self.cfgs,
                                                                  is_training=False)
        self.test_dota(det_net=retinanet, real_test_img_list=real_test_img_list, txt_name=txt_name)

        if not self.args.show_box:
            os.remove(txt_name)

if __name__ == '__main__':

    # tester = TestDOTARetinaNet(cfgs)
    tester = TestDOTARetinaNet(cfgs_res50_dota_v15)
    tester.eval()
    print(tester.numofprp / tester.s)


