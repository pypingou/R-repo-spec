%global packname  RLRsim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.10
Release:          1%{?dist}
Summary:          Exact (Restricted) Likelihood Ratio tests for mixed and additive models.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mgcv 

BuildRequires:    R-devel tex(latex) R-mgcv 

%description
Rapid, simulation-based exact (restricted) likelihood ratio tests for
testing the presence of variance components/nonparametric terms for models
fit with nlme::lme(),lme4::lmer(), mgcv::gamm() and SemiPar:spm()

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
%doc %{rlibdir}/RLRsim/DESCRIPTION
%doc %{rlibdir}/RLRsim/CITATION
%doc %{rlibdir}/RLRsim/html
%{rlibdir}/RLRsim/help
%{rlibdir}/RLRsim/Meta
%{rlibdir}/RLRsim/R
%{rlibdir}/RLRsim/libs
%{rlibdir}/RLRsim/NAMESPACE
%{rlibdir}/RLRsim/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.10-1
- initial package for Fedora