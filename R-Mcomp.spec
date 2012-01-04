%global packname  Mcomp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.03
Release:          1%{?dist}
Summary:          Data from the M-competitions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-stats R-tseries R-forecast 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-tseries R-forecast 

%description
The 1001 time series from the M-competition (Makridakis et al. 1982) and
the 3003 time series from the IJF-M3 competition (Makridakis and Hibon,

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
%doc %{rlibdir}/Mcomp/DESCRIPTION
%doc %{rlibdir}/Mcomp/html
%{rlibdir}/Mcomp/Meta
%{rlibdir}/Mcomp/NAMESPACE
%{rlibdir}/Mcomp/R
%{rlibdir}/Mcomp/help
%{rlibdir}/Mcomp/INDEX
%{rlibdir}/Mcomp/data

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.03-1
- initial package for Fedora