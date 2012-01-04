%global packname  HSROC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Joint meta-analysis of diagnostic test sensitivity and specificity with or without a gold standard reference test

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-coda R-MASS R-MCMCpack 

BuildRequires:    R-devel tex(latex) R-lattice R-coda R-MASS R-MCMCpack 

%description
This package implements a model for joint meta-analysis of sensitivity and
specificity of the diagnostic test under evaluation, while taking into
account the possibly imperfect sensitivity and specificity of the
reference test. This hierarchical model accounts for both within and
between study variability. Estimation is carried out using a Bayesian
approach, implemented via a Gibbs sampler. The model can be applied in
situations where more than one reference test is used in the selected

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
%doc %{rlibdir}/HSROC/DESCRIPTION
%doc %{rlibdir}/HSROC/html
%{rlibdir}/HSROC/NAMESPACE
%{rlibdir}/HSROC/R
%{rlibdir}/HSROC/INDEX
%{rlibdir}/HSROC/help
%{rlibdir}/HSROC/data
%{rlibdir}/HSROC/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora