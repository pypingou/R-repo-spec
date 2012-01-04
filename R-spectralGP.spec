%global packname  spectralGP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Approximate Gaussian processes using the Fourier basis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Routines for creating, manipulating, and performing Bayesian inference
about Gaussian processes in one and two dimensions using the Fourier basis
approximation: simulation and plotting of processes, calculation of
coefficient variances, calculation of process density, coefficient
proposals (for use in MCMC).  It uses R environments to store GP objects
as references/pointers.

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
%doc %{rlibdir}/spectralGP/CITATION
%doc %{rlibdir}/spectralGP/DESCRIPTION
%doc %{rlibdir}/spectralGP/html
%{rlibdir}/spectralGP/INDEX
%{rlibdir}/spectralGP/NAMESPACE
%{rlibdir}/spectralGP/help
%{rlibdir}/spectralGP/R
%{rlibdir}/spectralGP/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora