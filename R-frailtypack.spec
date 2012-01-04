%global packname  frailtypack
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.20
Release:          1%{?dist}
Summary:          General Frailty models using a semi_parametrical penalized likelihood estimation or a parametrical estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-20.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Frailtypack now fits several classes of frailty models using a penalized
likelihood estimation on the hazard function but also a parametrical
estimation. 1) A shared gamma frailty model and Cox proportional hazard
model. Left truncated, censored data and strata (max=2) are allowed. 
Clustered and recurrent survival times can be studied (the
Andersen-Gill(1982) approach has been implemented for recurrent events).
An automatic choice of the smoothing parameter is possible using an
approximated cross-validation procedure. 2) Additive frailty models for
proportional hazard models with two correlated random effects (intercept
random effect with random slope). 3) Nested frailty models for
hierarchically clustered data (with 2 levels of clustering) by including
two iid gamma random effects. 4) Joint frailty models in the context of
joint modelling of recurrent events with terminal event.

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
%doc %{rlibdir}/frailtypack/html
%doc %{rlibdir}/frailtypack/DESCRIPTION
%{rlibdir}/frailtypack/NAMESPACE
%{rlibdir}/frailtypack/Meta
%{rlibdir}/frailtypack/libs
%{rlibdir}/frailtypack/help
%{rlibdir}/frailtypack/docs
%{rlibdir}/frailtypack/INDEX
%{rlibdir}/frailtypack/data
%{rlibdir}/frailtypack/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.20-1
- initial package for Fedora