%global packname  geneARMA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Simulate, model, and display data from a time-course microarray experiment with periodic gene expression

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Fit models for periodic gene expression to time-course microarray data in
a normal mixture model framework with mean approximated by a truncated
Fourier series and covariance structure modeled by an ARMA(p,q) process. 
Estimation is performed with the EM algorithm.

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
%doc %{rlibdir}/geneARMA/html
%doc %{rlibdir}/geneARMA/DESCRIPTION
%{rlibdir}/geneARMA/INDEX
%{rlibdir}/geneARMA/help
%{rlibdir}/geneARMA/Meta
%{rlibdir}/geneARMA/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora