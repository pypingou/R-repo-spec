%global packname  plm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.7
Release:          1%{?dist}
Summary:          Linear Models for Panel Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-bdsmatrix R-nlme R-Formula R-MASS R-sandwich 

BuildRequires:    R-devel tex(latex) R-stats R-bdsmatrix R-nlme R-Formula R-MASS R-sandwich 

%description
A set of estimators and tests for panel data.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.7-1
- initial package for Fedora