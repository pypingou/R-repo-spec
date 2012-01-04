%global packname  RM2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0
Release:          1%{?dist}
Summary:          Revenue Management and Pricing Package

Group:            Applications/Engineering 
License:          GPL (version 3 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-msm 

BuildRequires:    R-devel tex(latex) R-msm 

%description
RM2 is a simple package that implements functions used in revenue
management and pricing environments.

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
%doc %{rlibdir}/RM2/DESCRIPTION
%doc %{rlibdir}/RM2/html
%{rlibdir}/RM2/R
%{rlibdir}/RM2/NAMESPACE
%{rlibdir}/RM2/help
%{rlibdir}/RM2/INDEX
%{rlibdir}/RM2/Meta

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0-1
- initial package for Fedora