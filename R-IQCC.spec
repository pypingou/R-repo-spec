%global packname  IQCC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Improved Quality Control Charts

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-qcc R-MASS R-micEcon 

BuildRequires:    R-devel tex(latex) R-qcc R-MASS R-micEcon 

%description
Builds statistical control charts with exact limits for univariate and
multivariate cases.

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
%doc %{rlibdir}/IQCC/DESCRIPTION
%doc %{rlibdir}/IQCC/html
%{rlibdir}/IQCC/Meta
%{rlibdir}/IQCC/help
%{rlibdir}/IQCC/INDEX
%{rlibdir}/IQCC/data
%{rlibdir}/IQCC/R
%{rlibdir}/IQCC/NAMESPACE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora