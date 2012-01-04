%global packname  imprProbEst
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Minimum distance estimation in an imprecise probability model

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-inline R-lpSolve 

BuildRequires:    R-devel tex(latex) R-inline R-lpSolve 

%description
A minimum distance estimator is calculated for an imprecise probability
model. The imprecise probability model consists of upper coherent
previsions whose credal sets are given by a finite number of constraints
on the expectations. The parameter set is finite. The estimator chooses
that parameter such that the empirical measure lies next to the
corresponding credal set with respect to the total variation norm.

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
%doc %{rlibdir}/imprProbEst/DESCRIPTION
%doc %{rlibdir}/imprProbEst/CITATION
%doc %{rlibdir}/imprProbEst/html
%{rlibdir}/imprProbEst/R
%{rlibdir}/imprProbEst/NAMESPACE
%{rlibdir}/imprProbEst/help
%{rlibdir}/imprProbEst/INDEX
%{rlibdir}/imprProbEst/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora