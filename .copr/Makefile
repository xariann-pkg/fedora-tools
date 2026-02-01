srpm:
	dnf -y install rpmdevtools spectool
	sed -i 's/SNAPSHOTDATE_PLACEHOLDER/$$(date +%Y%m%d)/' $(spec)
	spectool -g $(spec)
	rpmbuild -D "_srcrpmdir $(outdir)" -D "_sourcedir ." -bs $(spec)
