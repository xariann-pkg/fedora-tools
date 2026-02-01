srpm:
	dnf -y install rpmdevtools spectool
	spectool -g $(spec)
	rpmbuild -D "_srcrpmdir $(outdir)" -D "_sourcedir ." -bs $(spec)
