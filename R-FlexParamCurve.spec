%global packname  FlexParamCurve
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{dist}
Summary:          Tools to Fit Flexible Parametric Curves

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nlme 

BuildRequires:    R-devel tex(latex) R-nlme 

%description
selfStart functions and model selection tools to fit parametric curves in
nls, nlsList and nlme frameworks.

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
%doc %{rlibdir}/FlexParamCurve/DESCRIPTION
%doc %{rlibdir}/FlexParamCurve/html
%{rlibdir}/FlexParamCurve/R
%{rlibdir}/FlexParamCurve/INDEX
%{rlibdir}/FlexParamCurve/Meta
%{rlibdir}/FlexParamCurve/help
%{rlibdir}/FlexParamCurve/NAMESPACE
%{rlibdir}/FlexParamCurve/data

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- Update to version 1.3

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora