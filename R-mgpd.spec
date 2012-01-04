%global packname  mgpd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Functions for multivariate generalized Pareto distribution (MGPD of Type II)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-evd 

BuildRequires:    R-devel tex(latex) R-evd 

%description
Extends density functions to parametric multivariate generalized Pareto
distributions (MGPD of Type II), and provides fitting functions which
calculate maximum likelihood estimates for bivariate models (BGPD). There
are seven "classical" parametric dependence models within BGPD available:
logistic, negative logistic, bilogistic, negative bilogistic, Tajvidi's
generalised symmetric logistic, Dirichlet and mixed. Beyond these, two
novel asymmetric approaches giving absolutely continuous BGPD are
implemented as psi-logistic and psi-negative logistic models.

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
%doc %{rlibdir}/mgpd/DESCRIPTION
%doc %{rlibdir}/mgpd/html
%{rlibdir}/mgpd/Meta
%{rlibdir}/mgpd/INDEX
%{rlibdir}/mgpd/R
%{rlibdir}/mgpd/help
%{rlibdir}/mgpd/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora