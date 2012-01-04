%global packname  VIF
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          VIF Regression: A Fast Regression Algorithm For Large Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements a fast regression algorithm for building linear
model for large data as defined in the paper "VIF-Regression: A Fast
Regression Algorithm for Large Data (2011), Journal of the American
Statistical Association, Vol. 106, No. 493: 232-247" by Dongyu Lin, Dean
P. Foster, and Lyle H. Ungar.

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
%doc %{rlibdir}/VIF/html
%doc %{rlibdir}/VIF/DESCRIPTION
%{rlibdir}/VIF/Meta
%{rlibdir}/VIF/NAMESPACE
%{rlibdir}/VIF/data
%{rlibdir}/VIF/R
%{rlibdir}/VIF/INDEX
%{rlibdir}/VIF/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora