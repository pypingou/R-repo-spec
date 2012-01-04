%global packname  DoE.base
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.22.8
Release:          1%{?dist}
Summary:          Full factorials, orthogonal arrays and base utilities for DoE packages

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.22-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-relimp R-utils R-graphics R-tcltk R-vcd R-conf.design 


BuildRequires:    R-devel tex(latex) R-stats R-relimp R-utils R-graphics R-tcltk R-vcd R-conf.design



%description
This package creates full factorial experimental designs and designs based
on orthogonal arrays for (industrial) experiments. Additionally, it
provides some utility functions used also by other DoE packages.

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
%doc %{rlibdir}/DoE.base/DESCRIPTION
%doc %{rlibdir}/DoE.base/html
%doc %{rlibdir}/DoE.base/NEWS
%{rlibdir}/DoE.base/R
%{rlibdir}/DoE.base/NAMESPACE
%{rlibdir}/DoE.base/help
%{rlibdir}/DoE.base/INDEX
%{rlibdir}/DoE.base/Meta
%{rlibdir}/DoE.base/LICENSE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.22.8-1
- initial package for Fedora