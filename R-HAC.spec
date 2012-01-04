%global packname  HAC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          Estimation, simulation and visualization of Hierarchical Archimedean Copulae (HAC)

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-copula R-mnormt 
Requires:         R-fBasics R-graphics 

BuildRequires:    R-devel tex(latex) R-copula R-mnormt
BuildRequires:    R-fBasics R-graphics 


%description
Package provides the estimation of the structure and the parameters,
simulation methods and structural plots of high-dimensional Hierarchical
Archimedean Copulae (HAC).

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
%doc %{rlibdir}/HAC/html
%doc %{rlibdir}/HAC/DESCRIPTION
%{rlibdir}/HAC/NAMESPACE
%{rlibdir}/HAC/INDEX
%{rlibdir}/HAC/Meta
%{rlibdir}/HAC/help
%{rlibdir}/HAC/R

%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.8-1
- initial package for Fedora