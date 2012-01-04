%global packname  orth
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          Multivariate Logistic Regressions Using Orthogonalized Residuals.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Performs multivariate logistic regressions by way of orthogonalized
residuals. As a special case, the methodology recasts alternating logistic
regressions in a way that is consistent with standard estimating equation
theory. Cluster diagnostics and observation level diagnostics such as
leverage and Cook's distance are computed based on an approximation. Exact
versions of these diagnostics are computationally demanding and as of this
version, will not be included.

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
%doc %{rlibdir}/orth/DESCRIPTION
%doc %{rlibdir}/orth/html
%{rlibdir}/orth/R
%{rlibdir}/orth/NAMESPACE
%{rlibdir}/orth/Meta
%{rlibdir}/orth/data
%{rlibdir}/orth/help
%{rlibdir}/orth/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.1-1
- initial package for Fedora