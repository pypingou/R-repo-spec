%global packname  dclone
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Data Cloning and MCMC Tools for Maximum Likelihood Methods

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-coda R-R2WinBUGS R-snow 

BuildRequires:    R-devel tex(latex) R-coda R-R2WinBUGS R-snow 

%description
Low level functions for implementing maximum likelihood estimating
procedures for complex models using data cloning and Bayesian Markov chain
Monte Carlo methods with support for JAGS, WinBUGS and OpenBUGS.  Parallel
MCMC computation is supported and can result in nearly linear speed-up.

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
%doc %{rlibdir}/dclone/html
%doc %{rlibdir}/dclone/COPYING
%doc %{rlibdir}/dclone/CITATION
%doc %{rlibdir}/dclone/DESCRIPTION
%{rlibdir}/dclone/Meta
%{rlibdir}/dclone/NAMESPACE
%{rlibdir}/dclone/ChangeLog
%{rlibdir}/dclone/data
%{rlibdir}/dclone/help
%{rlibdir}/dclone/R
%{rlibdir}/dclone/INDEX

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora