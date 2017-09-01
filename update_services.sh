cp kp_asc_4pl_controller/kp_asc_4pl_controller.service /lib/systemd/system/
chmod 664 /lib/systemd/system/kp_asc_4pl_controller.service

cp kp_asc_4pl_webapp/kp_asc_4pl_webapp.service /lib/systemd/system
chmod 664 /lib/systemd/system/kp_asc_4pl_controller.service

systemctl daemon-reload
systemctl enable kp_asc_4pl_webapp.service
systemctl enable kp_asc_4pl_controller.service
systemctl restart kp_asc_4pl_webapp.service
systemctl restart kp_asc_4pl_controller.service