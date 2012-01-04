%global packname  BaM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99
Release:          1%{?dist}
Summary:          Functions and datasets for books by Jeff Gill.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-bayesm R-coda R-MASS R-stats R-mice R-survival R-foreign R-nnet 


BuildRequires:    R-devel tex(latex) R-bayesm R-coda R-MASS R-stats R-mice R-survival R-foreign R-nnet



%description
Books is "Bayesian Methods: A Social and Behavioral Sciences Approach,
Second Edition published by CRC Press, 2007"

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99-1
- initial package for Fedora