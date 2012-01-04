%global packname  mpm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.18
Release:          1%{?dist}
Summary:          Multivariate Projection Methods

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-18.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-KernSmooth 

BuildRequires:    R-devel tex(latex) R-MASS R-KernSmooth 

%description
Exploratory graphical analysis of multivariate data, specifically gene
expression data with different projection methods: principal component
analysis, correspondence analysis, spectral map analysis.

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
%doc %{rlibdir}/mpm/html
%doc %{rlibdir}/mpm/NEWS
%doc %{rlibdir}/mpm/DESCRIPTION
%{rlibdir}/mpm/data
%{rlibdir}/mpm/R
%{rlibdir}/mpm/NAMESPACE
%{rlibdir}/mpm/TODO
%{rlibdir}/mpm/INDEX
%{rlibdir}/mpm/Meta
%{rlibdir}/mpm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.18-1
- initial package for Fedora