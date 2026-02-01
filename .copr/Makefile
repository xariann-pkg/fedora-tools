srpm:
	dnf -y install rpmdevtools spectool
	spectool -r -g $(spec)
	rpmbuild -D "_srcrpmdir $(outdir)" -D "_sourcedir ." -bs $(spec)
