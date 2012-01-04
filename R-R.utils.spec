%global packname  R.utils
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.9.4
Release:          1%{?dist}
Summary:          Various programming utilities

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.oo 

BuildRequires:    R-devel tex(latex) R-R.oo 

%description
This package provides utility classes and methods useful when programming
in R and developing R packages.

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
%doc %{rlibdir}/R.utils/html
%doc %{rlibdir}/R.utils/NEWS
%doc %{rlibdir}/R.utils/DESCRIPTION
%{rlibdir}/R.utils/data-ex
%{rlibdir}/R.utils/help
%{rlibdir}/R.utils/NAMESPACE
%{rlibdir}/R.utils/Meta
%{rlibdir}/R.utils/R
%{rlibdir}/R.utils/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.4-1
- initial package for Fedora