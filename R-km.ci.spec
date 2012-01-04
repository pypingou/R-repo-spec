%global packname  km.ci
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Confidence intervals for the Kaplan-Meier estimator

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival R-stats 

BuildRequires:    R-devel tex(latex) R-survival R-stats 

%description
Computes various confidence intervals for the Kaplan-Meier estimator,
namely: Petos CI, Rothman CI, CI's based on Greenwoods variance, Thomas
and Grunkemeier CI and the simultaneous confidence bands by Nair and Hall
and Wellner.

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
%doc %{rlibdir}/km.ci/html
%doc %{rlibdir}/km.ci/DESCRIPTION
%{rlibdir}/km.ci/help
%{rlibdir}/km.ci/INDEX
%{rlibdir}/km.ci/Meta
%{rlibdir}/km.ci/data
%{rlibdir}/km.ci/NAMESPACE
%{rlibdir}/km.ci/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora