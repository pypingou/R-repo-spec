%global packname  mspath
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.9
Release:          1%{?dist}
Summary:          Multi-state Path-Dependent Models in Discrete Time

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
Functions for fitting path-dependent (non-Markov) multi-state models to
categorical processes observed at arbitrary times, optionally with
misclassified responses, and covariates on transition or misclassification
rates.  Uses discrete-time approximation.  Based on the Jackson's msm
package v 0.3.1, with an interface as compatible as possible.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.9-1
- initial package for Fedora