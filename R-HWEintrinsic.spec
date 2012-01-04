%global packname  HWEintrinsic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Objective Bayesian Testing for the Hardy-Weinberg Equilibrium Problem

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-utils 

%description
This package implements the general (multiallelic) Hardy-Weinberg
equilibrium problem from an objective Bayesian testing standpoint. This
aim is achieved through the identification of a class of priors
specifically designed for this testing problem. A class of intrinsic
priors under the full model is considered. This class is indexed by a
tuning quantity, the training sample size, as discussed in Consonni,
Moreno and Venturini (2010). These priors are objective, satisfy Savage's
continuity condition and have proved to behave extremely well for many
statistical testing problems.

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
%doc %{rlibdir}/HWEintrinsic/html
%doc %{rlibdir}/HWEintrinsic/DESCRIPTION
%{rlibdir}/HWEintrinsic/INDEX
%{rlibdir}/HWEintrinsic/Meta
%{rlibdir}/HWEintrinsic/help
%{rlibdir}/HWEintrinsic/data
%{rlibdir}/HWEintrinsic/NAMESPACE
%{rlibdir}/HWEintrinsic/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora