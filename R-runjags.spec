%global packname  runjags
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.9.2
Release:          1%{?dist}
Summary:          Interface utilities for JAGS (using BUGS syntax) and Apple Xgrid distributed computing clusters

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-coda R-lattice R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-coda R-lattice R-stats R-utils 

%description
A set of utility functions to run BUGS models using JAGS from within R,
and for JAGS or arbitrary R code submission to Xgrid clusters (requires
Mac OS X).  Automatic control of model run length, calculation of
autocorrealtion and Gelman Rubin statistic diagnostics, generation of
trace and density plots, calculation of DIC, and automatic retrieval of R
objects as data are supported.  Utilities to run user-supplied R functions
on Xgrid (using xapply as a replacement for lapply) are also included, and
do not require JAGS.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/runjags/html
%doc %{rlibdir}/runjags/CITATION
%doc %{rlibdir}/runjags/DESCRIPTION
%{rlibdir}/runjags/NAMESPACE
%{rlibdir}/runjags/xgrid
%{rlibdir}/runjags/Meta
%{rlibdir}/runjags/R
%{rlibdir}/runjags/help
%{rlibdir}/runjags/INDEX
%{rlibdir}/runjags/version_history.txt

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.9.2-1
- initial package for Fedora