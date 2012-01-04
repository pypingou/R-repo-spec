%global packname  HWEBayes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Bayesian investigation of Hardy-Weinberg Equilibrium via estimation and testing.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MCMCpack R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-MCMCpack R-mvtnorm 

%description
Estimation and testing of HWE using Bayesian methods. Three models are
currently considered: HWE, a model parameterized in terms of the allele
frequencies and a single inbreeding coefficient f, and the saturated
model. Testing is based on Bayes factors.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora