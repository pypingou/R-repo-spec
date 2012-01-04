%global packname  CausalGAM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Estimation of Causal Effects with Generalized Additive Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gam 

BuildRequires:    R-devel tex(latex) R-gam 

%description
This package implements various estimators for average treatment
effects---an inverse probability weighted (IPW) estimator, an augmented
inverse probability weighted (AIPW) estimator, and a standard regression
estimator---that make use of generalized additive models for the treatment
assignment model and/or outcome model.

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
%doc %{rlibdir}/CausalGAM/DESCRIPTION
%doc %{rlibdir}/CausalGAM/COPYING
%doc %{rlibdir}/CausalGAM/html
%{rlibdir}/CausalGAM/NAMESPACE
%{rlibdir}/CausalGAM/R
%{rlibdir}/CausalGAM/INDEX
%{rlibdir}/CausalGAM/help
%{rlibdir}/CausalGAM/Meta
%{rlibdir}/CausalGAM/LICENSE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora