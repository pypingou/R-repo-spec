%global packname  rrBLUP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Ridge regression and other kernels for genomic selection

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
One application is to estimate marker effects by ridge regression;
alternatively, BLUPs can be calculated based on kinship.  The genetic
correlation between lines can be modeled using a marker-based, additive
relationship matrix, or via Gaussian and exponential kernels.

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
%doc %{rlibdir}/rrBLUP/DESCRIPTION
%doc %{rlibdir}/rrBLUP/html
%{rlibdir}/rrBLUP/Meta
%{rlibdir}/rrBLUP/R
%{rlibdir}/rrBLUP/INDEX
%{rlibdir}/rrBLUP/NAMESPACE
%{rlibdir}/rrBLUP/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3-1
- initial package for Fedora