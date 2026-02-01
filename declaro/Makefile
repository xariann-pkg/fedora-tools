srpm:
	dnf -y install rpmdevtools spectool
	spectool -r -g declaro.spec
	rpmbuild -D "_srcrpmdir $(outdir)" -D "_sourcedir ." -bs declaro.spec
